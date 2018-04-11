import numpy as np
import bisect
import time

data_type = [('start_point', float), ('end_point', float), ('tag', 'S20')]
lst = [(-2, 10, 'string'), (-2, 9, 'awesome_player')]
arr = np.array(lst, dtype=data_type)
arr.sort(order='start_point')
print(arr)

quit()
start = time.time()
for i in range(10000):
    rand = np.random.randint(0, 100)
    index = bisect.bisect_left(arr, rand)
    arr = np.concatenate((arr[:index], [rand], arr[index:]))

print(time.time() - start, len(arr))


start = time.time()
for i in range(1000):
    rand = np.random.randint(0, 100)
    index = bisect.bisect_left(arr, rand)
    arr = np.concatenate((arr[:index], [rand], arr[index:]))

print(time.time() - start, len(arr))


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
    phy


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
