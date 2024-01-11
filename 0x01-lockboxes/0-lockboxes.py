#!/usr/bin/python3
"""
method to unlock boxes
"""


def canUnlockAll(boxes):
    """
    A method that checks if all boxes contains keys to other box
    """
    if not boxes or not boxes[0]:
        return False

    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    keys = set(boxes[0])

    while True:
        prev_unlocked = sum(unlocked)

        for i in range(num_boxes):
            if unlocked[i]:
                keys.update(boxes[i])

        for key in keys:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True

        if sum(unlocked) == prev_unlocked:
            break

    return sum(unlocked) == num_boxes
