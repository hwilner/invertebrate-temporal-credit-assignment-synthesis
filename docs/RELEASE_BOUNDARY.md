# Release Boundary

## Rule

This public staging tree is limited to documentation, data-free source code, synthetic tests, and lightweight configuration. It must not contain research data, derived outputs, figures, downloads, archives, external source material, source-specific metadata, access logs, notebooks, caches, or result-bearing documentation.

## Content allowed in the tree

| Category | Boundary |
|---|---|
| Documentation | Scope, assumptions, exclusions, contribution guidance, and maintenance instructions stated without empirical claims. |
| Source code | Deterministic, data-free utilities that do not access research-data or output paths. |
| Tests | Synthetic tests that do not read local research material or write data or output locations. |
| Tooling | Dependency-free checks that inspect tracked repository content only. |

## Content excluded from the tree

Excluded material includes raw or transformed data; tables of findings; numerical research values; figures and figure specifications; downloaded files; archives; external source records or metadata; internal indexes; access logs; notebooks; generated outputs; and caches. The exclusions apply even when a file is small or appears illustrative.

## Tracked-file scanner

`tools/check_release_boundary.py` is a dependency-free release-boundary check. From a Git checkout, run:

```bash
python3 tools/check_release_boundary.py
```

The scanner obtains its candidate paths with `git ls-files`, checks those tracked paths for prohibited locations and file types, and reads only tracked textual files for clear boundary markers such as external URLs, DOI-like identifiers, and email addresses. It never walks local data directories, reads untracked or ignored content, accesses a network, or writes files. It is a guardrail rather than a substitute for human review.

A staging folder without Git metadata cannot supply a tracked-file set; in that situation the scanner exits without inspecting local files. Run it after the tree is placed in its intended Git checkout.

## Human review

Before sharing a revision, confirm that its documentation uses conservative language, contains no empirical or source-specific outcome claims, and accurately reflects the current contents. Review [`STATUS_AND_PLAN.md`](STATUS_AND_PLAN.md) and [`METHODS_SCOPE.md`](METHODS_SCOPE.md) alongside the scanner.
