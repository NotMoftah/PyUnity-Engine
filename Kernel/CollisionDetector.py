import numpy as np

rect_list = []


def addRect(rect):
    """
        Add new rectangle collider to the matrix
    :param script_id: id of the script that owns the collider
    :param script_type: type of the string or any special message
    :param rect: rectangle (x1, x2, y1, y2)
    """
    rect_list.append(rect)


def badRectCast(rectangle):
    collisions = []
    for rect in rect_list:
        if checRectCollision(rectangle, rect):
            collisions.append((script_id, script_type))
    return collisions


def checRectCollision(rect1, rect2):
    pass