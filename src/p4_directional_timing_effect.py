#!/usr/bin/env python3
"""Provide a data-free arithmetic utility for synthetic timing contrasts.

The module accepts numeric sequences supplied by a caller and performs no file,
network, source-discovery, or research-data operations. It is a small reference
implementation for testing an arithmetic definition, not an empirical method.
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from statistics import fmean


def _finite_mean(values: Sequence[float], label: str) -> float:
    """Return the finite arithmetic mean of a non-empty numeric sequence.

    Args:
        values: Numeric values supplied for one condition and time point.
        label: Input label included in a validation error.

    Returns:
        Arithmetic mean of ``values`` as a float.

    Raises:
        ValueError: If ``values`` is empty, non-numeric, or includes a non-finite value.
    """
    if not values:
        raise ValueError(f"{label} must contain at least one timing value")
    try:
        converted = [float(value) for value in values]
    except (TypeError, ValueError) as error:
        raise ValueError(f"{label} must contain only numeric timing values") from error
    if not all(math.isfinite(value) for value in converted):
        raise ValueError(f"{label} must contain only finite timing values")
    return fmean(converted)


def within_source_directional_timing_effect(
    contingent_pre: Sequence[float],
    contingent_post: Sequence[float],
    control_pre: Sequence[float],
    control_post: Sequence[float],
) -> float:
    """Calculate the difference between two mean pre/post timing changes.

    The calculation is ``mean(contingent_post) - mean(contingent_pre) -
    (mean(control_post) - mean(control_pre))``. Its sign is an arithmetic
    direction set by the caller's input convention; this helper assigns no
    biological or empirical interpretation to that direction.

    Args:
        contingent_pre: Values before the first condition's change.
        contingent_post: Values after the first condition's change.
        control_pre: Values before the comparison condition's change.
        control_post: Values after the comparison condition's change.

    Returns:
        Difference between the two mean pre/post changes in the input unit.

    Raises:
        ValueError: If an input sequence is empty, non-numeric, or non-finite.
    """
    # Validate each input separately so an invalid caller input has a clear label.
    contingent_change = _finite_mean(
        contingent_post, "contingent_post"
    ) - _finite_mean(contingent_pre, "contingent_pre")
    control_change = _finite_mean(control_post, "control_post") - _finite_mean(
        control_pre, "control_pre"
    )
    return contingent_change - control_change
