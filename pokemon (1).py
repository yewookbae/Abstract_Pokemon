from abc import abstractmethod
import random
import check_input
class Pokemon:
  _battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]]
    
  def __init__(self, name, type):
    self._name = name
    self._type = type
    self._hp = 25
  
  @property    
  def hp(self):
    return self._hp
  
  def get_normal_menu(self):
    '''
    returns normal move menu
    '''
    return "1. Slam\n2. Tackle\n"
  
  def _normal_move(self, opponent, move):
    '''
    Gets players input for the normal move then does the requested normal move
    '''
    
    if move == 1:
      return self._slam(opponent)
    elif move == 2:
      return self._tackle(opponent)
  
  def _slam(self, opponent):
    '''
    slam pokemon move that does damage between 1 and 8 randomly
    '''
    damage = random.randint(1, 8)
    opponent.take_damage(damage * self._battle_table[self._type][opponent._type])
    return f"{self._name} used Slam on {opponent._name} dealing {damage} damage"
  
  def _tackle(self, opponent):
    '''
    tackle pokemon move that does damage between 3 and 6 randomly
    '''
    damage = random.randint(3, 6)
    opponent.take_damage(damage * self._battle_table[self._type][opponent._type])
    return f"{self._name} used Tackle on {opponent._name} dealing {damage} damage"
  @abstractmethod
  def get_special_menu(self):
    raise NotImplementedError()
  @abstractmethod
  def _special_move(self, opponent, move):
    raise NotImplementedError()
  
  def attack(self, opponent, move_type, move):
    '''
    Gets players input for the attack move then does the requested move
    '''
    if move_type == 1:
      return self._normal_move(opponent, move)
    elif move_type == 2:
      return self._special_move(opponent, move)

  def __str__(self):
    '''
    returns health
    '''
    return f"{self._name}: {self._hp}/25"
  
  def take_damage(self, dmg):
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0
