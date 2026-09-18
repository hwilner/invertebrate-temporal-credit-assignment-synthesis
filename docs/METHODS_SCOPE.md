# Methods Scope

## Conceptual focus

Temporal credit assignment concerns how a system could relate events separated in time when updating a representation or behavior. This repository treats that idea as a conceptual research topic. It does not use the topic to make claims about a particular system, mechanism, dataset, or outcome.

## Data-free timing contrast

The retained utility computes the difference between two mean pre/post changes supplied by a caller:

```text
mean(first_post) - mean(first_pre) - (mean(comparison_post) - mean(comparison_pre))
```

The formula is an arithmetic reference for synthetic inputs. Its sign is determined by the caller’s convention and has no biological interpretation within this repository. The utility performs input validation but no inference, estimation, source selection, data loading, or file access.

## Interpretation boundary

A mathematical contrast alone does not establish temporal credit assignment, causality, biological identity, or a comparison across systems. Any such interpretation would require material that is expressly excluded from this public staging tree.

## Implementation boundary

Public utilities should remain small, deterministic, and standard-library based where practical. They should document inputs, outputs, and errors with Google-style docstrings. Synthetic tests should demonstrate behavior through invented values only and should not create data or output files.
