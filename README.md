# Invertebrate Temporal Credit Assignment Synthesis

## Scope

This independent research repository contains a conservative, data-free starting point for discussing temporal credit assignment in invertebrate systems. It provides release-boundary documentation and a small pure-Python timing-contrast helper for synthetic examples. It contains no research data, external source material, empirical findings, figures, or analysis outputs, and it makes no empirical claims.

## Current status

**Public staging status:** this tree contains only conceptual documentation, synthetic tests, and data-free utility code. This status statement supersedes earlier staging language that could be read as reporting completed evidence review, source access, analysis, or findings. Such material is not part of this public tree.

## Contents

| Path | Contents |
|---|---|
| [`docs/STATUS_AND_PLAN.md`](docs/STATUS_AND_PLAN.md) | Current scope and maintenance plan. |
| [`docs/METHODS_SCOPE.md`](docs/METHODS_SCOPE.md) | Conceptual and implementation boundaries. |
| [`docs/DEFERRED_AND_DROPPED_DIRECTIONS.md`](docs/DEFERRED_AND_DROPPED_DIRECTIONS.md) | Work excluded from this public tree. |
| [`docs/RELEASE_BOUNDARY.md`](docs/RELEASE_BOUNDARY.md) | Public-release rules and the tracked-file scanner. |
| [`src/p4_directional_timing_effect.py`](src/p4_directional_timing_effect.py) | Pure arithmetic helper for synthetic timing contrasts. |
| [`tests/`](tests) | Synthetic, data-free tests. |
| [`tools/check_release_boundary.py`](tools/check_release_boundary.py) | Scanner for tracked paths and tracked text. |
| [`Makefile`](Makefile) | Dependency-free `make test` and `make check-release` targets. |

## Keywords

invertebrate neurobiology; temporal credit assignment; computational neuroscience; research methods; reproducibility; data-free testing

## Contributing

Contributions are welcome when they preserve the project’s independent, data-free public boundary. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/RELEASE_BOUNDARY.md`](docs/RELEASE_BOUNDARY.md) before proposing a change.
