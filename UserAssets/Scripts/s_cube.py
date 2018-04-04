from UserAssets.Scripts.basics import *


sprite = SpriteRenderer('texture.jpg')
transform = Transform2D()


def Render():
    # must add
    transform.applyTransformation()

    # your render code here
    sprite.render()


def Update():
    if Input.KeyDown('a'):
        transform.position.x -= 1

    if Input.KeyDown('d'):
        transform.position.x += 1
