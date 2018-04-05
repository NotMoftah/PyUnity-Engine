"""
    This is the Engine module.

    -- Author : AbdElAziz Mofath
    -- Date: 5th of April 2018 at 12:10 AM
"""

import UserAssets.Scripts
import OpenGL.GL
import os

__world_id_counter = 1000
__script_module = {}

__start = {}
__render = {}
__update = {}
__late_update = {}
__dead_scripts = []


def loadScripts():
    scriptsPath = os.path.dirname(UserAssets.Scripts.__file__)
    scripts = os.listdir(scriptsPath)

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


def __SendMeggage(script_id, method_name, *args):
    global __script_module

    if script_id in __script_module:
        if hasattr(__script_module[script_id], method_name):
            method = getattr(__script_module[script_id], method_name)
            if len(args) > 0:
                method(*args)
            else:
                method()


def __DestroyScript(script_id):
    global __dead_scripts

    if not (script_id in __dead_scripts):
        __dead_scripts.append(script_id)


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
    # first we sort the objects based on the distance from the camera.
    list_of_rendering = [__script_module[x] for x in __script_module if __render[x]]

    def sortingKey(gameObject):
        if hasattr(gameObject, 'transform') is True:
            return gameObject.transform.position.z
        return 0

    list_of_rendering.sort(key=sortingKey, reverse=True)

    # then we render
    for obj in list_of_rendering:
        OpenGL.GL.glPushMatrix()
        obj.Render()
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


def collectGarbage():
    global __dead_scripts, __start, __render, __update, __late_update
    if len(__dead_scripts) > 0:
        for obj in __dead_scripts:
            del __dead_scripts[obj]

            if obj in __start:
                del __start[obj]

            if obj in __render:
                del __render[obj]

            if obj in __update:
                del __update[obj]

            if obj in __late_update:
                del __late_update[obj]
