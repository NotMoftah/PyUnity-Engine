"""
    This is the Utilities module.

    the Utilities has:
        Vector3: A Universal class that describe a direction in a 3d space, it also works as 3 element array.

        Transform2D: A Universal class that describe the orientation of a game object in a 2d space.

    -- Author : AbdElAziz Mofath
    -- Date: 4th of April 2018 at 7:40 PM
"""
import math
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from UserAssets import Drawings
from Kernel import Time, Physics
from Kernel.DataBase import get_variable, set_variable
from Kernel.EventManager import __EnableScript, __DisableScript, __DestroyScript,\
    __SendMeggage, __InstantiateScript, __GetScript, __CastEvent


class Vector3:
    def __str__(self,):
        return "{" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "}"

    def __init__(self, x=0., y=0., z=0.):
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
        return not (self.x == other.x or self.y == other.y or self.z == other.z)

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

    def dot(self, vec):
        """
        the dot product of multiplying the current vector by vector vec
        * Doesnt affect the current vector values.

        :param vec: vector b in the notation dot = a . b
        :return: Vector3
        """
        val = self.x * vec.x + self.y * vec.y + self.z * vec.z
        return val

    def magnitude(self, ):
        """
        :return: float: the length of the vector
        """
        length = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return length

    def squareMagnitude(self, ):
        """
        :return: float: the Squared length of the vector
        """
        length = self.x * self.x + self.y * self.y + self.z * self.z
        return length

    @staticmethod
    def ones(scale=1):
        return Vector3(scale, scale, scale)

    @staticmethod
    def zeros():
        return Vector3(0, 0, 0)

    @staticmethod
    def lerp(vec_a, vec_b, t):
        return vec_a + (vec_b - vec_a) * t


class Transform2D:
    def __init__(self, ):
        self.__rotation = Vector3(0, 0, 0)
        self.position = Vector3(0, 0, 0)
        self.scale = Vector3(1, 1, 1)

        self.__up = Vector3(0, 1, 0)
        self.__right = Vector3(1, 0, 0)
        self.__update_axis = True

    def applyTransformation(self):
        """
            Apply the current transformation to the game object
        """
        glTranslatef(self.position.x, self.position.y, self.position.z)

        glRotatef(self.__rotation.x, 1, 0, 0)
        glRotatef(self.__rotation.y, 0, 1, 0)
        glRotatef(self.__rotation.z, 0, 0, 1)

        glScalef(self.scale.x, self.scale.y, self.scale.z)

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, vec):
        self.__rotation = vec
        self.__update_axis = True

    @property
    def up(self):
        """
        the normalized up direction of the game object
        :return: Vector3
        """
        if self.__update_axis:
            self.__update_axis = False
            ang = math.radians(self.rotation.z)
            self.__up = Vector3(-math.sin(ang), math.cos(ang), 0)
        return self.__up

    @property
    def right(self):
        """
        the normalized right direction of the game object
        :return: Vector3
        """
        if self.__update_axis:
            self.__update_axis = False
            ang = math.radians(self.rotation.z)
            self.__right = Vector3(math.cos(ang), math.sin(ang), 0)
        return self.__right

    @up.setter
    def up(self, vec):
        self.__rotation.z = math.degrees(math.atan2(vec.y, vec.x)) - 90
        self.__update_axis = True

    @right.setter
    def right(self, vec):
        self.__rotation.z = math.degrees(math.atan2(vec.y, vec.x))
        self.__update_axis = True

    def lookAtPoint(self, vec):
        direction = (vec - self.position).normalized()
        self.__rotation.z = math.degrees(math.atan2(direction.y, direction.x)) - 90
        self.__update_axis = True


