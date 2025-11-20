import time 
import random 
import json 
import random 
class CapsulePresenceSensorDescriptor:
    def _init_ (self) :
        self . value = 0
        self . timestamp = 0
        self . check_capsule_presence ()
    def check_capsul_presence(self):
        self . value = random{True, False}
        self . timestamp = int( time . time ())
    def to_json (self):
        return json . dumps ( self , default = lambda o : o. __dict__ )
