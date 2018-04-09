"""
    This is the Engine module.

    -- Author : AbdElAziz Mofath
    -- Date: 5th of April 2018 at 12:10 AM
"""

import UserAssets.Scripts
import importlib.util
import Kernel.Time
import OpenGL.GL
import gc
import os

__world_id_counter = 1000
__script_module = {}

__start = {}
__render = {}
__update = {}
__late_update = {}

__born_scripts = []
__dead_scripts = []

gc_time = 0.0


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


def __InstantiateScript(prefab_name):
    global __born_scripts
    prefab_module, prefab_id = __LoadPrefab('UserAssets.Prefabs.' + prefab_name)
    __born_scripts.append((prefab_module, prefab_id))

    if hasattr(prefab_module, 'Start'):
        prefab_module.Start()

    return prefab_module


def __GetScript(script_id):
    global __script_module
    if script_id in __script_module:
        return __script_module[script_id]
    return None


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
    global __dead_scripts, __start, __render, __update, __late_update, __script_module, gc_time
    if len(__dead_scripts) > 0:
        for obj in __dead_scripts:

            if obj in __start:
                del __start[obj]

            if obj in __render:
                del __render[obj]

            if obj in __update:
                del __update[obj]

            if obj in __late_update:
                del __late_update[obj]

            if obj in __script_module:
                del __script_module[obj]

        __dead_scripts = []

    if Kernel.Time.fixedTime >= gc_time + 1:
        gc_time = Kernel.Time.fixedTime
        gc.collect()


def __LoadPrefab(prefab):
    global __world_id_counter
    __world_id_counter = __world_id_counter + 1

    metaData = importlib.util.find_spec(prefab)
    ObjectModule = importlib.util.module_from_spec(metaData)
    metaData.loader.exec_module(ObjectModule)

    setattr(ObjectModule, '__id__', __world_id_counter)
    return ObjectModule, __world_id_counter


def __HookPrefab(prefabModule, prefab_id):
    __script_module[prefab_id] = prefabModule

    subscribeStart(prefab_id, hasattr(prefabModule, 'Start'))
    subscribeUpdate(prefab_id, hasattr(prefabModule, 'Update'))
    subscribeRender(prefab_id, hasattr(prefabModule, 'Render'))
    subscribeLateUpdate(prefab_id, hasattr(prefabModule, 'LateUpdate'))


def updateDictionary():
    global __born_scripts, __script_module

    if len(__born_scripts) > 0:
        for prefab_module, prefab_id in __born_scripts:
            __script_module[prefab_id] = prefab_module
            __HookPrefab(prefab_module, prefab_id)

    __born_scripts = []