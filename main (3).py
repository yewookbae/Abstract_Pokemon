#Name: Stefan Barua, Christian Bae
#Date: 03/13/23
#Desc: Abstracting to beat 3 pokemon to win.
from pokemon import Pokemon
from fire import Fire
from water import Water
from grass import Grass
import random
import check_input
class Main:
  '''Main: driver method'''
  gym_pokemon = []
  gym_type = random.randint(0, 2)

  if gym_type == 0:
    gym_pokemon = [Fire('Torchic'), Fire('Growlithe'), Fire('Lampert')]
    gym_type = 'FIRE'
  elif gym_type == 1:
    gym_pokemon = [Water('Gyarados'), Water('Vaporeon'), Water('Swampert')]
    gym_type = 'WATER'
  else:
    gym_pokemon = [Grass('Oddish'), Grass('Bellsprout'), Grass('Exeggcute')]
    gym_type = 'GRASS'
  
  print(f'PROF OAK: Hello Trainer! Today you\'re off to fight your first gym battle of 1 vs. 3 {gym_type} pokemon. Select the pokemon that you will fight with.\n1. I choose you, Charmander.\n2.Squirtle! GO!\n3.We can do it, Bulbasaur!')   #prints beginning message
  user_type = check_input.get_int_range('Please choose a pokemon: ', 1, 3)
  if user_type == 1:
    player = Fire('Charmander')
  elif user_type == 2:
    player = Water('Squirtle')
  else:
    player = Grass('Bulbasaur')

  print('  -- GYM BATTLE --')
  while gym_pokemon and player.hp != 0: #start of game loop
    print('...')
    print('GYM LEADER: I choose you:')
    print(gym_pokemon[0])
    print('\n' + str(player))
    
    attack_type = check_input.get_int_range('Choose an Attack Type:\n1. Normal\n2. Special\nEnter attack type: ', 1, 2)

    if attack_type == 1: 
      move = check_input.get_int_range(player.get_normal_menu(), 1, 2)
    elif attack_type == 2:
      move = check_input.get_int_range(player.get_special_menu(), 1, 2)
     
    print(player.attack(gym_pokemon[0], attack_type, move))

    if gym_pokemon[0].hp != 0:
      print(gym_pokemon[0].attack(player, random.randint(1, 2), random.randint(1, 2)))
    else:
      gym_pokemon.pop(0)
      print("GYM LEADER: NOOOOO! You defeated my pokemon!")

  if player.hp != 0: 
    print("YOU WON! You defeated the gym leader.")
  else: 
    print("You Lose. L")