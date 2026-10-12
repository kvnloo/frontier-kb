"""Minimal, pinned-source CRAM batching control; not the complete wave-3 study.

Usage (NumPy 2.3.5 / SciPy 1.17.0 used for the reported study):
  python reproduce_math372_wave3.py /path/to/openmc/deplete/cram.py > result.json
Use the file at OpenMC commit aa4afc41eb5421fb77351da863bca150be106a5e.
The exact Git blob is checked before selected AST nodes are executed. No download.

Credit: Maria Pusa, Antti Isotalo/Maria Pusa, OpenMC contributors (MIT),
and SciPy's Al-Mohy/Higham matrix-exponential action implementation.
Batching is conventional reuse, not a gain from OpenAI math family 325.
Only the numerical method is exercised, not OpenMC integration or transport.
The complete study also includes domain screens and a retained positivity failure.
"""
from __future__ import annotations

import argparse
import ast
from functools import partial
import hashlib
import json
import numbers
import os
from pathlib import Path
from types import SimpleNamespace
import time

# Process-local limits; set before importing numerical libraries.
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import numpy as np
import scipy
from scipy.sparse import csc_array, diags, eye_array
from scipy.sparse.linalg import expm_multiply, splu, spsolve

EXPECTED_BLOB = '3594ffbe8419aebd533d675631ead9001744510c'


def load_method(path: Path):
    raw = path.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if blob != EXPECTED_BLOB:
        raise ValueError(f'Unrecognized source blob: {blob}; require {EXPECTED_BLOB}')
    tree = ast.parse(raw)
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'IPFCramSolver')
    method = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == '__call__')
    names = {'c16_alpha', 'c16_theta', 'c16_alpha0'}
    assignments = [n for n in tree.body if isinstance(n, ast.Assign)
                   and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
                   and n.targets[0].id in names]

    def check_type(name, value, typ):
        if not isinstance(value, typ):
            raise TypeError(name)

    def check_greater_than(name, value, lower):
        if value <= lower:
            raise ValueError(name)

    bindings = dict(np=np, numbers=numbers, partial=partial, spsolve=spsolve, splu=splu,
                    csc_array=csc_array, eye_array=eye_array,
                    check_type=check_type, check_greater_than=check_greater_than)
    # Method and coefficient ASTs are unmodified; only imports/check helpers are bound here.
    module = ast.Module(body=assignments + [method], type_ignores=[])
    exec(compile(module, str(path), 'exec'), bindings)
    obj = SimpleNamespace(alpha=bindings['c16_alpha'], theta=bindings['c16_theta'],
                          alpha0=bindings['c16_alpha0'])
    return lambda A, B: bindings['__call__'](obj, A, B, 1.0, 1)


def run(path: Path, repeats: int) -> dict:
    if repeats < 3:
        raise ValueError('At least three paired repetitions required')
    kernel = load_method(path)
    rows = []
    for n in (64, 256, 1024):
        for columns in (1, 8, 32):
            for seed in (17, 29, 43):
                rates = 2.0 * np.random.default_rng(seed).uniform(0.25, 1.0, n - 1)
                A = diags([-np.r_[rates, 0.0], rates], [0, -1], shape=(n, n), format='csc')
                B = np.random.default_rng(seed + 1).random((n, columns))
                B /= B.sum(axis=0)
                reference = expm_multiply(A, B)
                modes = {
                    'columns': lambda: np.column_stack([kernel(A, B[:, i]) for i in range(columns)]),
                    # A one-column sparse solve returns a vector: adapt shape at the harness boundary.
                    'block': lambda: kernel(A, B) if columns > 1 else kernel(A, B[:, 0])[:, None],
                }
                answers = {name: fn() for name, fn in modes.items()}
                timings = {name: [] for name in modes}
                for rep in range(repeats):
                    order = list(modes) if rep % 2 == 0 else list(reversed(modes))
                    for name in order:
                        start = time.perf_counter_ns()
                        result = modes[name]()
                        timings[name].append((time.perf_counter_ns() - start) / 1e6)
                        if not np.isfinite(result).all():
                            raise AssertionError('Nonfinite numerical result')
                error = max(float(np.max(abs(x - reference))) for x in answers.values())
                mass = max(float(np.max(abs(x.sum(axis=0) - B.sum(axis=0)))) for x in answers.values())
                minimum = min(float(x.min()) for x in answers.values())
                difference = float(np.max(abs(answers['columns'] - answers['block'])))
                if error > 5e-12 or mass > 5e-12 or minimum < -5e-14 or difference > 5e-12:
                    raise AssertionError((n, columns, seed, error, mass, minimum, difference))
                rows.append(dict(n=n, columns=columns, seed=seed, raw_ms=timings,
                                 speed_ratio=float(np.median(timings['columns']) / np.median(timings['block'])),
                                 max_abs_error=error, mass_error=mass, minimum=minimum,
                                 block_column_difference=difference))
    return dict(source_blob=EXPECTED_BLOB, numerical_method_ast_unchanged=True,
                scope='synthetic same-operator numerical-kernel control; standalone check/import bindings',
                full_openmc_integration=False, math325_speedup_claim=False, gpu_tested=False,
                versions=dict(numpy=np.__version__, scipy=scipy.__version__),
                repeats=repeats, cases=rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--repeats', type=int, default=11)
    args = parser.parse_args()
    try:
        print(json.dumps(run(args.source, args.repeats), indent=2, allow_nan=False))
    except (OSError, ValueError, AssertionError) as exc:
        parser.exit(1, f'{exc}\n')
