from UserAssets.Scripts.basics import *
import random

transform = Transform2D()
light = SpriteRenderer('light2.png')


def Start():
    transform.position = Vector3(+2.5, 0, -1)
    transform.scale = Vector3(3, 3, 3)


def Render():
    transform.applyTransformation()
    glBlendFunc(GL_SRC_ALPHA, GL_ONE)
    light.render(brightness=.5)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
