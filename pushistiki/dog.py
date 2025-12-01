from .pushistik import Pushistik
from random import choice

class Dog(Pushistik):
    def play(self):
        choices = ['бесится', 'приносит палочку', 'бегает за своим хвостиком']
        print(f'Пёсик {self.name} {choice(choices)}')