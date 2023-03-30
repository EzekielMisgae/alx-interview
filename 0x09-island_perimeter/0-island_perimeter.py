#!/usr/bin/python3
"""Check if the grid is empty"""


def island_perimeter(grid):
    """Check if the grid is empty"""
    if not grid:
        return 0

    # Get the dimensions of the grid
    rows, cols = len(grid), len(grid[0])

    # Initialize the perimeter to zero
    perimeter = 0

    # Loop over all cells in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is land
            if grid[i][j] == 1:
                # Check if the cell to the left is water or out of bounds
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check if the cell to the right is water or out of bounds
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
                # Check if the cell above is water or out of bounds
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check if the cell below is water or out of bounds
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1

    return perimeter
