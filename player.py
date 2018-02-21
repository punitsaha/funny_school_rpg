from random import randint
from character import Character
from enemy import Enemy

class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 10
    self.health_max = 10
    self.wealth = 100
  def quit(self):
    print ("%s remembers about the subject backs, and commits suicide from depression.\nR.I.P." % self.name)
    self.health = 0
  def help(self):  print (Commands.keys())
  def status(self): print ("%s's health: %d/%d" % (self.name, self.health, self.health_max))
  def tired(self):
    print ("%s feels tired." % self.name)
    self.health = max(1, self.health - 1)
  def rest(self):
    if self.state != 'normal': print ("%s can't rest now!" % self.name); self.enemy_attacks()
    else:
      print ("%s rests." % self.name)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print ("%s is rudely awakened by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print ("%s slept too much." % self.name); self.health = self.health - 1
  def explore(self):
    if self.state != 'normal':
      print ("%s is too busy right now!" % self.name)
      self.enemy_attacks()
    else:
      print ("%s explores through the hallways." % self.name)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print ("%s comes face to face with %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired()
  def bhaag(self):
    if self.state != 'fight': print ("%s runs around for a while." % self.name); self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print ("%s runs away from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print ("%s couldn't run away from %s!" % (self.name, self.enemy.name)); self.enemy_attacks()
  def attack(self):
    if self.state != 'fight': print ("%s shouts in the hallways, pointlessly." % self.name); self.tired()
    else:
      if self.do_damage(self.enemy):
        print ("%s ne %s ko kaat dala!" % (self.name, self.enemy.name))
        self.wealth = self.wealth + self.enemy.wealth
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          print ("%s feels takatwar!" % self.name)
      else: self.enemy_attacks()
  def enemy_attacks(self):
    if self.enemy.do_damage(self): print ("%s was killed by %s!!!\nR.I.P." %(self.name, self.enemy.name))
  def wealth(self):
    print('Money left: %d' % self.wealth)
    if(self.health < self.health_max):
      heal = input("Want to use money to heal? (Y/N) ")
      if(heal == 'Y'):
        heal_amount = int(input("How much health do you need? "))
        if (heal_amount <= self.health_max - self.health and heal_amount * 10 < self.wealth):
          self.health = self.health + heal_amount
          self.wealth = self.wealth - heal_amount * 10
          print("%s feels MAST!!! " % self.name)
        else:
          print("How?.......This doesn't make any sense...")
      else:
        print("...eeyyyeee....")


from commands import Commands
