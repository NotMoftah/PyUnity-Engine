"""
    This is the Time module.

    -- Author : AbdElAziz Mofath
    -- Date: 4th of April 2018 at 10:00 PM
"""

__mouse_x, __mouse_y = 0, 0
__window_width, __window_height = 1, 1

__keyboard_keys_up = [False] * 256
__keyboard_keys_down = [False] * 256
__keyboard_keys_on_hold = [False] * 256

__mouse_keys_up = [False] * 10
__mouse_keys_down = [False] * 10
__mouse_keys_on_hold = [False] * 10


def __InputFrameUpdate(window_width, window_height):
    """
        Refresh the keys buffer and make sure the right key is pressed or released. same for mouse.
        
    :param window_width: the width of the current drawing window in pixels
    :param window_height: the height of the current drawing window in pixels
    """
    global __keyboard_keys_down, __keyboard_keys_up, __mouse_keys_up, __mouse_keys_down
    global __window_width, __window_height

    __window_width, __window_height = window_width, window_height

    __keyboard_keys_down = [False] * 256
    __keyboard_keys_up = [False] * 256

    __mouse_keys_down = [False] * 5
    __mouse_keys_up = [False] * 5


def __OnKeyDown(key, x, y):
    """
        Event of a keyboard key press
    :param key: the key been stroke
    :param x: the x pos of the mouse back then
    :param y: the y pos of the mouse back then
    """
    global __keyboard_keys_down
    global __keyboard_keys_on_hold

    if __keyboard_keys_on_hold[ord(key)] is False:
        __keyboard_keys_down[ord(key)] = True
    __keyboard_keys_on_hold[ord(key)] = True


def __OnKeyUp(key, x, y):
    """
        Event of a keyboard key released
    :param key: the key been stroke
    :param x: the x pos of the mouse back then
    :param y: the y pos of the mouse back then
    """

    global __keyboard_keys_up
    global __keyboard_keys_on_hold

    __keyboard_keys_up[ord(key)] = True
    __keyboard_keys_on_hold[ord(key)] = False


def __OnMouseClick(key, s, x, y):
    """
        Event of a mouse key stroke
    :param key: the key been stroke
    :param s: the state of the key
    :param x: the x pos of the mouse back then
    :param y: the y pos of the mouse back then
    """

    global __mouse_keys_up, __mouse_keys_down, __mouse_keys_on_hold

    if s == 0:
        __mouse_keys_down[key] = True
        __mouse_keys_on_hold[key] = True
    else:
        __mouse_keys_up[key] = True
        __mouse_keys_on_hold[key] = False


def __OnMouseMotion(x, y):
    """
        Event of a motion of the mouse
    :param x: the x pos of the mouse back then
    :param y: the y pos of the mouse back then
    """

    global __mouse_x, __mouse_y, __window_width, __window_height, __m_delta_x, __m_delta_y

    halfX = __window_width / 2
    halfY = __window_height / 2

    __m_delta_x = __mouse_x - (x - halfX) / +halfX
    __m_delta_y = __mouse_y - (y - halfY) / -halfY

    __mouse_x = (x - halfX) / +halfX
    __mouse_y = (y - halfY) / -halfY


def KeyDown(key):
    """
    :param key: latter of the key. for example: 'w'
    :return: True or False wither the key been pressed this frame or not.
    """
    return __keyboard_keys_down[ord(key)]


def KeyHold(key):
    """
    :param key: latter of the key. for example: 'w'
    :return: True or False wither the key is being hold down this frame or not.
    """

    return __keyboard_keys_on_hold[ord(key)]


def KeyUp(key):
    """
    :param key: latter of the key. for example: 'w'
    :return: True or False wither the key been released this frame or not.
    """

    return __keyboard_keys_up[ord(key)]


def MouseKeyUp(key):
    """
    :param key: int: 0 Mouse Left Bottom, 1 Mouse middle Bottom, 2 Mouse right Bottom
    :return: True or False wither the key been released this frame or not.
    """

    return __mouse_keys_up[key]


def MouseKeyDown(key):
    """
    :param key: int: 0 Mouse Left Bottom, 1 Mouse middle Bottom, 2 Mouse right Bottom
    :return: True or False wither the key been pressed this frame or not.
    """

    return __mouse_keys_down[key]


def MouseKeyHoldDown(key):
    """
    :param key: int: 0 Mouse Left Bottom, 1 Mouse middle Bottom, 2 Mouse right Bottom
    :return: True or False wither the key is being hold down this frame or not.
    """
    return __mouse_keys_on_hold[key]


def MousePosition():
    """
    :return: the position of the mouse referenced to the drawing window in range (-1, 1) in both x, y.
    """

    return __mouse_x, __mouse_y
