#!usr/bin/python3
"""method to unlock boxes
"""


def canUnlockAll(boxes):
    """
    A method that checks if all boxes contains a keys to other box
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = set(boxes[0])
    
    while True:
        prev_unlocked = sum(unlocked)
        for i in range(len(boxes)):
            if unlocked[i]:
                keys.update(boxes[i])
        for key in keys:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
        if sum(unlocked) == prev_unlocked:
            break
        
    return sum(unlocked) == len(boxes)
                