class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy...............","xxxxxxxxxxxxxxxxxxxx"])

happy_bday.sing_me_a_song()