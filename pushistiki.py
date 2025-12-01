import random
from pushistiki import Pushistik, Cat, Dog, Hedgehog

musya = Cat('Муся', 3, 100, 25)
musya.play()
ralph = Dog('Ральф', 20, 500, 40)
ralph.play()
barni = Dog('Барни', 50, 1000, 15)
barni.play()
pyzhik = Dog('Пыжик', 30, 200, 30)
pyzhik.play()
egor = Hedgehog('Егор', 0.4, 3000, 5)
egor.play()

class Shop:

    def __init__(self, name):
        self.name = name
        self.cats = []
        self.dogs = []
        self.hedgehogs = []

    def add(self, type, pushistik):
        if 'котик' == type:
            self.cats.append(pushistik)
        if 'пёсик' == type:
            self.dogs.append(pushistik)
        if 'ёжик' == type:
            self.hedgehogs.append(pushistik)

    def show(self):
        print('В нашем магазине есть следующие виды пушистиков:')
        print('Котики:')
        for cat in self.cats:
            print(cat)
        print('Пёсики:')
        for dog in self.dogs:
            print(dog)
        print('Ёжики:')
        for hedgehog in self.hedgehogs:
            print(hedgehog)

    def gift(self):
        dog = random.choice(self.dogs)
        self.dogs.remove(dog)
        return dog


shop = Shop('Милые пушистики')
shop.add('котик', musya)
shop.add('пёсик', ralph)
shop.add('пёсик', barni)
shop.add('пёсик', pyzhik)
shop.add('ёжик', egor)

class NotImplementedException(Exception):
    ...


print(f"Приветствуем вас в магазине {shop.name}!")

enter = input("Желаете купить пушистика (да/нет)?")

if 'да' == enter:
    print("Добро пожаловать!")
    shop.show()

    choose = input("Кого хотите купить: котика (1), ёжика (2), пёсика (3)?")

    try:
        if '1' == choose:
            raise NotImplementedException("Извините, котиков уже распродали!")
        elif '2' == choose:
            raise NotImplementedException("Ёжики сейчас в спячке!")
        elif '3' == choose:
            a = input("Отличный выбор! Рады сообщить, что сегодня в магазине проходит акция: угадайте слово из набора слов и получите пёсика в подарок! Желаете поучаствовать (да/нет)?")
            if "да" == a:
                def play():
                    print("Отлично, называйте слово!")

                    s = input("Какое слово выбираете (корм, поводок, шерсть, косточка, игрушка)?")

                    words = ["корм", "поводок", "шерсть", "косточка", "игрушка"]

                    win = random.randint(0, 4)

                    if s not in words:
                        raise NotImplementedException("Пожалуйста назовите слово из указанных!")

                    if s == words[win]:
                        print("Поздравляем, вы выиграли пёсика!")
                        return True
                    else:
                        print(f"Вы проиграли, слово было {words[win]}, увы!")
                        return False


                dogs = []
                while True:
                    if 0 == len(shop.dogs):
                        print('Извините, в магазине кончились пёсики!')
                        break
                    с = play()
                    if True == с:
                        dog = shop.gift()
                        dogs.append(dog)
                        vkusnyashka = input(f'Какую вкусняшку дадите {dog.name}?')
                        dog.eat(vkusnyashka)
                        print(f'{dog.name} радостно бежит к вам!')
                        dog.run()
                    repeat = input(f'С вами домой уже уходят следующие пёсики: {[let.name for let in dogs]}! Но ведь их много не бывает! Сыграем еще? (да/нет)')

                    if repeat.strip().lower() == 'нет':
                        break
            elif "нет" == a:
                print("Хорошо, тогда с вас 100 рублей!")

    except NotImplementedException as err:
        print(f'Не работает: {err}')

    print('Заходите еще!')

elif 'нет' == enter:
    print("Нам жаль что сегодня вы ушли от нас без пушистика! Будем ждать вас снова!")