"""Alpha-Beta pruning implementation."""

from dataclasses import dataclass

from src.game_tree import GameTree
from src.minimax import is_terminal


@dataclass(frozen=True)
class PruningReport:
    """Result returned by Alpha-Beta search."""

    score: int
    leaves_seen: int
    cuts: int


def alpha_beta(
    position: GameTree,
    low_bar: float = float("-inf"),
    high_bar: float = float("inf"),
    is_max_turn: bool = True,
) -> PruningReport:
    """Evaluate a game tree using Alpha-Beta pruning."""
    if is_terminal(position):
        return PruningReport(score=position, leaves_seen=1, cuts=0)

    leaves_seen = 0
    cuts = 0

    if is_max_turn:
        best_score = float("-inf")
        for child_index, option in enumerate(position):
            report = alpha_beta(option, low_bar, high_bar, False)
            leaves_seen += report.leaves_seen
            cuts += report.cuts
            best_score = max(best_score, report.score)
            low_bar = max(low_bar, best_score)

            if high_bar <= low_bar:
                cuts += len(position) - child_index - 1
                break

        return PruningReport(score=int(best_score), leaves_seen=leaves_seen, cuts=cuts)

    best_score = float("inf")
    for child_index, option in enumerate(position):
        report = alpha_beta(option, low_bar, high_bar, True)
        leaves_seen += report.leaves_seen
        cuts += report.cuts
        best_score = min(best_score, report.score)
        high_bar = min(high_bar, best_score)

        if high_bar <= low_bar:
            cuts += len(position) - child_index - 1
            break

    return PruningReport(score=int(best_score), leaves_seen=leaves_seen, cuts=cuts)
