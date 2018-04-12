from UserAssets.Scripts.basics import *

car = SpriteRenderer('toto.png')
transform = Transform2D()
collider = BoxCollider2D(2, 2, transform, __id__, collider_tag='bullet')


def Start():
    global startTime
    transform.position.z = -1
    startTime = Time.fixedTime


def Render():
    collider.render()
    transform.applyTransformation()
    car.render()


def Update():
    global startTime
    transform.position += transform.up * 30 * Time.deltaTime

    if Time.fixedTime >= startTime + 1:
        destroy_script(__id__)


