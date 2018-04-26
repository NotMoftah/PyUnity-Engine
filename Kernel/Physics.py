__box_dict = {}


def addBox(box):
    __box_dict[box.collider_id] = [box, True]


def __EnableCollider(collider_id):
    if collider_id in __box_dict:
        __box_dict[collider_id][1] = True


def __DisableCollider(collider_id):
    if collider_id in __box_dict:
        __box_dict[collider_id][1] = False


def __DestroyCollider(collider_id):
    if collider_id in __box_dict:
        del __box_dict[collider_id]


def __PhysicsUpdate():
    """
        Sort and sweep collision detection.

        #1 Sort all the box collider based on their X or Y axis.
        #2 Clear all previous frame collisions.
        #3 Sweep the list from left to right and search for all collisions.
            * Sweep only collider with event method hooked to it.
        #4 trigger all BoxCollider2D collision events

        * Time complexity is almost always n log n unless all the boxes collider together then it's n ** 2.
            - In that case it's optimal because we have to alert evey box that he has collied with the others.
                - If there's no event attached to collider it'll always be n log n.

        * Space complexity is always N + K. where K is max number of collisions.
    """
    box_list = [v[0] for k, v in __box_dict.items() if v[1] is True]
    box_list.sort(key=lambda x: x.start_pos_x())

    for i in range(len(box_list)):
        for j in range(i + 1, len(box_list)):
            if box_list[i].end_pos_x() < box_list[j].start_pos_x():
                break

            if box_list[i].is_collision(box_list[j]):
                box_list[i].trigger_hit_event(box_list[j].collider_id, box_list[j].collider_tag)
                box_list[j].trigger_hit_event(box_list[i].collider_id, box_list[i].collider_tag)
                break
