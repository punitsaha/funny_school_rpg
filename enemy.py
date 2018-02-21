from character import Character
from random import randint

class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = 'zombie'
    self.health = randint(1, player.health)
    self.wealth = randint(self.health, 5*self.health)
