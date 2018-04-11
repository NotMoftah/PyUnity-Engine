static_rect_list = []


def addStaticRect(rect_id, rect, rect_tag):
    global static_rect_list
    static_rect_list.append((rect_id, rect, rect_tag))


def delRect(rect_id):
    global static_rect_list
    for i in range(len(static_rect_list)):
        if static_rect_list[i][0] == rect_id:
            del static_rect_list[i]
            break


def slowRectCast(rect_a):
    for rect_id, rect_b, rect_tag in static_rect_list:
        if __IsCollision(rect_a, rect_b):
            return rect_id, rect_tag
    return None


def __PhysicsUpdate():
    pass


def __IsCollision(rect_a, rect_b):
    """
        :param rect_a:  (min x, min y, max x, max y)
        :param rect_b:  (min x, min y, max x, max y)
        :return: True or False wither they collide or not
    """
    if rect_a[0] > rect_b[2] or rect_a[2] < rect_b[0]:
        return False

    if rect_a[1] > rect_b[3] or rect_a[3] < rect_b[1]:
        return False

    return True
