"""
    This is the camera module. the camera is used to render the scene from a specific point.

    the camera has:
        Position, Rotation that control the POV of the game
        Near, Far that control how far the camera will render
        Size that control how wide the camera is. it also works a zooming lens.

    during the game control only position and rotation to avoid any errors.

    -- Author : AbdElAziz Mofath
    -- Date: 4th of April 2018 at 8:10 PM
"""

from OpenGL.GL import glTranslate, glRotatef
from Kernel.Utilities import Vector3

__swr, __shr = 0, 0
size, near, far = 5, 0.1, 100.

clearColor = Vector3(1, 1, 1)

position = Vector3(0, 0, -10)
rotation = Vector3(0, 0, 0)


def applyTransformation(screenWidthRatio, screenHeightRatio):
    """
        This function is used to apply the camera transformation to the game.
        it must be used only before calling every object in the game.

        it only do transformation and rotation. so scaling.
    """
    global position, __swr, __shr
    __swr, __shr = screenWidthRatio, screenHeightRatio

    glTranslate(-position.x, -position.y, -position.z)

    glRotatef(rotation.x, 1, 0, 0)
    glRotatef(rotation.y, 0, 1, 0)
    glRotatef(rotation.z, 0, 0, 1)


def screenToWorld(vec):
    global position, __swr, __shr
    x, y = vec.x * __swr * size, vec.y * __shr * size
    return Vector3(position.x + x, position.y + y, 0)
