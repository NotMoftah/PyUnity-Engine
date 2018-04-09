from UserAssets.Scripts.basics import *

car = SpriteRenderer('car.png')
transform = Transform2D()


def Start():
    global player, follow, speed
    speed = 10.
    follow = False
    player = get_script('player')
    transform.position.z = -1
    transform.scale = Vector3(0.1, 0.1, 0.1)


def Render():
    global follow

    transform.applyTransformation()

    if follow:
        car.render(color=Vector3(1, 0, 0))
    else:
        car.render()


def Update():
    global follow, speed

    if Input.KeyDown('0'):
        follow = not follow

    if follow:
        liner_speed = (player.transform.position - transform.position).normalized()
        transform.position += liner_speed * Time.deltaTime * 3
        transform.lookAtPoint(player.transform.position)

    else:
        if Input.KeyHold('8'):
            transform.position += Vector3(0, 1, 0) * Time.deltaTime * speed

        if Input.KeyHold('5'):
            transform.position -= Vector3(0, 1, 0) * Time.deltaTime * speed

        if Input.KeyHold('6'):
            transform.position += Vector3(1, 0, 0) * Time.deltaTime * speed

        if Input.KeyHold('4'):
            transform.position -= Vector3(1, 0, 0) * Time.deltaTime * speed

        transform.lookAtPoint(Camera.screenToWorld(Input.MousePosition()))

        print(speed)


def set_speed(val):
    global speed
    speed = val


