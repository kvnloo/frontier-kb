---
id: inbox-cursor-p1-control-table-20260914
title: "Cursor: P1 MB specialist is useful on Hermes recovery; evolution-lab push blocked"
type: inbox
status: draft
created: 2026-09-14
updated: 2026-09-14
node: cursor
harnesses: [cursor]
domains: [ai-ml, neuroscience]
tags: [inbox, flyforge, p1]
confidence: high
---

# P1 mushroom-body specialist (local)

Operator asked to keep evolving the fly into something useful for this stack. Checked git, Linear, X.

- Linear: [PER-1524](https://linear.app/0ism/issue/PER-1524) Done. [PER-1525](https://linear.app/0ism/issue/PER-1525) Backlog (P1). PER-944 stays Backlog viewer. Did not mint into Todo.
- X: API credits depleted this run. SHERWOOD fly-DEX clip remains a FlyWire overlay, not a gym.
- Useful object: cheap Hermes recovery actions `{retry, restart_sandbox, escalate, noop, page_human}`. Not trading. Not MaleCNS SGD. Not Qwen.

Engine work is two commits on `cursor/p1-control-table-9425` in evolution-lab (`7ed11ee`, `20555e7`). L1 table: `local_plasticity` confirm **1.00** / val **0.979** / **640** params. Kill criterion does not fire. Patch backup: `inbox/cursor/evolution-lab-p1-control-table-9425.patch`.

**Blocker:** this Cloud Agent environment can read `kvnloo/evolution-lab` but cannot push it. Cursor GitHub App installation covers `frontier-kb` and `fly-wirehead` only. Add `kvnloo/evolution-lab` to the environment and the GitHub App, then `git push -u origin cursor/p1-control-table-9425` and open a draft PR to `nightly`.

Apply on evolution-lab (copy the patch out of this vault first):

```sh
cd /path/to/evolution-lab
git checkout -b cursor/p1-control-table-9425 origin/nightly
git am /path/to/frontier-kb/inbox/cursor/evolution-lab-p1-control-table-9425.patch
python -m unittest discover -s tests -p 'test_*.py'
python -m evolution_lab table --level 1
python -m evolution_lab advise '{"sandbox_alive": 0, "retry": 0, "budget": 1}'
```

## Links

- [[literature/lit-20260914-p1-control-table-kill-criterion]]
- [[inbox/cursor/inbox-cursor-evolution-lab-repo-20260912]]
