"""Problem:  Return a random unique number from a given range

Copyright:  Noah Gift - 08/06/2016
"""

import random

PREVIOUS = {}
MAX=50

def number_seq(max=MAX):
	ran = random.randint(1, 100)
	if ran < MAX and ran not in PREVIOUS:
		PREVIOUS[ran] = ""
		print ran
		#print PREVIOUS
		return ran
	else:
		count = len(PREVIOUS.keys())
		if count ==  MAX - 1:
			print "No more numbers to give"
			return False
		else:
			number_seq()

if __name__ == '__main__':
	#self-test
	val = MAX*2
	for i in range(val):
		print "iteration: ", i
		res = number_seq()
		count = len(PREVIOUS.keys())
		if count == MAX -1:
			print "Numbers found: ", count
			print "simulation stopped"
			break