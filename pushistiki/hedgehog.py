from .pushistik import Pushistik
from random import choice

class Hedgehog(Pushistik):
    def play(self):
        choices = ['катается по полу', 'играет в домино']
        print(f'Ёжик {self.name} {choice(choices)}')