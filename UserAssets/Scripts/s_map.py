from UserAssets.Scripts.basics import *

maze = SpriteRenderer('floor.png')
transform = Transform2D()


def Start():
    global offset_x, offset_y
    offset_x, offset_y = maze.size()


def Render():
    transform.applyTransformation()

    maze.render()

    maze.render(x=offset_x * 2)
    maze.render(y=offset_y * 2)
    maze.render(x=offset_x * 2, y=offset_y * 2)


def Update():
    global offset_x, offset_y
    cameraPos = Camera.position
    sign = lambda a: 1 if a > 0 else -1

    if cameraPos.x >= transform.position.x + 2 * abs(offset_x):
        transform.position.x += 2 * abs(offset_x)
    elif cameraPos.x <= transform.position.x - 2 * abs(offset_x):
        transform.position.x -= 2 * abs(offset_x)

    if cameraPos.y >= transform.position.y + 2 * abs(offset_y):
        transform.position.y += 2 * abs(offset_y)
    elif cameraPos.y <= transform.position.y - 2 * abs(offset_y):
        transform.position.y -= 2 * abs(offset_y)

    offset_x = abs(offset_x) * sign(Camera.position.x - transform.position.x)
    offset_y = abs(offset_y) * sign(Camera.position.y - transform.position.y)