from pokemon import Pokemon
import random

class Grass(Pokemon):
  def __init__(self, name):
    super().__init__(name, 2)
  def get_special_menu(self):
    '''
    returns the menu for special move for grass type
    '''
    return "Choose a move:\n1. Razor Leaf\n2. Solar Beam\n"
  
  def _special_move(self, opponent, move):
    if move == 1:
      return self._razor_leaf(opponent)
    elif move == 2:
      return self._solar_beam(opponent)

  def _razor_leaf(self, opponent):
    '''
    Razor Leaf pokemon move that does damage between 1 and 5 randomly
    '''
    damage = random.randint(1, 5)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    opponent.take_damage(total_damage)
    if multiplier == 2:
      return f"{self._name} used Razor Leaf and dealt {total_damage} damage (super effective) to {opponent._name} "
    elif multiplier == 0.5:
      return f"{self._name} used Razor Leaf and dealt {total_damage} damage (not very effective) to {opponent._name} "
    else:
      return f"{self._name} used Razor Leaf and dealt {total_damage} damage to {opponent._name} "

  def _solar_beam(self,opponent):
    '''
    solar beam pokemon move that does damage between 3 and 4 randomly
    '''
    damage = random.randint(3,4)
    multiplier = self._battle_table[self._type][opponent._type]
    total_damage = int(damage * multiplier)
    opponent.take_damage(total_damage)
    if multiplier == 2:
      return f"{self._name} used Solar Beam and dealt {total_damage} damage (super effective) to {opponent._name} "
    elif multiplier == .5:
      return f"{self._name} used Solar Beam and dealt {total_damage} damage (super effective) to {opponent._name} "
    else:
      return f"{self._name} used Razor Solar Beam and dealt {total_damage} damage (super effective) to {opponent._name} "