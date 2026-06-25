"""Simple Tic-Tac-Toe agent powered by Alpha-Beta search."""

from dataclasses import dataclass

Board = tuple[str, ...]

HUMAN = "X"
AGENT = "O"
EMPTY = " "

WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


@dataclass(frozen=True)
class MoveChoice:
    """Best move returned by the Tic-Tac-Toe agent."""

    index: int
    score: int
    positions_seen: int


def empty_board() -> Board:
    """Return a new empty board."""
    return (EMPTY,) * 9


def available_moves(board: Board) -> list[int]:
    """Return indexes where a move can be played."""
    return [index for index, cell in enumerate(board) if cell == EMPTY]


def play_move(board: Board, index: int, marker: str) -> Board:
    """Return a new board after placing a marker."""
    if index < 0 or index >= len(board):
        raise ValueError("The selected square is outside the board.")
    if board[index] != EMPTY:
        raise ValueError("The selected square is already occupied.")

    next_board = list(board)
    next_board[index] = marker
    return tuple(next_board)


def winner(board: Board) -> str | None:
    """Return the winner marker when the game is over."""
    for first, second, third in WINNING_LINES:
        if board[first] != EMPTY and board[first] == board[second] == board[third]:
            return board[first]

    return None


def is_draw(board: Board) -> bool:
    """Return True when the board is full and no player won."""
    return winner(board) is None and EMPTY not in board


def evaluate(board: Board) -> int:
    """Score a terminal board from the agent perspective."""
    current_winner = winner(board)
    if current_winner == AGENT:
        return 10
    if current_winner == HUMAN:
        return -10
    return 0


def _search(
    board: Board,
    agent_turn: bool,
    alpha: float,
    beta: float,
) -> tuple[int, int]:
    """Return score and visited positions for the current board."""
    if winner(board) is not None or is_draw(board):
        return evaluate(board), 1

    seen = 0

    if agent_turn:
        best_score = float("-inf")
        for move in available_moves(board):
            score, child_seen = _search(play_move(board, move, AGENT), False, alpha, beta)
            seen += child_seen
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return int(best_score), seen

    best_score = float("inf")
    for move in available_moves(board):
        score, child_seen = _search(play_move(board, move, HUMAN), True, alpha, beta)
        seen += child_seen
        best_score = min(best_score, score)
        beta = min(beta, best_score)
        if beta <= alpha:
            break

    return int(best_score), seen


def choose_best_move(board: Board) -> MoveChoice:
    """Choose the best move for the agent using Alpha-Beta pruning."""
    if winner(board) is not None or is_draw(board):
        return MoveChoice(index=-1, score=evaluate(board), positions_seen=0)

    best_move = -1
    best_score = float("-inf")
    positions_seen = 0

    for move in available_moves(board):
        score, seen = _search(play_move(board, move, AGENT), False, float("-inf"), float("inf"))
        positions_seen += seen
        if score > best_score:
            best_score = score
            best_move = move

    return MoveChoice(index=best_move, score=int(best_score), positions_seen=positions_seen)


def board_from_rows(top: str, middle: str, bottom: str) -> Board:
    """Build a board from three 3-character strings."""
    board = tuple(top + middle + bottom)
    if len(board) != 9:
        raise ValueError("The board must contain exactly 9 cells.")
    return tuple(EMPTY if cell == "-" else cell for cell in board)


def render_board(board: Board) -> str:
    """Return a text representation of the board."""
    rows = [" | ".join(board[start : start + 3]) for start in range(0, 9, 3)]
    return "\n---------\n".join(rows)


def render_position_guide(board: Board) -> str:
    """Return the board showing indexes for empty cells."""
    guide = tuple(str(index) if cell == EMPTY else cell for index, cell in enumerate(board))
    return render_board(guide)


def game_status(board: Board) -> str:
    """Return a short status message for the current board."""
    current_winner = winner(board)
    if current_winner == HUMAN:
        return "Human wins."
    if current_winner == AGENT:
        return "Agent wins."
    if is_draw(board):
        return "Draw."
    return "Game in progress."


def run_console_game() -> None:
    """Play a simple console Tic-Tac-Toe game against the Alpha-Beta agent."""
    board = empty_board()
    print("\nTic-Tac-Toe console game")
    print("You are X. Choose a square from 0 to 8.")

    while winner(board) is None and not is_draw(board):
        print("\nCurrent board:")
        print(render_position_guide(board))
        raw_move = input("Your move: ").strip()

        try:
            board = play_move(board, int(raw_move), HUMAN)
        except (ValueError, TypeError):
            print("Invalid move. Try again.")
            continue

        if winner(board) is not None or is_draw(board):
            break

        choice = choose_best_move(board)
        board = play_move(board, choice.index, AGENT)
        print(f"Agent plays: {choice.index} (score {choice.score})")

    print("\nFinal board:")
    print(render_board(board))
    print(game_status(board))
