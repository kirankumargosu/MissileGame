from missile import Missile
from enemy import  Enemy

class WarFactory:
    __instance = None

    @staticmethod
    def getInstance():
        if WarFactory.__instance is None:
            __instance = WarFactory()
        return WarFactory.__instance

    def __init__(self):
        if WarFactory.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            WarFactory.__instance = self
            print("WarFactory Initialized")

    @staticmethod
    def createWarItem(typ):
        targetClass = typ.capitalize()
        return globals()[targetClass]()
