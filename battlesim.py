import json
import os
import os.path
import time
import sys
from random import randint, randrange
import random
os.system('clear')

#------------------- Variables 
shinyRoll = randint(1, 4096) 


#-------------------



#------------------- JSON (for testing)
with open('pkmn.json', 'r') as file:
	pkmn = json.load(file)
with open('dialogue.json', 'r') as file2:
	dialogue = json.load(file2)

#-------------------

#------------------- Functions
def clear():
	os.system('clear')

def loading():        # loading animation
	load = "|\—/"
	idx = 0
	while True:
		print(load[idx % len(load)], end="\r")
		idx += 1
		time.sleep(0.14)
		if idx == 20:
			break


def load_log():
	try:
		with open('logFile.json', 'r') as file:
			log_data = json.load(file)
		return log_data
	except (json.JSONDecodeError, IOError):    # default logfile
		return {"name": "Trainer", "id": 000000, "battles_won": 0, "battles_lost": 0, "badges": 0, "shinies_encountered": 0}


def save_log(log_data):
	with open('logFile.json', 'w') as file:
		json.dump(log_data, file, indent=4)


def create_log_file():       # create the log if it doesn't exist yet
	playerName = input("What's your name?: ")
	trainer_id = randint(100000, 999999)  # Random ID

	log_data = {
		"name": playerName,
		"id": trainer_id,
		"battles_won": 0,
		"battles_lost": 0,
		"badges": 0,
		"shinies_encountered": 0
	}

	with open("logFile.json", "w") as log_file:
		json.dump(log_data, log_file, indent=4)
	print("Creating your battle log...")
	loading()
	time.sleep(0.1)
	print("done!\nPlease restart the program to continue.")
	exit()

def checkLog():      # Check if log is readable. If not, force exit.
	log_file_path = 'logFile.json'
	if os.path.exists(log_file_path):
		try:
			with open(log_file_path, 'r') as log_file:
				log_data = json.load(log_file)
				print(f"Bill: Hiya, {log_data['name']}!\nWhatcha' need?")
		except (json.JSONDecodeError, IOError) as e:
			print(f"Error reading the log file: {e}")
			print("The log file is corrupted or unreadable. Please restart the program.")
			exit()
	else:
		create_log_file()

def load_log():
	try:
		with open('logFile.json', 'r') as file:
			log_data = json.load(file)
		return log_data
	except (json.JSONDecodeError, IOError):     # default logfile
		return {"name": "Trainer", "id": 000000, "battles_won": 0, "battles_lost": 0, "badges": 0, "shinies_encountered": 0}


def updateLog():
	log_data = {
		"name": playerName,
		"id": trainerID,
		"battles_won": battlesWon,
		"battles_lost": battlesLost,
		"badges": gymBadges,
		"shinies_encountered": shinyEncounters
	}

	with open("logFile.json", "w") as log_file:
		json.dump(log_data, log_file, indent=4)


def giveBadge():     # check if a badge is to be given (currently unused)
	global gymBadges 
	if checkGymLeader == True:
		gymBadges += 1
		updateLog()
	elif checkGymLeader == False:
		pass


def shinyChance():    # shiny chance
	global shinyEncounters
	if shinyRoll == 1995:
		print("You've found a shiny!\nAdded to your log.")
		# to-do: add shiny to logfile
	else:
		pass



def listTrainers():
		clear()
		readme = open("./txtxt/trainers.txt", "r")
		print(readme.read())
		input("\n\npress ENTER to exit")
		clear()

def listPkmn():
		clear()
		readme = open("./txtxt/pkmn.txt", "r")
		print(readme.read())
		input("\n\npress ENTER to exit")
		clear()


def get_pokemon_details(pokemon_name):
	try:
		with open('pkmn.json', 'r') as file:
			pkmn_data = json.load(file)
		pokemon_name = pokemon_name.lower()
		if pokemon_name in pkmn_data["pokemon"]:
			return pkmn_data["pokemon"][pokemon_name]  
		else:
			print(f"Pokemon {pokemon_name} not found in the database.")
			return None
	except (json.JSONDecodeError, IOError):
		print("Error loading Pokémon data.")
		return None


