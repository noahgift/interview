"""
Problem:  Return a random unique collection from a list

Copyright:  Noah Gift - 08/06/2016
"""

import random

TEST = ["A", "B", "C", "D", "E", "F"]

def ran_list(test=TEST):
	FOUND = []
	my_range = random.randint(1, len(TEST))
	print "Returning this many elements", my_range
	count = len(FOUND)
	for i in range(my_range):
		val = random.choice(TEST)
		FOUND.append(val)
		index = TEST.index(val)
		del TEST[index]
		#print TEST,val
	return FOUND

if __name__ == '__main__':
	print ran_list()


