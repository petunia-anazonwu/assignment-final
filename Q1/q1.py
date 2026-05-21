import random

def create_board(size: int = 8) -> list[list[int]]:
    """Creates an empty 8x8 chessboard initialized with zeros."""
    return [[0 for _ in range(size)] for _ in range(size)]

def print_board(board: list[list[int]]):
    """Prints the matrix neatly formatted to the console terminal."""
    size = len(board)
    print("\n" + "---" * size)
    for row in board:
        print(" ".join(f"{cell:2d}" for cell in row))
    print("---" * size + "\n")

def get_valid_moves(pos: tuple[int, int], board: list[list[int]]) -> list[tuple[int, int]]:
    """Finds all open valid L-shaped knight moves from the current position."""
    size = len(board)
    r, c = pos
    move_offsets = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    valid = []
    for dr, dc in move_offsets:
        nr, nc = r + dr, c + dc
        if 0 <= nr < size and 0 <= nc < size and board[nr][nc] == 0:
            valid.append((nr, nc))
    return valid

def KnightsTourLasVegas(startingPosition: tuple[int, int]) -> tuple[bool, list[list[int]]]:
    """Solves the Knight's Tour randomly via the Las Vegas approach."""
    board = create_board(8)
    r, c = startingPosition
    board[r][c] = 1
    current_pos = startingPosition
    
    for step in range(2, 65):
        moves = get_valid_moves(current_pos, board)
        if not moves:
            return False, board
            
        next_pos = random.choice(moves)
        nr, nc = next_pos
        board[nr][nc] = step
        current_pos = next_pos

    # Check if the last square can step back to the start
    final_moves = [
        (current_pos[0] + dr, current_pos[1] + dc)
        for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    ]
    if startingPosition in final_moves:
        return True, board
        
    return False, board

def KnightsTourBacktracking(startingPosition: tuple[int, int]) -> tuple[bool, list[list[int]]]:
    """Solves the Knight's Tour systematically using deterministic Backtracking."""
    board = create_board(8)
    r, c = startingPosition
    board[r][c] = 1
    
    move_offsets = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    def solve(curr_r: int, curr_c: int, move_count: int) -> bool:
        if move_count == 65:
            for dr, dc in move_offsets:
                if (curr_r + dr, curr_c + dc) == startingPosition:
                    return True
            return False
            
        # Warnsdorff's heuristic optimization to reduce execution duration
        moves = []
        for dr, dc in move_offsets:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] == 0:
                onward_count = len(get_valid_moves((nr, nc), board))
                moves.append((onward_count, nr, nc))
                
        moves.sort(key=lambda x: x[0])
        
        for _, nr, nc in moves:
            board[nr][nc] = move_count
            if solve(nr, nc, move_count + 1):
                return True
            board[nr][nc] = 0
            
        return False

    success = solve(r, c, 2)
    return success, board

def main():
    print("Welcome to the Closed Knight's Tour program!")
    print("Initial Empty Chessboard Layout:")
    print_board(create_board(8))
    
    while True:
        print("Select an execution approach:\n1. Backtracking Strategy\n2. Las Vegas Strategy\n3. Exit Program")
        choice = input("Enter option index (1-3): ").strip()
        
        if choice == '3':
            break
        if choice not in ['1', '2']:
            print("Invalid input! Try again.\n")
            continue
            
        try:
            row = int(input("Enter starting row (0-7): ").strip())
            col = int(input("Enter starting column (0-7): ").strip())
            if not (0 <= row < 8 and 0 <= col < 8):
                raise ValueError
        except ValueError:
            print("Invalid coordinates!\n")
            continue
            
        start_pos = (row, col)
        if choice == '1':
            success, final_board = KnightsTourBacktracking(start_pos)
        else:
            success, final_board = KnightsTourLasVegas(start_pos)
            
        print("SUCCESS" if success else "UNSUCCESSFUL")
        print_board(final_board)

if __name__ == "__main__":
    main()


