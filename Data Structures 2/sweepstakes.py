import random
from contestant import Contestant


class Sweepstake:

    def __init__(self):
        self.contestants = {}
        self.winner = ''

    def add_contestants(self, name):
        key = len(self.contestants) + 1
        self.contestants[key] = name

    def pick_contestant(self):
        sweepstake_winner = random.randint(1, len(self.contestants))
        self.winner = self.contestants.get(sweepstake_winner)
        print(f'Congrats to {self.winner}! You are the chosen WINNER!!')


