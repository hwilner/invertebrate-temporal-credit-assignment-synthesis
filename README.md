# Invertebrate Temporal Credit Assignment Synthesis

This independent research repository records the current status of a cross-system temporal-credit-assignment synthesis and provides a deterministic, data-free timing-contrast helper.

## Research status

| Completed work | Outcome |
|---|---|
| Review of available source-specific records | The records remain separate and do not provide a pre-specified common bridge for a pooled benchmark. |
| Comparison of evidence readiness | P1 is directionally suggestive but unstable; P2 is inconclusive across reference families; P3 contains one bounded positive encoding result and one non-supportive route. |
| Cross-system synthesis | Not successful: no pooled effect, common benchmark, or shared mechanism can be justified from the available records. |
| Prospective timing helper | Implemented and tested on synthetic inputs only; it is not an empirical effect estimate. |

**Current conclusion:** the synthesis question remains **unresolved**. The existing records do not support pooling, ranking, or translating results into a shared biological mechanism.

## What is included

| Path | Contents |
|---|---|
| `src/p4_directional_timing_effect.py` | Pure timing-contrast arithmetic helper. |
| `tests/` | Synthetic tests for arithmetic direction, cancellation, and validation. |
| `tools/check_release_boundary.py` | Tracked-text and tracked-path release-boundary scanner. |
| `docs/` | Research status, methods scope, deferred directions, and contribution guidance. |

## Validation

```bash
make test
make check-release
```

## Keywords

Temporal credit assignment, evidence synthesis, *Aplysia*, *Drosophila*, computational neuroscience, reproducible research methods.

## Contributing

Contributions are welcome for data-free methods, synthetic tests, documentation, accessibility, and careful review of synthesis assumptions. Please read [Contributing](CONTRIBUTING.md) and the [research status](docs/STATUS_AND_PLAN.md) before opening a change.

## Documentation

- [Extended introduction for non-specialists](docs/EXTENDED_INTRODUCTION.md)
- [Methods: done, intended, and hygiene](docs/METHODS.md)
- [Introduction for new readers](docs/INTRODUCTION.md)
- [Current results and discussion](docs/CURRENT_RESULTS_AND_DISCUSSION.md)
- [Research status and plan](docs/STATUS_AND_PLAN.md)
- [Methods scope](docs/METHODS_SCOPE.md)
- [Release boundary](docs/RELEASE_BOUNDARY.md)
- [Deferred and dropped directions](docs/DEFERRED_AND_DROPPED_DIRECTIONS.md)
