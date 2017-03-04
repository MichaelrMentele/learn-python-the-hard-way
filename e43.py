# e43.py
# Learn Python the hard way refresh

''' Problem solving in OOP
1. Write/Draw the Problem (Dissect)
2. Extract key concepts and research (identify)
3. create a class hierarchy and object map for the concepts (synthesize)
4. code the classes and test (execute)
5. iterate

* map
	-next scene
	-opening_scene
* engine
	-play
* scene
	-enter
	* death
	* central corridor
	* laser weapon armory
	* the bridge
	* escape pod

'''
from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print("This scene is not yet configured. Subclass it and implement enter()")
		exit(1)

class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Really? You died like that.",
		"What were you thinking?",
		"You're dead. Ahaha.",
		"T.T"
	]

	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print(
			"The Space Monkeys have invaded your ship and eaten\n" +
			"your entire crew. You are the last surviving member\n" +
			"and you have to stop the monkey's from invading earth\n" +
			"and causing planet of the Apes to happen. Go find the\n" +
			"ships reactor, overload it and then get the hell out on\n" +
			"an escape pod.\nYou are running down the central corridor\n" +
			"to the armory when a monkey samurai jumps out, feathers\n" +
			"poking from his armor. Wait, what? No time to think he is\n" +
			"in your way and about to pull a blaster!"
		)

		action = input("> ")

		if action == "shoot!":
			print(
				"Quick on the draw you yank out your missile launcher...\n" +
				"Damnit! Why the hell do you have a missile launcher on a\n" +
				"space ship. Struggling to aim it you raise of the launcher\n"
				"and blow him away--or try! The missile flies wide and\n" +
				"doesn't even explode! The monkey/bird/thing chortles\n" +
				"and blows you away with his blaster."
			)
			return('death')
		elif action == "dodge!":
			print(
				"You try to dodge but you are holding a missile launcher.\n"
			)
			return('death')
		elif action == "tell a joke":
			print(
				"Luckily, you owned a monkey and know what they find funny.\n" +
				"You remember a joke, \"Ooo o ooh oooh ooo o OH OH OH AHHH!\"\n" +
				"The monkey tries not to laugh but can't help it. You raise\n" +
				"rocket and take aim."
				)
			return('laser_weapon_armory')
		else:
			print("DOES NOT COMPUTE")
			return('central_corridor')

class LaserWeaponArmory(Scene):

	def enter(self):
		print(
			"You do a dive roll into the Weapon Armory crouch and scan the room.\n" +
			"The room seems empty. You stand and run to the far side of the room.\n" +
			"You spot the reactor. You need to enter a 3-digit code. You recall\n" + 
			"the engineer saying you got 10 tries and then you would be locked out\n" +
			"of the system."
		)
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = input("[keypad]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print("BZZZEDD!")
			guesses += 1
			guess = input("[keypad]> ")

		if guess == code:
			print(
				"You access the engineering terminal. It takes you a few minutes to figure out how to set the self destruct. But you do. 10 minutes and then kaBOOM!"
			)
			return 'the_bridge'
		else: 
			print("You are locked out and totally boned.")
			return 'death'



class TheBridge(Scene):

	def enter(self):
		print("You are on the bridge.")

		action = input("> ")

		if action == "yell insults":
			print("You yell insults and then turn towards the escape pods.")
		else:
			return 'death'

class EscapePod(Scene):

	def enter(self):
		print("Running through the ship. 5 pods, which do you take?")

		good_pod = randint(1,5)
		guess = input("[pod #]> ")

		if int(guess) != good_pod:
			return 'death'
		else:
			print("Nice guess.")
			return 'finished'

class Finished(Scene):

	def enter(self):
		print("Congratz! You win.")
		return 'finished'

class Map(object):

	scenes = {
		'central_corridor' : CentralCorridor(),
		'laser_weapon_armory' : LaserWeaponArmory,
		'the_bridge' : TheBridge(),
		'escape_pod' : EscapePod(),
		'death' : Death(),
		'finished' : Finished(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def opening_scene(self):
		return self.next_scene(self.start_scene)

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		current_scene.enter()

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()