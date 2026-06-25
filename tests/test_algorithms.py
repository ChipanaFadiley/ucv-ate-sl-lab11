from src.alpha_beta import alpha_beta
from src.game_tree import (
    medium_tree,
    ordered_tree_for_pruning,
    sample_tree,
    unbalanced_tree,
)
from src.minimax import minimax


def test_minimax_sample_tree_uses_alternating_turns():
    result = minimax(sample_tree())

    assert result.score == 3
    assert result.leaves_seen == 4


def test_alpha_beta_sample_tree_matches_minimax():
    tree = sample_tree()

    assert alpha_beta(tree).score == minimax(tree).score


def test_minimax_medium_tree_returns_real_minimax_value():
    result = minimax(medium_tree())

    assert result.score == 7


def test_alpha_beta_medium_tree_matches_minimax_and_saves_work():
    tree = medium_tree()
    minimax_result = minimax(tree)
    alpha_beta_result = alpha_beta(tree)

    assert alpha_beta_result.score == minimax_result.score
    assert alpha_beta_result.leaves_seen <= minimax_result.leaves_seen


def test_alpha_beta_ordered_tree_prunes_branches():
    result = alpha_beta(ordered_tree_for_pruning())

    assert result.score == 8
    assert result.cuts > 0


def test_alpha_beta_unbalanced_tree_matches_minimax():
    tree = unbalanced_tree()

    assert alpha_beta(tree).score == minimax(tree).score
