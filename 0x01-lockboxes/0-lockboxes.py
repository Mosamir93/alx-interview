#!/usr/bin/python3
"""
This module determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened.
    """
    n = len(boxes)
    unlocked_boxes = [False] * n
    unlocked_boxes[0] = True
    keys = boxes[0]
    for key in keys:
        if key < n and not unlocked_boxes[key]:
            unlocked_boxes[key] = True
            keys.extend(boxes[key])
    return all(unlocked_boxes)
