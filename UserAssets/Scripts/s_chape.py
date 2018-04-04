from UserAssets.Scripts.basics import *


sprite = SpriteRenderer('texture.png')
transform = Transform2D()

Camera.clearColor = Vector3(0.5, 0.5, 0.5)


def Render():
    # must add
    transform.applyTransformation()

    # your render code here
    sprite.render()


def Update():
    transform.scale = Vector3(0.5, 0.5, 0.5)

    if Input.KeyDown('+'):
        transform.position.y += 1

    if Input.KeyDown('-'):
        transform.position.y -= 1
