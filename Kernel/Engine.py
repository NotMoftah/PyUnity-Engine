"""
    This is the Engine module.

    -- Author : AbdElAziz Mofath
    -- Date: 4th of April 2018 at 7:00 PM
"""

import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from Kernel import Time, Input, Camera, EventManager


def start():
    """
        Start the engine hence the game.
    """
    __init()
    EventManager.loadScripts()
    EventManager.castStart()
    glutMainLoop()


def __init():
    """
        Typical OpenGL init function
    """
    glutInit()
    pygame.init()
    glutInitWindowSize(500, 500)
    glutCreateWindow(b'Game Engine')
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_WINDOW_DOUBLEBUFFER)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Gl Functions
    glutSetCursor(1)
    glutKeyboardFunc(Input.__OnKeyDown)
    glutKeyboardUpFunc(Input.__OnKeyUp)
    glutMouseFunc(Input.__OnMouseClick)
    glutMotionFunc(Input.__OnMouseMotion)
    glutPassiveMotionFunc(Input.__OnMouseMotion)

    glutDisplayFunc(__GameLoopManager)
    glutIdleFunc(__GameLoopManager)


def __GameLoopManager():
    """
        The main loop in which everything take place in order.
    """
    Time.__UpdateDeltaTime()

    __FrameUpdate()
    __RenderUpdate()

    __InputUpdate()
    __PhysicsUpdate()
    __LateFrameUpdate()

    EventManager.collectGarbage()
    Time.__SleepTimeToLockFramsOn(60)


def __InputUpdate():
    Input.__InputFrameUpdate(glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))


def __FrameUpdate():
    EventManager.castUpdate()


def __RenderUpdate():
    glLoadIdentity()

    glClearColor(Camera.clearColor.x, Camera.clearColor.y, Camera.clearColor.z, .0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    screenWidthRatio = glutGet(GLUT_WINDOW_WIDTH) / 500
    screenHeightRatio = glutGet(GLUT_WINDOW_HEIGHT) / 500

    glOrtho(-Camera.size * screenWidthRatio, Camera.size * screenWidthRatio,
            -Camera.size * screenHeightRatio, Camera.size * screenHeightRatio,
            Camera.near, -Camera.far)

    Camera.applyTransformation()
    EventManager.castRender()
    glutSwapBuffers()


def __PhysicsUpdate():
    pass


def __LateFrameUpdate():
    EventManager.castLateUpdate()


start()
