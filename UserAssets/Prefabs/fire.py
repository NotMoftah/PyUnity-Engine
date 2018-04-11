from UserAssets.Scripts.basics import *

car = SpriteRenderer('toto.png')
transform = Transform2D()


def Start():
    global startTime
    transform.position.z = -1
    startTime = Time.fixedTime


def Render():
    transform.applyTransformation()
    car.render()


def Update():
    global startTime
    transform.position += transform.up * 30 * Time.deltaTime

    if Time.fixedTime >= startTime + 5:
        destroy_script(__id__)


