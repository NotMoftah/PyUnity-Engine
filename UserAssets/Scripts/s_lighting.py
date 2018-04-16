from UserAssets.Scripts.basics import *

transform = Transform2D()
light = SpriteRenderer('light2.png')
__id__ = 'light'


def Start():
    transform.scale = Vector3(5, 5, 5)


def Render():
    transform.applyTransformation()
    glBlendFunc(GL_SRC_ALPHA, GL_ONE)
    light.render(brightness=.5, color=Vector3(0, 1, 0))
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
