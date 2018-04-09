from UserAssets.Scripts.basics import *

car = SpriteRenderer('toto.png')
transform = Transform2D()


def Start():
    global direction, startTime
    transform.position.z = -1
    direction = transform.up()
    startTime = Time.fixedTime


def Render():
    transform.applyTransformation()
    car.render()


def Update():
    global direction, startTime
    transform.position += transform.up() * 5 * Time.deltaTime

    if Time.fixedTime >= startTime + 5:
        destroy_script(__id__)


def set_speed(pos, up):
    transform.position = pos
    transform.lookAtPoint(pos + up)


