from .pushistik import Pushistik
from random import choice

class Cat(Pushistik):
    def play(self):
        choices = ['бегает за мышкой', 'прыгает по полкам', 'обдирает обои']
        print(f'Котик {self.name} {choice(choices)}')