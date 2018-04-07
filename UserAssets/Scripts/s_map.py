from UserAssets.Scripts.basics import *

maze = SpriteRenderer('floor.png')
transform0 = Transform2D()


transform0.scale = Vector3(5, 5, 5)


# def Start():
#     disable_script(__id__)


def Render():
    transform0.applyTransformation()

    maze.render(mul=5, brightness=.7)


def Update():
    if Input.KeyHold('+'):
        Camera.position.y += 5 * Time.deltaTime

    if Input.KeyHold('-'):
        Camera.position.y -= 5 * Time.deltaTime
