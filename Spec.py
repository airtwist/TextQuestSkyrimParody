from abc import ABC, abstractmethod


class Spec(ABC):
    @abstractmethod
    def __init__(self, name, health, geo_x, geo_y, power, speed, money, ability):
        self.name = name
        self.health = health
        self.geo_x = geo_x
        self.geo_y = geo_y
        self.power = power
        self.speed = speed
        self.money = money
        self.ability = ability
    @abstractmethod
    def getHit(self, damage):
        self.health = self.health - damage



