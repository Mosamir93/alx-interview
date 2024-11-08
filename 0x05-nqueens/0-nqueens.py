#!/usr/bin/python3
"""Nqueens module."""
import sys


def solve_nqueens(n):
    """Solves the problem."""
    def is_safe(board, row, col):
        for r, c in board:
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def build_board(board, row):
        """Builds the board."""
        if row == n:
            print(board)
            return
        for col in range(n):
            if is_safe(board, row, col):
                build_board(board + [(row, col)], row + 1)

    build_board([], 0)


def main():
    """Entry point."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number\n")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4\n")
        sys.exit(1)
    solve_nqueens(n)


if __name__ == "__main__":
    main()
