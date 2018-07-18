"""
Author: Soumil Ramesh Kulkarni
Question: Write an algorithm such that if an element in NxM matrix is 0, its entire row and column are set to 0.
"""
import sys 
import unittest

class ZeroMatrix():
	def __init__(self, inp_matrix):
		self.inp_matrix = inp_matrix

	def create_zero_matrix(self):
		row_to_column_dict={}
		#print "Input Matrix is:"
		for i in range(len(self.inp_matrix)):
			#print self.inp_matrix[i]
			for j in range (len(self.inp_matrix[i])):
				if self.inp_matrix[i][j] == 0:
					#print "hey"
					row_to_column_dict[i] = j
		#print row_to_column_dict
		for i in range(len(self.inp_matrix)):
			if i in row_to_column_dict:
				for j in range(len(self.inp_matrix[i])):
					self.inp_matrix[i][j] = 0
		for i in row_to_column_dict:
			current_index = row_to_column_dict[i]
			for j in self.inp_matrix:
				j[current_index] = 0
					
		#print "Output Matrix is:"
		#for i in range(len(self.inp_matrix)):
		#	print self.inp_matrix[i]
		return self.inp_matrix

a = ZeroMatrix([[1,0,1,1],[2,2,2,2],[3,3,3,0],[4,4,4,4]])
a.create_zero_matrix()	
