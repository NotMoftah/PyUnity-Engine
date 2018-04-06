from UserAssets.Scripts.basics import *

sprite = SpriteRenderer('car.png')
glow = SpriteRenderer('glow.png')

transform = Transform2D()


def Render():
    # must add
    transform.applyTransformation()

    # your render code here
    sprite.render()

    glTranslate(0, 20, 0)
    glScale(10, 10, 10)

    glow.render()


def Update():
    transform.scale = Vector3(0.25, 0.25, 0.25)
    transform.position.z = -1

    if Input.KeyHold('w'):
        transform.position += Vector3(0, 1, 0) * Time.deltaTime * 4

    if Input.KeyHold('s'):
        transform.position -= Vector3(0, 1, 0) * Time.deltaTime * 4

    if Input.KeyHold('d'):
        transform.position += Vector3(1, 0, 0) * Time.deltaTime * 4

    if Input.KeyHold('a'):
        transform.position -= Vector3(1, 0, 0) * Time.deltaTime * 4

    transform.lookAtPoint(Camera.screenToWorld(Input.MousePosition()))
    Camera.position = transform.position

