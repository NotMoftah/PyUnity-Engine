from UserAssets.Scripts.basics import *
transform = Transform2D()


def Render():
    # must add
    transform.applyTransformation()

    # your render code here
    glColor3f(0, 0, 0)
    glutWireCube(2)


def Update():
    if Input.KeyDown('z'):
        transform.rotation.z += 5

    if Input.KeyDown('x'):
        transform.rotation.x += 5
