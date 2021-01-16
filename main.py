import random
from MainCharacter import Hero
from Monster import Monster
from Chest import Chest
from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('fus-ro-dah.mp3')

wolk = Monster("Волк, подручный Стража Леса", 100, 1, 1, 5, 0, 20, 0)
boss = Monster("Страж Леса", 500, 3, 3, 15, 0, 2000, 0)
chest1 = Chest("Таинственный сверток", 2, 2, 300)

while True:
    print("Введите имя персонажа")
    char_name = input()
    print("Выберите класс: рыцарь, копьеносец")
    char_class = input()
    if char_class == 'рыцарь':
        h1 = Hero(char_name, 100, 0, 0, 10, 1, 0, 0)
    elif char_class == 'копьеносец':
        h1 = Hero(char_name, 100, 0, 0, 10, 1, 0, 0)
    else:
        print("Произошла ошибка!")
        break
    for i in range(10):
        print("\n")
    print("\n----------------------",
          "\nВы проснулись в повозке"
          "\nЭй ты, наконец то проснулся", char_name,
          "\nТы же пытался пересь границу, верно? и попался в Имперскую засаду как и мы все, и этот вор"
          "\nВор : Гребанные бурерожденные Скайрим был в порядке пока вы не приперлись , Империя была достаточно ленива"
          "\nСлушай мы не должны быть тут, если бы не гребанные бурерожденные , я бы украл лошадь и был бы на пол "
          "пути в Хаммерфилд",
          "\nБурерожденный : ну и что теперь? То что вы", char_class, " не имеет никакого значения все равны"
                                                                      "\n----------------------"
                                                                      "\n----------------------"
                                                                      "\nВо время вашей казни напал дракон и вы "
                                                                      "сумели сбежать "
                                                                      "\n----------------------")
    break

while True:


    print("На данный момент вы находитесь на координатах \nx:",
          h1.geo_x, " y:", h1.geo_y)
    print("Куда вы пойдёте?")
    temp_coord = input()
    if temp_coord == 'a':
        h1.left()
    elif temp_coord == 'd':
        h1.right()
    elif temp_coord == 'w':
        h1.up()
    elif temp_coord == 's':
        h1.down()
    else:
        print("Произошла ошибка!")

    if (h1.geo_x == chest1.geo_x) and (h1.geo_y == chest1.geo_y):
        print("Кажется, вы что-то нашли!", chest1.name, "!", "\n вы ощущаете прирост сил"
                                                             "\n <слово силы> разблокирована")
        h1.money += chest1.money
        h1.health = 150
        h1.ability = h1.ability + 1
        print("Теперь у Вас ", h1.money, "монет.", "\nВаше здоровье выросло и составляет", h1.health)
        chest1.geo_x = 1000

    """
    Проверяем наличие монстра в клетке
    """
    if (h1.geo_x == wolk.geo_x) and (h1.geo_y == wolk.geo_y):
        break

while True:
    if wolk.health <= 0:
        print("Враг повержен! \nразделав тушу, вы находите в желудке зверя", wolk.money, "золотых.")

        h1.money += wolk.money

        input()
        break
    else:

        print("Битва с волком")
        print("Ваше здоровье: ", h1.health, "Здоровье Врага: ", wolk.health)
        wolk.damage_from_monster()
        h1.getHit(wolk.power)
        if h1.ability > 0:
            print("удар/слово силы/побег")
            temp_reaction = input()
            if temp_reaction == 'слово силы':
                crit = random.randint(0, 1)
                if crit == 1:
                    print('-----------------------------')
                    print('!!!Вы использовали Cлово силы!!!')
                    mixer.music.play()
                    print('-----------------------------')
                    h1.power += 30
                    wolk.getHit(h1.power)
                    h1.power -= 30
                else:
                    print('слово силы не удалась')
                    wolk.getHit(h1.power)
            elif temp_reaction == 'удар':
                wolk.getHit(h1.power)
            elif temp_reaction == 'побег':
                break
            else:
                print("Произошла ошибка!")
        else:
            print("удар/побег")
            temp_reaction = input()
            if temp_reaction == 'удар':
                crit = random.randint(0, 1)
                if crit == 1:
                    print('---------------------------')
                    print('!!!Вы пробили с двух рук!!!')
                    print('---------------------------')
                    h1.power += 15
                    wolk.getHit(h1.power)
                    h1.power -= 15
                else:
                    wolk.getHit(h1.power)
            elif temp_reaction == 'побег':
                break
            else:
                print("Произошла ошибка!")

while True:
    print("На данный момент вы находитесь на координатах \nx:",
          h1.geo_x, " y:", h1.geo_y)
    print("Куда вы пойдёте?")
    temp_coord = input()
    if temp_coord == 'a':
        h1.left()
    elif temp_coord == 'd':
        h1.right()
    elif temp_coord == 'w':
        h1.up()
    elif temp_coord == 's':
        h1.down()
    else:
        print("Произошла ошибка!")

    if (h1.geo_x == chest1.geo_x) and (h1.geo_y == chest1.geo_y):
        print("Вы нашли ", chest1.name, "!")
        h1.money += chest1.money
        print("Теперь у Вас ", h1.money, "монет.")
        chest1.geo_x = 1000
    """
    Проверяем наличие босса в клетке
    """
    if (h1.geo_x == boss.geo_x) and (h1.geo_y == boss.geo_y):
        print("Вы чувствуете сильное давление,"
              "\nвы подверглись неожиданной атаке, но уклонились."
              "\nВнезапно оппонент заговорил"
              "\n"
              "\n<<Кто ты? Я тебя дальше не пущу!>>"
              "\nВы понимаете, что бой неизбежен... или, все-таки, побег?")
        break

while True:
    if boss.health <= 0:
        print("Вы победили босса и спасли принцессу! \nВаша награда: ", wolk.money, "золотых.")
        h1.money += boss.money
        input()
        break
    else:
        print("Ваше здоровье: ", h1.health, "Здоровье Врага: ", boss.health)
        if h1.health < 0:
            print("Конец игры")
            break
        else:
            h1.power = 75
            boss.damage_from_monster()
            h1.getHit(boss.power)
            if h1.ability > 0:
                print("удар/слово силы/побег")
                temp_reaction = input()
                if temp_reaction == 'слово силы':
                    crit = random.randint(0, 1)
                    if crit == 1:
                        print('-----------------------------')
                        print('!!!Вы используете слово силы!!!')
                        print('!!!FUS RO DAH!!!')
                        print('-----------------------------')
                        h1.power += 30
                        boss.getHit(h1.power)
                        h1.power -= 30
                    else:
                        print('слово силы не удалась')
                        boss.getHit(h1.power)
                elif temp_reaction == 'удар':
                    boss.getHit(h1.power)
                elif temp_reaction == 'побег':
                    break
                else:
                    print("Произошла ошибка!")
            else:
                print("удар/побег")
                temp_reaction = input()
                if temp_reaction == 'удар':
                    crit = random.randint(0, 1)
                    if crit == 1:
                        print('---------------------------')
                        print('!!!Вы пробили с двух рук!!!')
                        print('---------------------------')
                        h1.power += 15
                        boss.getHit(h1.power)
                        h1.power -= 15
                    else:
                        boss.getHit(h1.power)
                elif temp_reaction == 'побег':
                    break
                else:
                    print("Произошла ошибка!")
for i in range(10):
    print("\nКОНЕЦ")
    break
