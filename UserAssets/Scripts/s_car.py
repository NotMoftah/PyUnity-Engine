from UserAssets.Scripts.basics import *

transform = Transform2D()
car = SpriteRenderer('car.png')
collider = BoxCollider2D(2, 2, transform, 'car')


def Start():
    global player, follow, light
    follow = False
    player = get_script('player')
    light = get_script('light')
    transform.position.z = -1
    transform.scale = Vector3(0.1, 0.1, 0.1)
    Camera.size = 8
    collider.on_collision_trigger(oncoll)


def Render():
    global follow
    collider.render()

    transform.applyTransformation()

    if follow:
        car.render(color=Vector3(1, 0, 0))
    else:
        car.render()


def Update():
    global follow, player

    if Input.KeyDown('0'):
        follow = not follow

    if follow:
        speed = (player.transform.position - transform.position).normalized()
        transform.position += speed * Time.deltaTime * 15
        transform.lookAtPoint(player.transform.position)

    else:

        if Input.MouseKeyDown(0):
            bullet = instantiate_script('fire')
            bullet.transform.position = transform.position
            bullet.transform.up = transform.up

        if Input.KeyHold('8'):
            transform.position += Vector3(0, 1, 0) * Time.deltaTime * 10

        if Input.KeyHold('5'):
            transform.position -= Vector3(0, 1, 0) * Time.deltaTime * 10

        if Input.KeyHold('6'):
            transform.position += Vector3(1, 0, 0) * Time.deltaTime * 10

        if Input.KeyHold('4'):
            transform.position -= Vector3(1, 0, 0) * Time.deltaTime * 10

        transform.lookAtPoint(Camera.screenToWorld(Input.MousePosition()))

    Camera.position = Vector3.lerp(Camera.position, transform.position, 2 * Time.deltaTime)
    Camera.position.z = -10
    light.transform.position = transform.position + Vector3(0, 0, +0.01)


def oncoll(hits):
    global follow
    for hit in hits:
        if hit == 'player':
            follow = False
