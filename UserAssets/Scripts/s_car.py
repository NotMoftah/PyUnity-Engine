from UserAssets.Scripts.basics import *

car = SpriteRenderer('car.png')
transform = Transform2D()


def Start():
    global player, follow
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
    global follow

    if Input.KeyDown('0'):
        follow = not follow

    if follow:
        speed = (player.transform.position - transform.position).normalized()
        transform.position += speed * Time.deltaTime * 15
        transform.lookAtPoint(player.transform.position)

    else:

        if Input.MouseKeyHoldDown(0):
            fire = instantiate_script('fire')
            fire.set_speed(transform.position, transform.up())

        if Input.KeyHold('8'):
            transform.position += Vector3(0, 1, 0) * Time.deltaTime * 10

        if Input.KeyHold('5'):
            transform.position -= Vector3(0, 1, 0) * Time.deltaTime * 10

        if Input.KeyHold('6'):
            transform.position += Vector3(1, 0, 0) * Time.deltaTime * 10

        if Input.KeyHold('4'):
            transform.position -= Vector3(1, 0, 0) * Time.deltaTime * 10

        transform.lookAtPoint(Camera.screenToWorld(Input.MousePosition()))

    Camera.position = transform.position


