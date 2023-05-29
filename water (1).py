from pokemon import Pokemon
import random

class Water(Pokemon):
  def __init__(self, name):
    super().__init__(name, 1)
  
  def get_special_menu(self):
    '''
    returns special move menu for water type
    '''
    return "Choose a move:\n1. Water Gun\n2. Bubble Beam\n"
  
  def _special_move(self, opponent, move):
    if move == 1:
      return self._water_gun(opponent)
    elif move == 2:
      return self._bubble_beam(opponent)

  def _water_gun(self, opponent):
    '''
    water gun pokemon move that does damage between 1 and 5 randomly
    '''
    damage = random.randint(1, 5)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    opponent.take_damage(total_damage)
    if multiplier == 2:
      return f"{self._name} used Water Gun and dealt {total_damage} damage (super effective) to {opponent._name} "
    elif multiplier == 0.5:
      return f"{self._name} used Water Gun and dealt {total_damage} damage (not very effective) to {opponent._name}"
    else:
      return f"{self._name} used Water Gun and dealt {total_damage} damage to {opponent._name} "

  def _bubble_beam(self, opponent):
    '''
    Bubble beam pokemon move that does damage between 3 and 4 randomly
    '''
    damage = random.randint(3, 4)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    opponent.take_damage(total_damage)
    if multiplier == 2:
      return f"{self._name} used Bubble Beam and dealt {total_damage} damage (super effective) to {opponent._name} "
    elif multiplier == 0.5:
      return f"{self._name} used Bubble Beam and dealt {total_damage} damage (not very effective) to {opponent._name} "
    else:
      return f"{self._name} used Bubble Beam and dealt {total_damage} damage to {opponent._name} "