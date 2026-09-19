#!/usr/bin/env python3
"""Synthetic-only tests for the data-free timing-contrast utility."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from p4_directional_timing_effect import within_source_directional_timing_effect  # noqa: E402


class DirectionalTimingEffectTest(unittest.TestCase):
    """Test synthetic arithmetic and validation behavior of the timing utility."""

    def test_negative_effect_represents_a_negative_arithmetic_direction(self) -> None:
        """Return a negative value for the corresponding synthetic input pattern."""
        effect = within_source_directional_timing_effect(
            contingent_pre=[5.0, 5.0],
            contingent_post=[4.0, 4.0],
            control_pre=[5.0, 5.0],
            control_post=[5.0, 5.0],
        )

        self.assertAlmostEqual(effect, -1.0)

    def test_matched_condition_changes_cancel(self) -> None:
        """Return zero when synthetic condition changes have equal means."""
        effect = within_source_directional_timing_effect(
            contingent_pre=[2.0, 4.0],
            contingent_post=[3.0, 5.0],
            control_pre=[10.0],
            control_post=[11.0],
        )

        self.assertAlmostEqual(effect, 0.0)

    def test_positive_effect_represents_a_positive_arithmetic_direction(self) -> None:
        """Return a positive value for the corresponding synthetic input pattern."""
        effect = within_source_directional_timing_effect(
            contingent_pre=[1.0],
            contingent_post=[2.5],
            control_pre=[3.0, 3.0],
            control_post=[4.0, 4.0],
        )

        self.assertAlmostEqual(effect, 0.5)

    def test_rejects_empty_or_nonfinite_inputs(self) -> None:
        """Reject synthetic inputs that cannot define the arithmetic contrast."""
        invalid_inputs = (
            ([], [1.0], [1.0], [1.0]),
            ([1.0], [], [1.0], [1.0]),
            ([1.0], [1.0], [], [1.0]),
            ([1.0], [1.0], [1.0], [float("nan")]),
            ([1.0], ["not-a-number"], [1.0], [1.0]),
        )
        for values in invalid_inputs:
            with self.subTest(values=values):
                with self.assertRaises(ValueError):
                    within_source_directional_timing_effect(*values)


if __name__ == "__main__":
    unittest.main()
