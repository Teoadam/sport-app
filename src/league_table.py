"""Simple league table helper functions for a sport app example."""

from __future__ import annotations


def _validate_non_negative_int(name: str, value: int) -> None:
    """Validate that a value is a non-negative integer (bool is rejected)."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be int, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"{name} cannot be negative")


def calculate_points(wins: int, draws: int, losses: int) -> int:
    """Return total points based on 3-1-0 point system.

    Raises:
        ValueError: If any input is negative.
        TypeError: If any input is not an integer.
    """
    for name, value in {"wins": wins, "draws": draws, "losses": losses}.items():
        _validate_non_negative_int(name, value)

    return wins * 3 + draws


def goal_difference(goals_for: int, goals_against: int) -> int:
    """Return goal difference with validation."""
    for name, value in {"goals_for": goals_for, "goals_against": goals_against}.items():
        _validate_non_negative_int(name, value)

    return goals_for - goals_against


def total_matches(wins: int, draws: int, losses: int) -> int:
    """Return total number of played matches."""
    for name, value in {"wins": wins, "draws": draws, "losses": losses}.items():
        _validate_non_negative_int(name, value)

    return wins + draws + losses
