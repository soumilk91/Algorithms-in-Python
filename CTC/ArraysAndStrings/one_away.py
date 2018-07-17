"""
Author: Soumil Ramesh Kulkarni
Question: There are 3 types of edits that can be performed on a string, 1) Insert a character, 2) Delete a character, 3) Replace a character. Given 2 strings, write a function to check if they are one edit away (or zero edit away)
 eg: pale, ple -> true
     pales, pale -> true
     pale, bale -> true
     pale, bake - > false
"""

import sys 
import unittest


class OneEditAway():
	def __init__(self, string1, string2):
		self.string1 = string1
		self.string2 = string2

	def check_if_one_edit_away(self):
		if ((len(self.string1) == len(self.string2)) or (len(self.string1) - len(self.string2) == 1) or (len(self.string1) - len(self.string2) == -1 )):
			edits = 0
			if len(self.string1) != len(self.string2):
				edits += 1
				if len(self.string1) < len(self.string2):
					loop_count = len(self.string1)
				else:
					loop_count = len(self.string2)
			else:
				loop_count = len(self.string1)
			for i in range (loop_count):
				if self.string1[i] == self.string2[i]:
					continue
				else:
					edits += 1
				if edits > 1:
					return False
			return True
		else:
			return False

class TestOneEditAway(unittest.TestCase):
	def test_correct_one_edit_away(self):
		a = OneEditAway("pale", "pal")
		self.assertTrue(a.check_if_one_edit_away())
	
	def test_identical_strings(self):
		a = OneEditAway("pale", "pale")
		self.assertTrue(a.check_if_one_edit_away())

	def test_wrong_order(self):
		a = OneEditAway("pale", "aple")
		self.assertFalse(a.check_if_one_edit_away())

	def test_multiple_edits_away_when_len_greater_than_one(self):
		a = OneEditAway("pale", "pa")
		self.assertFalse(a.check_if_one_edit_away())

	def test_multiple_edits_away_when_len_equal_to_one(self):
                a = OneEditAway("pale", "apl")
                self.assertFalse(a.check_if_one_edit_away())

if __name__ == "__main__":
	unittest.main()	
