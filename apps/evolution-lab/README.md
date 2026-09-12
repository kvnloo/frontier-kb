# Evolution Lab lives in its own repo

The experiment engine is an **original** GitHub repo — not this path, not a vault package:

- Engine: [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab) ([PR #1](https://github.com/kvnloo/evolution-lab/pull/1))
- Protocol: [kvnloo/verified-oss-loop](https://github.com/kvnloo/verified-oss-loop)
- Maintainer roadmap: [ROADMAP.md](https://github.com/kvnloo/evolution-lab/blob/main/ROADMAP.md)
- Claimable P0: [evolution-lab#2](https://github.com/kvnloo/evolution-lab/issues/2)

This vault holds research notes only. VOL claim leases live on evolution-lab GitHub. Do not put the training loop back here. Do not fork FlyGym or OpenEvolve into this tree.

```sh
git clone https://github.com/kvnloo/evolution-lab.git
cd evolution-lab
pip install -e .
python -m evolution_lab gym-smoke
```
