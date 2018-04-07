"""
    This is the Utilities module.

    the Utilities has:
        Vector3: A Universal class that describe a direction in a 3d space, it also works as 3 element array.

        Transform2D: A Universal class that describe the orientation of a game object in a 2d space.

    -- Author : AbdElAziz Mofath
    -- Date: 4th of April 2018 at 7:40 PM
"""
import os
import math
import pygame
import random
from OpenGL.GL import *
from Kernel import Time
from UserAssets import Drawings
from Kernel.EventManager import __EnableScript, __DisableScript, __DestroyScript,\
    __SendMeggage, __InstantiateScript, __GetScript


class Vector3:
    def __str__(self):
        return "{" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "}"

    def __init__(self, x, y, z):
        """

        :param x: x value
        :param y: y value
        :param z: z value
        """
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        newVec = Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z)
        return newVec

    def __sub__(self, other):
        newVec = Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z)
        return newVec

    def __mul__(self, i):
        return Vector3(self.x * i, self.y * i, self.z * i)

    def __truediv__(self, i):
        return Vector3(self.x / i, self.y / i, self.z / i)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y and self.z != other.z

    def setValues(self, x, y, z):
        """
        set the values of the vector

        :param x: x
        :param y: y
        :param z: z
        """
        self.x = x
        self.y = y
        self.z = z

    def normalized(self, ):
        """
        This function makes a copy of the current vector, Then normalize it so that its length be exactly one.

        * Doesnt affect the current vector values.

        :return: Vector3
        """
        length = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        if length == 0:
            return Vector3(0, 0, 0)
        else:
            Nx = self.x / length
            Ny = self.y / length
            Nz = self.z / length
            return Vector3(Nx, Ny, Nz)

    def normalize(self, ):
        """
            Normalize the current vector so that its length be exactly one.

            * Change the current values of the vector
        """
        length = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        if length == 0:
            self.x, self.y, self.z = 0, 0, 0
        else:
            self.x = self.x / length
            self.y = self.y / length
            self.z = self.z / length

    def cross(self, vec):
        """
        the cross product of multiplying the current vector by vector vec
        * Doesnt affect the current vector values.

        :param vec: vector b in the notation cross = a * b
        :return: Vector3
        """
        newVec = Vector3(self.y * vec.z - self.z * vec.y,
                         self.z * vec.x - self.x * vec.z,
                         self.x * vec.y - self.y * vec.x)
        return newVec

    def magnitude(self, ):
        """
        The length of the vector.

        :return: float: the length of the vector
        """
        length = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return length


class Transform2D:
    def __init__(self, ):
        self.position = Vector3(0, 0, 0)
        self.rotation = Vector3(0, 0, 0)
        self.scale = Vector3(1, 1, 1)

        self.__up = Vector3(0, 1, 0)
        self.__right = Vector3(1, 0, 0)

    def applyTransformation(self):
        """
            Apply the current transformation to the game object
        """
        glTranslatef(self.position.x, self.position.y, self.position.z)

        glRotatef(self.rotation.x, 1, 0, 0)
        glRotatef(self.rotation.y, 0, 1, 0)
        glRotatef(self.rotation.z, 0, 0, 1)

        glScalef(self.scale.x, self.scale.y, self.scale.z)

    def up(self):
        """
        the normalized up direction of the game object
        :return: Vector3
        """

        ang = math.radians(self.rotation.z)
        return Vector3(-math.sin(ang), math.cos(ang), 0)

    def right(self):
        """
        the normalized right direction of the game object
        :return: Vector3
        """

        ang = math.radians(self.rotation.z)
        return Vector3(math.cos(ang), math.sin(ang), 0)

    def lookAtPoint(self, vec):
        direction = (vec - self.position).normalized()
        self.rotation.z = math.degrees(math.atan2(direction.y, direction.x)) - 90


