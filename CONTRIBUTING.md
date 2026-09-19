# Contributing

Contributions are welcome to this independent research repository. Proposed changes should improve conceptual clarity, documentation, data-free utilities, or synthetic tests without introducing empirical claims or material outside the public boundary.

## Public boundary

Do not add research data, derived outputs, figures, downloads, archives, external source material or metadata, access logs, notebooks, or cached files. Do not add empirical findings, numerical research values, source-specific outcome statements, personal contact details, or statements that imply a venue or release decision. The complete boundary is described in [`docs/RELEASE_BOUNDARY.md`](docs/RELEASE_BOUNDARY.md).

## Code and tests

Retained utilities must be deterministic, data-free, and free of filesystem access to research-data or output locations. Use Google-style docstrings for public callables, covering a summary plus `Args`, `Returns`, and `Raises` when applicable. Add concise explanatory comments only where they clarify a non-obvious implementation choice. Tests must use synthetic inputs and must not create files in repository data or output paths.

## Documentation

Keep documentation accurate and conservative. Describe scope, assumptions, and exclusions rather than outcomes. Add public documentation only when it can stand on its own without external source metadata or private research context. Review [`docs/METHODS_SCOPE.md`](docs/METHODS_SCOPE.md) and [`docs/DEFERRED_AND_DROPPED_DIRECTIONS.md`](docs/DEFERRED_AND_DROPPED_DIRECTIONS.md) before expanding scope.

## Future Testing Opportunities

**Data-free software or documentation tests that contributors can work on now**

- Perform a manual contract review of the existing timing helper against `docs/METHODS_SCOPE.md`, checking that its documented inputs, arithmetic, validation, and interpretation remain limited to caller-supplied synthetic sequences. Record proposed wording changes only; do not change runtime code or the test suite.
- Conduct a plain-language review of the public documentation, checking whether a reader can distinguish the unresolved synthesis status from a negative result and can identify the difference between synthetic arithmetic and empirical evidence.
- Check the current public documents for consistent use of the comparison boundary: each should avoid implying a pooled effect, common benchmark, ranking, cross-system translation, or shared mechanism.
- Review the existing synthetic test descriptions and local-check instructions for clarity and reproducibility, proposing documentation-only corrections where a contributor could otherwise mistake a synthetic check for an empirical analysis.

**Research-facing tests requiring maintainer approval and an appropriate data boundary**

- Draft a proposed bridge specification for maintainer review before any candidate material is inspected. It should state the target, comparator, outcome, measurement scale, timing convention, mapping rule, and exclusion rule.
- After approval and only outside this public repository's data boundary, evaluate whether candidate records meet the approved bridge without changing their original meaning; retain non-comparable cases rather than forcing them into a shared result.
- After approval and only within an appropriate research boundary, evaluate whether pre-specified alternative bridge choices yield the same qualitative interpretation, with the alternatives and decision rule fixed before review.
- Before any interpretation is considered, ask whether a proposed benchmark keeps synthetic timing arithmetic separate from empirical inference; require a documented safeguard that the helper is not treated as evidence for a biological mechanism.

## Local checks

From a Git checkout, run the tracked-file boundary scanner and the synthetic standard-library test suite before sharing a change:

```bash
python3 tools/check_release_boundary.py
python3 -B -m unittest discover -s tests -v
```

The scanner intentionally reads only Git-tracked paths and tracked text. It cannot validate untracked local material; keep that material outside this tree.
