#!/usr/bin/python3
"""Determines if all boxes can be opened """


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened """
    # Set of visited boxes
    visited = set()

    # Recursive helper function to explore all reachable boxes
    def dfs(i):
        # Mark the current box as visited
        visited.add(i)

        # Explore each box that can be reached from the current box
        for j in boxes[i]:
            if j not in visited:
                dfs(j)

    # Start the depth-first search from the first box (which is unlocked)
    dfs(0)

    return len(visited) == len(boxes)