class SpriteRenderer:
    def __init__(self, sprite_name):
        """
        :param sprite_name: the name of the sprite
        """
        drawings_path = os.path.dirname(Drawings.__file__)
        self.sprite_path = drawings_path + '\\' + sprite_name

        self.sprite = pygame.image.load(self.sprite_path)
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()

        self.sprite_data = pygame.image.tostring(self.sprite, "RGBA", 1)
        self.sprite_text_id = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.sprite_text_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.sprite_width, self.sprite_height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, self.sprite_data)

    def render(self, mul=1, brightness=1):

        """
            render the sprite at the origin.
        """

        glEnable(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, self.sprite_text_id)

        rx = self.sprite_width / 100
        ry = self.sprite_height / 100

        glColor3f(1 * brightness, 1 * brightness, 1 * brightness)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-1 * rx, -1 * ry, 0)

        glTexCoord2f(0, mul)
        glVertex3f(-1 * rx, 1 * ry, 0)

        glTexCoord2f(mul, mul)
        glVertex3f(1 * rx, 1 * ry, 0)

        glTexCoord2f(mul, 0)
        glVertex3f(1 * rx, -1 * ry, 0)
        glEnd()

        glDisable(GL_TEXTURE_2D)


class Animation:
    def __init__(self, sprite_name, size, speed):
        """
        :param sprite_name: the name of the sprite
        """
        self.size, self.speed = size, speed
        self.frame_counter, self.start = 0, 0
        drawings_path = os.path.dirname(Drawings.__file__)
        self.sprite_path = drawings_path + '\\' + sprite_name

        self.sprite = pygame.image.load(self.sprite_path)
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()

        self.sprite_data = pygame.image.tostring(self.sprite, "RGBA", 1)
        self.sprite_text_id = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.sprite_text_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.sprite_width, self.sprite_height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, self.sprite_data)

    def __frame_bounds(self, animate):
        step = 1 / self.size

        if animate:
            self.frame_counter += self.speed * Time.deltaTime
            if self.frame_counter >= step:
                self.start += step * int(self.frame_counter / step)
                self.frame_counter = 0

            return self.start, self.start + step

        return 0, step

    def render(self, animate=True, brightness=1):

        """
            render the sprite at the origin.
        """

        glEnable(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, self.sprite_text_id)

        rx = self.sprite_width / (100 * self.size)
        ry = self.sprite_height / 100
        tx, ty = self.__frame_bounds(animate)

        glColor3f(1 * brightness, 1 * brightness, 1 * brightness)

        glBegin(GL_QUADS)
        glTexCoord2f(tx, 0)
        glVertex3f(-rx, -ry, 0)

        glTexCoord2f(ty, 0)
        glVertex3f(rx, -ry, 0)

        glTexCoord2f(ty, 1)
        glVertex3f(rx, ry, 0)

        glTexCoord2f(tx, 1)
        glVertex3f(-rx, ry, 0)
        glEnd()

        glDisable(GL_TEXTURE_2D)


class ParticleSystem:
    def __init__(self, sprite_name, num):
        drawings_path = os.path.dirname(Drawings.__file__)
        self.sprite_path = drawings_path + '\\' + sprite_name

        self.sprite = pygame.image.load(self.sprite_path)
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()

        self.sprite_data = pygame.image.tostring(self.sprite, "RGBA", 1)
        self.sprite_text_id = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.sprite_text_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.sprite_width, self.sprite_height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, self.sprite_data)

        self.alive = False

        self.speed_list = [random.random() for _ in range(num)]
        self.pos_list = [(0, 0) for _ in range(num)]

    def activate(self):
        self.alive = True

    def render(self):
        if self.alive is True:
            pass


def send_message(script_id, method, *args):
    __SendMeggage(script_id, method, *args)


def enable_script(script_id):
    __EnableScript(script_id)


def disable_script(script_id):
    __DisableScript(script_id)


def destroy_script(script_id):
    __DestroyScript(script_id)


def instantiate_script(script_name):
    __InstantiateScript(script_name)


def get_script(script_id):
    return __GetScript(script_id)
