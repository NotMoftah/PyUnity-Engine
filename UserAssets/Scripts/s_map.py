from UserAssets.Scripts.basics import *
import Kernel.EventManager

maze = SpriteRenderer('maze.png')
transform0 = Transform2D()


transform0.scale = Vector3(5, 5, 5)


def Render():
    transform0.applyTransformation()

    maze.render()
