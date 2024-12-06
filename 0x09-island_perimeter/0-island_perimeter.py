#!/usr/bin/python3
"""Island perimeter module."""


def island_perimeter(grid):
    """Calculates the perimeter of
    an island described in grid."""
    perimeter = 0
    cols = len(grid)
    rows = len(grid[0])

    for i in range(cols):
        for j in range(rows):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
