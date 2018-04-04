from UserAssets.Scripts.basics import *


maze = SpriteRenderer('maze.png')
transform = Transform2D()


transform.scale = Vector3(5, 5, 5)


def Render():
    transform.applyTransformation()

    maze.render()
