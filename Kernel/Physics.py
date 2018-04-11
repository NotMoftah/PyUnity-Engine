__box_list = []


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
    __box_list.sort(key=lambda box: box.__start_pos_x())

    for box in __box_list:
        box.__clear_collision()

    for i in range(len(__box_list)):
        j = i

        if __box_list[i].__method is not None:
            while __box_list[i].__end_pos_x() < __box_list[j].__start_pos_x():
                if __box_list[i].__is_collision(__box_list[j]):
                    __box_list[i].__append_collision(__box_list[j].tag)
                    __box_list[j].__append_collision(__box_list[i].tag)

                j = j + 1

        __box_list[i].__trigger_event()
