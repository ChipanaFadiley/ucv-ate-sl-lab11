import pytest

from src.tic_tac_toe import (
    AGENT,
    HUMAN,
    board_from_rows,
    choose_best_move,
    empty_board,
    game_status,
    is_draw,
    play_move,
    render_position_guide,
    render_board,
    winner,
)


def test_choose_best_move_wins_when_available():
    board = board_from_rows("OO-", "XX-", "---")

    choice = choose_best_move(board)

    assert choice.index == 2
    assert choice.score == 10
    assert choice.positions_seen > 0


def test_choose_best_move_blocks_human_win():
    board = board_from_rows("XX-", "O--", "---")

    choice = choose_best_move(board)

    assert choice.index == 2


def test_winner_detects_diagonal_win():
    board = board_from_rows("OXX", "-O-", "X-O")

    assert winner(board) == AGENT


def test_draw_is_detected_without_winner():
    board = board_from_rows("XOX", "OOX", "XXO")

    assert is_draw(board)


def test_play_move_rejects_occupied_square():
    board = play_move(empty_board(), 4, HUMAN)

    with pytest.raises(ValueError):
        play_move(board, 4, AGENT)


def test_play_move_rejects_square_outside_board():
    with pytest.raises(ValueError):
        play_move(empty_board(), 9, HUMAN)


def test_render_board_contains_grid_lines():
    board = board_from_rows("XO-", "---", "--O")

    assert "---------" in render_board(board)


def test_position_guide_shows_indexes_for_empty_squares():
    board = board_from_rows("XO-", "---", "--O")

    guide = render_position_guide(board)

    assert "2" in guide
    assert "8" not in guide


def test_game_status_reports_agent_win():
    board = board_from_rows("OOO", "XX-", "---")

    assert game_status(board) == "Agent wins."


def test_choose_best_move_returns_no_move_for_finished_board():
    board = board_from_rows("OOO", "XX-", "---")

    choice = choose_best_move(board)

    assert choice.index == -1
    assert choice.positions_seen == 0
