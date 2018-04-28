from UserAssets.Scripts.basics import *


t = Transform2D()
s = SpriteRenderer('floor.jpg')


def Render():
    t.applyTransformation()
    s.render(mul=20)


def Update():
    t.scale = Vector3(20, 20, 1)
