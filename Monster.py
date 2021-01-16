from Spec import Spec


class Monster(Spec):

    def __init__(self, name, health, geo_x, geo_y, power, speed, money, ability):
        super().__init__(name, health, geo_x, geo_y, power, speed, money, ability)

    def getHit(self, damage):
        print("Монстр получает урон:\t", damage)
        pass

    def damage_from_monster(self):
        print("Вы получаете урон:\t", self.power)
