# Contributing

Contributions are welcome to this independent research repository. Proposed changes should improve conceptual clarity, documentation, data-free utilities, or synthetic tests without introducing empirical claims or material outside the public boundary.

## Public boundary

Do not add research data, derived outputs, figures, downloads, archives, external source material or metadata, access logs, notebooks, or cached files. Do not add empirical findings, numerical research values, source-specific outcome statements, personal contact details, or statements that imply a venue or release decision. The complete boundary is described in [`docs/RELEASE_BOUNDARY.md`](docs/RELEASE_BOUNDARY.md).

## Code and tests

Retained utilities must be deterministic, data-free, and free of filesystem access to research-data or output locations. Use Google-style docstrings for public callables, covering a summary plus `Args`, `Returns`, and `Raises` when applicable. Add concise explanatory comments only where they clarify a non-obvious implementation choice. Tests must use synthetic inputs and must not create files in repository data or output paths.

## Documentation

Keep documentation accurate and conservative. Describe scope, assumptions, and exclusions rather than outcomes. Add public documentation only when it can stand on its own without external source metadata or private research context. Review [`docs/METHODS_SCOPE.md`](docs/METHODS_SCOPE.md) and [`docs/DEFERRED_AND_DROPPED_DIRECTIONS.md`](docs/DEFERRED_AND_DROPPED_DIRECTIONS.md) before expanding scope.

## Local checks

From a Git checkout, run the tracked-file boundary scanner and the synthetic standard-library test suite before sharing a change:

```bash
python3 tools/check_release_boundary.py
python3 -B -m unittest discover -s tests -v
```

The scanner intentionally reads only Git-tracked paths and tracked text. It cannot validate untracked local material; keep that material outside this tree.
