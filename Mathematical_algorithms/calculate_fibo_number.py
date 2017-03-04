"""
@ Author : Soumil Kulkarni

This file contains various methods related to problems on FIBO Series

"""
import sys 

# Method to calculate the fibo number recursively 
def calculate_fibo_number_recursive(num):
	if num < 0:
		print "Input incorrect"
	elif num == 0 :
		return 0
	elif num == 1 :
		return 1
	else :
		return (calculate_fibo_number_recursive(num - 1) + calculate_fibo_number_recursive(num -2 ))

# Method to calculate fibo number using a list 
def calculate_fibo_number_with_list(num):
	num_list =[0,1]
	if num < 0:
		print "Input incorrect"
	elif num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		n = num - 2
		pointer_1 = 0
		poniter_2 = 1
		for i in range(n):
			num_list.append(num_list[pointer_1] + num_list[poniter_2])
			pointer_1 += 1
			poniter_2 += 1
		return (num_list[pointer_1] + num_list[poniter_2])


# Method to reduce the space complexity in the previous soultion. 
# Hint :  All you need is the last 2 digits, so just store the last 2 digits and neglect the others. Space complexity will be reduced from O(N) to O(1)

def calulate_fibo_number_with_list_improved(num):
	num_list = [0,1]
	if num < 0:
		print "Input incorrect"
	elif num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		n = num - 2
		pointer_1 = 0
		poniter_2 = 1
		for i in range (n):
			temp =  num_list[0] + num_list[1]
			num_list[0] = num_list[1]
			num_list[1] = temp
		return (num_list[0] + num_list[1])



