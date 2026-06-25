"""Game tree samples for Minimax and Alpha-Beta pruning.

A game tree is represented with nested lists. Internal nodes are lists and
terminal nodes are integer scores.
"""

from typing import TypeAlias

GameTree: TypeAlias = int | list["GameTree"]


def sample_tree() -> GameTree:
    """Return a small demonstration tree.

    With alternating MAX/MIN turns from the root, the expected value is 3.
    """
    return [
        [3, 5],
        [2, 9],
    ]


def medium_tree() -> GameTree:
    """Return a deeper tree where Alpha-Beta can prune some branches.

    With alternating MAX/MIN/MAX turns from the root, the expected value is 7.
    """
    return [
        [[3, 5], [6, 9]],
        [[1, 2], [0, -1]],
        [[7, 4], [8, 6]],
    ]


def ordered_tree_for_pruning() -> GameTree:
    """Return a tree ordered to make pruning easier.

    With alternating MAX/MIN/MAX turns from the root, the expected value is 8.
    """
    return [
        [[10, 9], [8, 7]],
        [[6, 5], [4, 3]],
        [[2, 1], [0, -1]],
    ]


def unbalanced_tree() -> GameTree:
    """Return an additional tree with different branching factors."""
    return [
        [[4, -2, 11], [7]],
        [[5, 1], [12, 3], [2]],
        [[9], [0, 6]],
    ]
