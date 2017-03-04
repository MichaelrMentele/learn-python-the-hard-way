# Review: Learn Python The Hard Way
# e41.py
# Speak OOP

terms = {
			"class" : "Tell Python to make a new type of thing, a new blueprint for things",
			"object" : "An instance of a class. The most basic type of thing, or the class for all things.",
			"instance" : "A particular thing created from a class",
			"def" : "The way you define functions and methods inside of a class or module",
			"self" : "A reference tot he curent instance.",
			"inheritance" : "A word to describe how classes are hierarchechal and pass things on to their children.",
			"composition" : "The idea that a class can be composed of over classes. An object can be a superclass and be made up of smaller objects.",
			"attribute" : "A property of a class is a variable ON THE CLASS and not on the instance...",
			"is-a" : "Denotes inheritance from a sub class to its super class, an eagle is a bird for instance",
			"has-a" : "A way to describe an attribute or something about a class or has a trait. A bird has a beak."
		}

for key, value in terms.items():
	print("What is " + key + "?")
	input()
	print("The answer is " + value + "\nDid you get it right?")


code_snippets = {
					"class X(Y)" : "Make a class named X that is-a Y.",
					"class X(object): def __init__(self, J)" : "class X has-a __init__ that takes self and J parameters.",
					"class X(object): def M(self, J)" : "class X has-a function named M that takes self and J parameters.",
					"foo = X()" : "Set foo to an instance of class X.",
					"foo.M(J)" : "From foo get the M function, and call it with parameters self, J.",
					"foo.K = Q" : "From foo get the K attribute and set it to Q."				
				}

for key, value in code_snippets.items():
	print("What is " + key + "?")
	input()
	print("The answer is " + value + "\nDid you get it right?")			