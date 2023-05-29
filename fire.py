from pokemon import Pokemon
import random

class Fire(Pokemon):
  def __init__(self, name):
    '''
    calls super to set the name and type fire = 0 
    '''
    super().__init__(name, 0)
  
  def get_special_menu(self):
    """returns special move menu for fire type"""
    return "Choose a move\n1. Ember\n2. Flame Charge\n"
  
  def _special_move(self, opponent, move):
    if move == 1:
      return self._ember(opponent)
    elif move == 2:
      return self._flame_charge(opponent)

  def _ember(self, opponent):
    '''
    ember pokemon move that does damage between 1 and 5 randomly
    '''
    damage = random.randint(1, 5)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    opponent.take_damage(total_damage)
    if multiplier == 2:
      return f"{self._name} used Ember and dealt {total_damage} damage (super effective) to {opponent._name} "
    elif multiplier == 0.5:
      return f"{self._name} used Ember and dealt {total_damage} damage (not very effective) to {opponent._name} "
    else:
      return f"{self._name} used Ember and dealt {total_damage} damage to {opponent._name} "

  def _flame_charge(self, opponent):
    '''
    flame charge pokemon move that does damage between 3 and 4 randomly
    '''
    damage = random.randint(3, 4)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    opponent.take_damage(total_damage)
    if multiplier == 2:
      return f"{self._name} used Flame Charge and dealt {total_damage} damage (super effective) to {opponent._name} "
    elif multiplier == 0.5:
      return f"{self._name} used Flame Charge and dealt {total_damage} damage (not very effective) to {opponent._name}"
    else:
      return f"{self._name} used Flame Charge and dealt {total_damage} damage to {opponent._name} "
