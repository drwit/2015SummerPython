from sys import exit
from random import randint

class Scene(object):
	
	def enter(self):
		pass
				
class Engine(object):

	def __init__(self, scene_map):
		pass
	
	def play(self):
		pass
		
class Death(Scene): 														# done
	
	titles = [
		"Try harder!",
		"Your mom cried so badly.",
		"It suckes",
		"Still not married?",
		"God bless you"
	]
	
	def enter(self):
		print self.titles[randint(0, len(self.titles)-1)]
		
class Bed(Scene):															# done
	chances = 4
	
	def enter(self):
		print "Now you are lying on the bed."
		print "You believe that only by guess out the true number can you stay alive."
		print "And the key number is among 0 - 9, meanwhile %d chances remained." % self.chances
		print "Now close your eyes, pick a number:"
		
		answer = randint(0,9)
		val = int(raw_input("> "))
		guesses = 1
		
		while val != answer and guesses < self.chances:
			if val < answer:
				print "Too little,man. Try again."			
			else:
				print "Too large,man. Try again."
			val = int(raw_input("> "))
			guesses = guesses + 1
		
		if val == answer:
			print "Yes it is! You jump down the bed."
			return "Toilet"
		else:
			print "YOU FALL IN THE DREAM."
			return "Death"
		
class BehindTheDoor(Scene):

	def enter(self):
		pass
		
class Alive(Scene):

	def enter(self):
		print "Finally you go to heaven"	
		exit(1)

class Toilet(Scene):														# todo

	def enter(self):
		print "You meet the Toilet God."
		print "He's bald.SILLY."
		print "He asks: 'AM I HANDSOME?'"
		
		val = raw_input("Your choice? > ")
		if val == "Yes" or val == "yes" or val == "Yes!" val == "yes!":
			print "'Good.' Toilet God says."
			return "Alive"
			
		else:
			print "'CAREFUL KID!'"
			return "Death"
		
class Map(object):

	scenes = {
		"Death" : Death(),
		"Bed" : Bed(),
		"BehindTheDoor" : BehindTheDoor(),
		"Toilet" : Toilet(),
		"Alive" : Alive(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes[scene_name]
		return val
		
	def opening_scene(self):
		pass
			
		
		
		
		
		
		
		
		
		