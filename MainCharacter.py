from Spec import Spec


class Hero(Spec):



    def __init__(self, name, health, geo_x, geo_y, power, speed, money, ability):
        super().__init__(name, health, geo_x, geo_y, power, speed, money, ability)

    def getHit(self, damage):
        print("Герой получае урон: \t ", damage)
        pass

    def attack(self):
        return self.power

    def up(self):
        print("Ваш персонаж сделал шаг вперед\n")
        self.geo_y = self.geo_y + self.speed

    def right(self):
        print("Ваш персонаж сделал шаг вправо\n")
        self.geo_x = self.geo_x + self.speed

    def down(self):
        print("Ваш персонаж сделал шаг назад\n")
        self.geo_y = self.geo_y - self.speed

    def left(self):
        print("Ваш персонаж сделал шаг налево\n")
        self.geo_x = self.geo_x - self.speed
