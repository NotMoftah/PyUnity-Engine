from UserAssets.Scripts.basics import *

car = SpriteRenderer('toto.png')
transform = Transform2D()


def Start():
    global startTime, rect
    transform.position.z = -1
    startTime = Time.fixedTime
    rect = StaticRectCollider(__id__, (0, 0, 1, 1), 'hello')


def Render():
    transform.applyTransformation()
    car.render()


def Update():
    global startTime
    transform.position += transform.up * 30 * Time.deltaTime

    if Time.fixedTime >= startTime + 5:
        destroy_script(__id__)


