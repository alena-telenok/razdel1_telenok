class NotImplementedException(Exception):
    pass

class Pushistik:

    def __init__(self, name, weight, price, speed = None):
        self.name = name
        self.weight = weight
        self.weight1 = weight
        self.price = price
        self.speed = speed

    def __str__(self):
        ret = f'Пушистик {self.__class__.__name__}: имя={self.name}; вес={self.weight}кг; цена={self.price}руб;'
        if self.speed:
            ret += f' скорость={self.speed}км/ч'
        return ret

    def run(self):
        print(f'Пушистик {self.name} бежит со скоростью {self.speed * self.weight1 / self.weight}км/ч при весе {self.weight}кг')

    def eat(self, food):
        self.weight = self.weight + 0.1
        print(f'Пушистик {self.name} покушал {food}, и его вес увеличился на 100 грамм! Теперь он весит {self.weight}кг')

    def play(self):
        # pass
        raise NotImplementedException(f'Метод не реализован для общего класса {self.__class__.__name__}')

if __name__ == '__main__':
    musya = Pushistik('Муся', 3, 100, 25)
    print(musya)
    musya.run()
    musya.eat('колбаску')
    musya.run()
    musya.eat('вискас')
    musya.run()
    musya.play()