class SpriteRenderer:
    def __init__(self, sprite_name, smooth=True):
        """
        :param sprite_name: the name of the sprite
        """
        drawings_path = os.path.dirname(Drawings.__file__)
        sprite_path = drawings_path + '\\' + sprite_name

        self._sprite = pygame.image.load(sprite_path)
        self._sprite_width = self._sprite.get_width()
        self._sprite_height = self._sprite.get_height()

        self._sprite_data = pygame.image.tostring(self._sprite, "RGBA", 1)
        self._sprite_text_id = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self._sprite_text_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR if smooth else GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR if smooth else GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self._sprite_width, self._sprite_height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, self._sprite_data)

        del self._sprite, self._sprite_data

    def __del__(self):
        glDeleteTextures(1, self._sprite_text_id)

    @property
    def size(self):
        """
        :return: the width and the height of the sprite
        """
        return self._sprite_width / 100, self._sprite_height / 100

    def render(self, mul=1, brightness=1, color=Vector3(1, 1, 1)):
        """
            render the sprite at the origin.
        """

        glEnable(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, self._sprite_text_id)

        rx = self._sprite_width / 100
        ry = self._sprite_height / 100

        glColor3f(color.x * brightness, color.y * brightness, color.z * brightness)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-rx, -ry, 0)

        glTexCoord2f(0, mul)
        glVertex3f(-rx, +ry, 0)

        glTexCoord2f(mul, mul)
        glVertex3f(+rx, +ry, 0)

        glTexCoord2f(mul, 0)
        glVertex3f(+rx, -ry, 0)
        glEnd()

        glDisable(GL_TEXTURE_2D)


class Animation:
    def __init__(self, sprite_name, size, speed, smooth=True):
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
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR if smooth else GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR if smooth else GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.sprite_width, self.sprite_height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, self.sprite_data)

        del self.sprite, self.sprite_data

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


class PlainText:
    def __init__(self, text, line_width=1):
        self.text = text
        self.line_width = line_width

    def render(self, color=Vector3.zeros()):
        glScale(0.001, 0.001, 0.001)
        glLineWidth(self.line_width)
        glColor3f(color.x, color.y, color.z)

        for c in self.text.encode():
            glutStrokeCharacter(GLUT_STROKE_ROMAN, c)


class BoxCollider2D:
    def __init__(self, width, height, transform, collider_id, collider_tag='box'):
        self.width = width
        self.height = height
        self.transform = transform
        self.collider_id = collider_id
        self.collider_tag = collider_tag

        self.method = None
        Physics.addBox(self)

    def render(self):
        x = self.width / 2
        y = self.height / 2

        glScale(1 / self.transform.scale.x,
                1 / self.transform.scale.y,
                1 / self.transform.scale.z)

        glColor3f(1, 1, 1)
        glLineWidth(1)

        glBegin(GL_LINE_LOOP)
        glVertex3f(-x, -y, 0)
        glVertex3f(-x, +y, 0)
        glVertex3f(+x, +y, 0)
        glVertex3f(+x, -y, 0)
        glEnd()

    def on_collision_trigger(self, method):
        self.method = method

    def trigger_hit_event(self, hit_id, hit_tag):
        if self.method is not None:
            self.method(hit_id, hit_tag)

    def start_pos_x(self):
        return self.transform.position.x - (self.width / 2)

    def start_pos_y(self):
        return self.transform.position.y - (self.height / 2)

    def end_pos_x(self):
        return self.transform.position.x + (self.width / 2)

    def end_pos_y(self):
        return self.transform.position.y + (self.height / 2)

    def is_collision(self, box):
        x1 = self.start_pos_x() > box.end_pos_x()
        x2 = self.end_pos_x() < box.start_pos_x()

        y1 = self.start_pos_y() > box.end_pos_y()
        y2 = self.end_pos_y() < box.start_pos_y()

        return not (x1 or x2 or y1 or y2)


def castEvent(event_name, *args):
    __CastEvent(event_name, *args)


def send_message(script_id, method, *args):
    __SendMeggage(script_id, method, *args)


def enable_script(script_id):
    __EnableScript(script_id)


def disable_script(script_id):
    __DisableScript(script_id)


def destroy_script(script_id):
    __DestroyScript(script_id)


def instantiate_script(script_name):
    return __InstantiateScript(script_name)


def get_script(script_id):
    return __GetScript(script_id)


def lerp(vec_a, vec_b, t):
    return vec_a + (vec_b - vec_a) * t
