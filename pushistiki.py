import random


class NotImplementedException(Exception):
    ...


print("Приветствуем вас в магазине Милые пушистики!")

enter = input("Желаете купить пушистика (да/нет)?")

if 'да' == enter:
    print("Добро пожаловать!")

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


                b = 0
                while True:
                    с = play()
                    if True == с:
                        b += 1
                    repeat = input(f'С вами домой уже уходит {b} пёсиков! Но ведь их много не бывает! Сыграем еще? (да/нет)')

                    if repeat.strip().lower() == 'нет':
                        break
            elif "нет" == a:
                print("Хорошо, тогда с вас 100 рублей!")

    except NotImplementedException as err:
        print(f'Не работает: {err}')

    print('Заходите еще!')

elif 'нет' == enter:
    print("Нам жаль что сегодня вы ушли от нас без пушистика! Будем ждать вас снова!")