"""Minimax search implementation."""

from dataclasses import dataclass

from src.game_tree import GameTree


@dataclass(frozen=True)
class SearchReport:
    """Result returned by a game-tree search."""

    score: int
    leaves_seen: int


def is_terminal(position: GameTree) -> bool:
    """Return True when the position is a terminal score."""
    return isinstance(position, int)


def minimax(position: GameTree, is_max_turn: bool = True) -> SearchReport:
    """Evaluate a game tree using the Minimax algorithm."""
    if is_terminal(position):
        return SearchReport(score=position, leaves_seen=1)

    child_reports = [minimax(option, not is_max_turn) for option in position]
    leaves_seen = sum(report.leaves_seen for report in child_reports)
    scores = [report.score for report in child_reports]

    if is_max_turn:
        return SearchReport(score=max(scores), leaves_seen=leaves_seen)

    return SearchReport(score=min(scores), leaves_seen=leaves_seen)
