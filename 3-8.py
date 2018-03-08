class NewClass():
	instance_number = 0
	def count():
		instance_number += 1
	def __init__(self):
		count()
	
	@classmethod
	def printInstanceN():
		print 'Number of the instances created: ',instance_number