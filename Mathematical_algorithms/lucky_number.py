'''
What is a Lucky Number ??? 

Example :
---------------
Take the set of integers
1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,

First, delete every second number, we get following reduced set.
1,3,5,7,9,11,13,15,17,19,--

Now, delete every third number, we get
1, 3, 7, 9, 13, 15, 19,--

Continue this process indefinitely--
Any number that does NOT get deleted due to above process is called LUCKY.

Therefore, set of lucky numbers is 1, 3, 7, 13,---

Now, given an integer n, write a function to say whether this number is lucky or not.

'''

import sys

def isLucky(number):
	if number % 2 == 0:
		print "Not a lucky Number"
		return False
	else:
		num_list = []
		for i in range (1,number+1):
			num_list.append(i)
		itr = 2
		while (itr < len(num_list)):
			tmp_list = []
			for i in range(len(num_list)):
				if ((i + 1)%itr != 0):
					tmp_list.append(num_list[i])
			num_list = tmp_list
			itr += 1

		if number in num_list:
			print num_list
			print "It is a luck Number"
		else:
			print num_list
			print "Not a luck number"


try:
	inp = int(raw_input("Enter an integer: "))
	isLucky(inp)
except Exception as e:
	print "Wrong input. \n EXCEPTION: %s"%e
