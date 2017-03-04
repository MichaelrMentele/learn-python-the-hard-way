# Review: Learn Python The Hard Way
# e40.py
# Class example

class Car(object):

	def __init__(self, type):
		self.type = type

	def drive(self):
		print("Driving")

truck = Car("Truck")

truck.drive()


class Bird(object):

	def __init__(self, species, birdsong):
		self.species = species
		self.birdsong = birdsong

	def sing(self):
		for line in self.birdsong:
			print(line)

seagull = Bird("seagull", ["caw", "caw, caw, squak, shriek"])
seagull.sing()

songs = {
			"Seagull" : ["Shriek, piercing cry!"],
			"Finch" : ["Tweet, Tweet."],
			"Eagle" : ["Ayeee, Ayeee"]
		}

bird_species = "Seagull"
seagull = Bird(bird_species, songs[bird_species])
seagull.sing()

bird_species = "Eagle"
eagle = Bird(bird_species, songs[bird_species])
eagle.sing()