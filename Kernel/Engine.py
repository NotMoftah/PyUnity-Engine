"""
    This is the Engine module.

    -- Author : AbdElAziz Mofath
    -- Date: 4th of April 2018 at 7:00 PM
"""


from OpenGL.GL import *
from OpenGL.GLUT import *
from Kernel import Time, Input, Camera, EventManager


def start(scripts='defult'):
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
    glutInitWindowSize(500, 500)
    glutCreateWindow(b'Game Engine')
    glutInitDisplayMode(GLUT_DEPTH | GLUT_WINDOW_DOUBLEBUFFER)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

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
    __FrameUpdate()
    __RenderUpdate()

    __InputUpdate()
    __PhysicsUpdate()
    __LateFrameUpdate()

    Time.__UpdateDeltaTime()
    Time.__SleepTimeToLockFramsOn(60)


def __InputUpdate():
    Input.__InputFrameUpdate(glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))


def __FrameUpdate():
    EventManager.castUpdate()
    pass


def __RenderUpdate():
    glLoadIdentity()

    glClearColor(Camera.clearColor.x, Camera.clearColor.y,
                 Camera.clearColor.z, 1.)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    screenRatio = glutGet(GLUT_WINDOW_WIDTH) / glutGet(GLUT_WINDOW_HEIGHT)

    glOrtho(-Camera.size * screenRatio, Camera.size * screenRatio,
            -Camera.size, Camera.size,
            Camera.near, -Camera.far)

    Camera.applyTransformation()
    EventManager.castRender()
    glutSwapBuffers()


def __PhysicsUpdate():
    pass


def __LateFrameUpdate():
    EventManager.castLateUpdate()
    pass


start()
