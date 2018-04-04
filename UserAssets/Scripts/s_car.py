from UserAssets.Scripts.basics import *


sprite = SpriteRenderer('car.png')
transform = Transform2D()

Camera.clearColor = Vector3(0.5, 0.5, 0.5)


def Render():
    # must add
    transform.applyTransformation()

    # your render code here

    sprite.render()

def Update():
    transform.scale = Vector3(0.25, 0.25, 0.25)
    transform.position.z = -2

    if Input.KeyHold('w'):
        transform.position += transform.up() * Time.deltaTime * 5

    if Input.KeyHold('s'):
        transform.position -= transform.up() * Time.deltaTime * 5

    if Input.KeyHold('d'):
        transform.rotation.z -= 180 * Time.deltaTime

    if Input.KeyHold('a'):
        transform.rotation.z += 180 * Time.deltaTime
