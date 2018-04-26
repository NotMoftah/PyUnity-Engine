# Math
import math
import random
import numpy as np

# OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Kernel
from Kernel import Input, Time, Camera, Physics

# Utilities
from Kernel.Utilities import *


'''
    All the functions that the engine can process:
    
    - Start():
        * It'll be called once and only once open the game start.
                
    - Update():
        * It'll be called evert frame at the very beginning of it.
        * Use it to do anything and update anything you'd like.
        
    - Render():
        * It'll be called every frame after the update.
        * Use it to only render and draw objects.
        * Don't forget to apply transformations.
    
    - LateUpdate():
        * It'll be called evert frame at the very ending of it.
        * Use it to do anything and update anything you'd like.

    - Events(event_name, *args):
        * It'll be called only when some other script call the cast_event().
        * the arguments are must. never forget them.
        
        
    Important scripting calls:
    
    - castEvent(event_name, *args):
        * use it whenever you like to cast an event to all the scripts in the engine
        
    - send_message(script_id, method, *args):
        * use it to call a private method in a script using it's id.
        
    - enable_script(script_id):
        * as it says
        
    - disable_script(script_id):
        * as it says
        
    - destroy_script(script_id):
        * as it says
        
    - instantiate_script(script_name):
        * upload the script from the prefab and run it like normal scripts.
        * it return the script as class and you can edit and access it freely
        
    - get_script(script_id):
        * return the script as a class that you can access freely.
            
'''