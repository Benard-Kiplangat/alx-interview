#!/usr/bin/python3
"""
A solution to determine if a series of lockboxes can be opened
"""


def canUnlockAll(boxes):
    """
    A function that determines whether a series of
    locked boxes can be opened
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
