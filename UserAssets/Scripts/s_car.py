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
        transform.position += speed * Time.deltaTime * 3
        transform.lookAtPoint(player.transform.position)

    else:
        # if Input.KeyHold('8'):
        #     transform.position += transform.up() * Time.deltaTime * 10
        #
        # if Input.KeyHold('5'):
        #     transform.position -= transform.up() * Time.deltaTime * 10
        #
        # if Input.KeyHold('6'):
        #     transform.rotation.z -= 180 * Time.deltaTime
        #
        # if Input.KeyHold('4'):
        #     transform.rotation.z += 180 * Time.deltaTime

        if Input.KeyHold('8'):
            transform.position += Vector3(0, 1, 0) * Time.deltaTime * 10

        if Input.KeyHold('5'):
            transform.position -= Vector3(0, 1, 0) * Time.deltaTime * 10

        if Input.KeyHold('6'):
            transform.position += Vector3(1, 0, 0) * Time.deltaTime * 10

        if Input.KeyHold('4'):
            transform.position -= Vector3(1, 0, 0) * Time.deltaTime * 10

        transform.lookAtPoint(Camera.screenToWorld(Input.MousePosition()))

