#!/usr/bin/python3
"""
unlock all the boxes
The first box is open
and every box has a key to another box
"""


def openBoxes(unopenedBoxes, openedBoxes, boxes):
    """
    use all the keys as much as you can using set
    """
    if len(unopenedBoxes) == 0:
        if len(openedBoxes) == len(boxes):
            return True
        else:
            return False
    box = unopenedBoxes.pop()
    if box not in openedBoxes:
        for key in boxes[box]:
            if key not in openedBoxes and key < len(boxes):
                unopenedBoxes.add(key)
    openedBoxes.add(box)
    return openBoxes(unopenedBoxes, openedBoxes, boxes)


def canUnlockAll(boxes):
    """ using set """
    openedBoxes = set()
    unopenedBoxes = set()
    unopenedBoxes.add(0)
    x = openBoxes(unopenedBoxes, openedBoxes, boxes)
    return x
