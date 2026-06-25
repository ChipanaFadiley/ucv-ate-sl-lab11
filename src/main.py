"""Command line entry point for Laboratory 11."""

import argparse
from collections.abc import Callable

from src.alpha_beta import alpha_beta
from src.game_tree import (
    GameTree,
    medium_tree,
    ordered_tree_for_pruning,
    sample_tree,
    unbalanced_tree,
)
from src.minimax import minimax
from src.tic_tac_toe import (
    AGENT,
    board_from_rows,
    choose_best_move,
    play_move,
    render_board,
    run_console_game,
)


TreeFactory = Callable[[], GameTree]


def compare_algorithms(tree_name: str, build_tree: TreeFactory) -> None:
    """Print a compact comparison between Minimax and Alpha-Beta."""
    tree = build_tree()
    minimax_report = minimax(tree)
    pruning_report = alpha_beta(tree)

    print(f"\nTree: {tree_name}")
    print("-" * 44)
    print(f"Minimax score: {minimax_report.score}")
    print(f"Minimax leaves seen: {minimax_report.leaves_seen}")
    print(f"Alpha-Beta score: {pruning_report.score}")
    print(f"Alpha-Beta leaves seen: {pruning_report.leaves_seen}")
    print(f"Alpha-Beta cuts: {pruning_report.cuts}")


def show_tic_tac_toe_demo() -> None:
    """Print a short Tic-Tac-Toe decision demo."""
    board = board_from_rows("XO-", "X--", "O--")
    choice = choose_best_move(board)
    next_board = play_move(board, choice.index, AGENT)

    print("\nTic-Tac-Toe Alpha-Beta demo")
    print("-" * 44)
    print("Current board:")
    print(render_board(board))
    print(f"Agent move: {choice.index}")
    print(f"Move score: {choice.score}")
    print(f"Positions seen: {choice.positions_seen}")
    print("Next board:")
    print(render_board(next_board))


def run_examples() -> None:
    """Run the laboratory examples."""
    compare_algorithms("Sample Tree", sample_tree)
    compare_algorithms("Medium Tree", medium_tree)
    compare_algorithms("Ordered Tree", ordered_tree_for_pruning)
    compare_algorithms("Unbalanced Tree", unbalanced_tree)
    show_tic_tac_toe_demo()


def main() -> None:
    """Run examples or the optional console game."""
    parser = argparse.ArgumentParser(description="Laboratory 11 runner")
    parser.add_argument(
        "--play",
        action="store_true",
        help="start a console Tic-Tac-Toe game against the Alpha-Beta agent",
    )
    args = parser.parse_args()

    if args.play:
        run_console_game()
        return

    run_examples()


if __name__ == "__main__":
    main()
