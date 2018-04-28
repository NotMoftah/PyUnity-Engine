from UserAssets.Scripts.basics import *

transform = Transform2D()
image = SpriteRenderer('start_button.png')


def Start():
    global close
    close = False
    transform.position.y = 3


def Render():
    global close

    transform.applyTransformation()
    transform.scale = Vector3(0.1, 0.1, 0.1)

    if close:
        image.render(brightness=.5)
    else:
        image.render()


def Update():
    global close

    world_mouse_position = Camera.screenToWorld(Input.MousePosition())
    delta_pos = world_mouse_position - transform.position

    if delta_pos.magnitude() < 2.5:
        close = True
    else:
        close = False