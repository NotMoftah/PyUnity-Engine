"""
    This is the Engine module.

    -- Author : AbdElAziz Mofath
    -- Date: 5th of April 2018 at 12:10 AM
"""

import UserAssets.Scripts
from os import listdir
import OpenGL.GL
import os.path

__world_id_counter = 1000
__script_module = {}

__start = {}
__render = {}
__update = {}
__late_update = {}


def loadScripts():
    scriptsPath = os.path.dirname(UserAssets.Scripts.__file__)
    scripts = listdir(scriptsPath)

    for script in scripts:
        if script[:2] == 's_':
            __HookMethods('UserAssets.Scripts.' + script[:-3])


def __HookMethods(script):
    global __world_id_counter, __script_module
    __world_id_counter = __world_id_counter + 1
    ObjectModule = __import__(script, globals(), locals(), ['object'])

    if hasattr(ObjectModule, '__id__'):
        current_id = ObjectModule.__id__
    else:
        setattr(ObjectModule, '__id__', __world_id_counter)
        current_id = __world_id_counter

    __script_module[current_id] = ObjectModule

    subscribeStart(current_id, hasattr(ObjectModule, 'Start'))
    subscribeUpdate(current_id, hasattr(ObjectModule, 'Update'))
    subscribeRender(current_id, hasattr(ObjectModule, 'Render'))
    subscribeLateUpdate(current_id, hasattr(ObjectModule, 'LateUpdate'))

    return ObjectModule


def __DisableScript(script_id):
    global __start, __render, __update, __late_update

    if script_id in __start:
        __start[script_id] = False

    if script_id in __render:
        __render[script_id] = False

    if script_id in __update:
        __update[script_id] = False

    if script_id in __late_update:
        __late_update[script_id] = False


def __EnableScript(script_id):
    global __script_module

    subscribeStart(script_id, hasattr(__script_module[script_id], 'Start'))
    subscribeUpdate(script_id, hasattr(__script_module[script_id], 'Update'))
    subscribeRender(script_id, hasattr(__script_module[script_id], 'Render'))
    subscribeLateUpdate(script_id, hasattr(__script_module[script_id], 'LateUpdate'))

    print('DONE')


def __SendMeggage(script_id, method_name, *args):
    global __script_module

    if script_id in __script_module:
        if hasattr(__script_module[script_id], method_name):
            method = getattr(__script_module[script_id], method_name)
            method(args)


def subscribeStart(current_id, status):
    __start[current_id] = status


def subscribeRender(current_id, status):
    __render[current_id] = status


def subscribeUpdate(current_id, status):
    __update[current_id] = status


def subscribeLateUpdate(current_id, status):
    __late_update[current_id] = status


def castStart():
    global __script_module, __start

    for subscriber in __script_module:
        if __start[subscriber]:
            __script_module[subscriber].Start()


def castRender():
    global __script_module, __render

    for subscriber in __script_module:
        if __render[subscriber]:
            OpenGL.GL.glPushMatrix()
            __script_module[subscriber].Render()
            OpenGL.GL.glPopMatrix()


def castUpdate():
    global __script_module, __update

    for subscriber in __script_module:
        if __update[subscriber]:
            __script_module[subscriber].Update()


def castLateUpdate():
    global __script_module, __late_update

    for subscriber in __script_module:
        if __late_update[subscriber]:
            __script_module[subscriber].LateUpdate()