def simulate_battle(player_pokemon_name, opponent_pokemon_name):
	player_pokemon = get_pokemon_details(player_pokemon_name)
	opponent_pokemon = get_pokemon_details(opponent_pokemon_name)

	if not player_pokemon or not opponent_pokemon:
		print("Invalid Pokémon data!")
		return

	player_hp = player_pokemon['hp']
	opponent_hp = opponent_pokemon['hp']
	opponent_status = None  
	player_status = None  

	print(f"\n{player_pokemon['name']} (HP: {player_hp}) vs. {opponent_pokemon['name']} (HP: {opponent_hp})\n")
	while player_hp > 0 and opponent_hp > 0:
		display_moveset(player_pokemon)
		move_choice = input(f"Choose your move (1-{len(player_pokemon['moveset'])}): ")
		try:
			move_choice = int(move_choice)
			if move_choice < 1 or move_choice > len(player_pokemon['moveset']):
				print("Invalid choice! Please choose a valid move.")
				continue
		except ValueError:
			print("Invalid input! Please choose a valid number.")
			continue

		player_move = player_pokemon['moveset'][move_choice - 1]
		print(f"\n{player_pokemon['name']} uses {player_move['move']}!")

		if 'effect' in player_move:
			opponent_status = apply_status_effect(player_move, opponent_status, target="opponent")
		else:
			damage = player_move['power']
			if random.random() < 0.1:  
				damage = int(damage * 1.5)
				print(f"Critical hit! The damage is increased to {damage}.\n")
			opponent_hp -= damage
			print(f"It dealt {damage} damage! Opponent's HP is now {max(0, opponent_hp)}\n")

		if opponent_hp <= 0:
			print(f"{opponent_pokemon['name']} fainted! {player_pokemon['name']} wins the battle!")
			update_battle_log('win')
			break

		if opponent_status == "paralyzed" and random.random() < 0.25:
			print(f"{opponent_pokemon['name']} is paralyzed and cannot move!")
			continue
			
		if opponent_status == "asleep" and random.random() < .75:
			print(f"{opponent_pokemon['name']} is asleep!")
			continue

		opponent_move = random.choice(opponent_pokemon['moveset'])
		print(f"{opponent_pokemon['name']} uses {opponent_move['move']}!")

		if 'effect' in opponent_move:
			player_status = apply_status_effect(opponent_move, player_status, target="player")
		else:
			damage = opponent_move['power']
			if random.random() < 0.1:              # critical hit
				damage = int(damage * 1.5)
				print(f"Critical hit! The damage is increased to {damage}.\n")
			player_hp -= damage
			print(f"It dealt {damage} damage! {player_pokemon['name']}'s HP is now {max(0, player_hp)}\n")

		if player_hp <= 0:
			print(f"{player_pokemon['name']} fainted! {opponent_pokemon['name']} wins the battle!")
			update_battle_log('lose')
			break


def display_moveset(pokemon):
	print(f"\n{pokemon['name']} Moveset:")
	for i, move in enumerate(pokemon['moveset'], start=1):
		effect_text = f" (Effect: {move['effect']})" if 'effect' in move else ""
		print(f"{i}. {move['move']} (Power: {move['power']}, Type: {move['type']}){effect_text}")


# apply any status effects to the opponent
def apply_status_effect(move, current_status, target="opponent"):
	effect = move.get('effect')
	if effect == "Paralyzes the opponent" and current_status != "paralyzed":
		print(f"{target.capitalize()} is paralyzed! It may be unable to move!")
		return "paralyzed"
	elif effect == "Lowers the opponent's attack":
		print(f"{target.capitalize()}'s attack is lowered!")
	elif effect == "Puts the opponent to sleep" and current_status != "asleep":
		print(f"{target.capitalize()} is now asleep!")
		return "asleep"
	elif effect == "Raises the user's defense":
		print(f"{target.capitalize()}'s defense is raised!")
	elif effect == "Lowers the opponent's speed":
		print(f"{target.capitalize()}'s speed is lowered!")
	elif effect == "Forces the opponent to use attacking moves only":
		print(f"{target.capitalize()} is taunted and can only use attacking moves!")
	return current_status



def update_battle_log(result):
	log_data = load_log()
	if result == 'win':
		log_data["battles_won"] += 1
	else:
		log_data["battles_lost"] += 1
	save_log(log_data)



def start_battle():
	print("placeholder text")
	player_choice = input("Choose your Pokémon: ").lower()
	opponent_choice = "missingno"      # pokemon you wish to battle
	simulate_battle(player_choice, opponent_choice)


#-------------------
loading()
shinyChance()
while True:
	checkLog()
	print("[1] boot-up Simulator [2] PKMN [3] view TRAINERS [4] TRAINER card [5] about [E] exit\n")
	startup = str(input("> "))
	if startup == "E":
		break
	elif startup == "5":
		clear()
		readme = open("./txtxt/README.md", "r")
		print(readme.read())
		input("\n\npress ENTER to exit")
		clear()
	elif startup == "4":
		clear()
		print("------------------ Trainer Card")
		howto = open("logFile.json", "r")
		print(howto.read())
		print("------------------ ◓")
		input("\n\npress ENTER to exit")
		clear()
	elif startup == "3":
		listTrainers()
	elif startup == "2":
		listPkmn()
		pass
	elif startup == "1":
		clear()
		start_battle()
	else:
		clear()
		print(">> invalid input")
