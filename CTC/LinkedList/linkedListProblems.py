"""
Author: Soumil Ramesh Kulkarni
Date: Sun Jul 22 2018
"""

class Node():
	def __init__(self, data):
		self.data = data 
		self.next_node = None

class Basic_Linked_List_Functions():
	def __init__(self):
		self.head = None
	# Prints a all the contents of a singly Linked List in a list format 
	def print_singly_linked_list(self):
		if self.head == None:
			print "Singly Linked List is Empty"
		else:
			temp = self.head
			ret_list = []
			while temp != None:
				ret_list.append(temp.data)
				temp = temp.next_node
			print ret_list

	# Addition of a new node at the start of the singly linked list 
	def add_node_at_the_start(self, data):
		if self.head == None:
			new_node = Node(data)
			self.head = new_node
		else:
			new_node = Node(data)
			new_node.next_node = self.head 
			self.head = new_node

	# Addition of a new node at the end of a singly linked list 
	def add_node_at_the_end(self, data):
		if self.head == None:
			new_node = Node(data)
			self.head = new_node
		else:
			new_node = Node(data)
			temp = self.head 
			while temp.next_node != None:
				temp = temp.next_node
			temp.next_node = new_node

	# Deletion of node at the start of the Singly Linked List 
	def delete_node_at_the_start(self):
		if self.head == None:
			print "Linked List already empty"
		else:
			self.head = self.head.next_node
	
	# Deletion of a node at the end of the Singly Linked List
	def delete_node_at_the_end(self):
		if self.head == None:
			print "Linked List already empty"
		else:
			temp1= None
			temp2= self.head
			while temp2.next_node != None:
				temp1= temp2
				temp2 = temp2.next_node
			temp1.next_node = None
	
	# Function to Reverse a Singly Linked List
	def reverse_singly_linked_list(self):
		if self.head == None:
			print "The Linked List is already empty"
		else:
			prev = None
			curr = self.head
			while curr != None:
				ne_node = curr.next_node
				curr.next_node = prev
				prev = curr
				curr = ne_node
			self.head = prev
	

	# Have to redo this function
	# Remove all the duplicates from a Singly Linked List
	def remove_duplicates_from_singly_linkedlist(self):
		if self.head == None:
			print "Linked List is Empty "
		else:
			temp = self.head
			while temp.next_node != None:
				temp1 = temp
				temp2 = temp1.next_node
				#print temp2.data
				if temp2 != None:
					while temp1.data == temp2.data:
						temp2 = temp2.next_node
				temp1.next_node = temp2
				while temp2 != None:
					if temp2.data == temp.data:
						temp1.next_node = temp2.next_node
					temp1 = temp1.next_node
					temp2 = temp2.next_node
				temp = temp.next_node
							
	# Given a Singly Linked List and a integer(k), return the last "k" elemets of that linked list 
	def return_the_last_k_elements_of_a_linked_list(self, lastk):
		ret_list = []
		temp = self.head 
		for i in range (lastk - 1):
			if temp.next_node == None:
				print "Not Enough Nodes present in the LinkedList"
				return
			temp = temp.next_node
		temp1 = self.head
		while (temp.next_node != None):
			temp = temp.next_node
			temp1 = temp1.next_node
		while (temp1 != None):
			ret_list.append(temp1.data)
			temp1 = temp1.next_node
		print ret_list

# A basic implementation of a Stack. This will be used in the function written below which is written to find if the singly linked list is a Palindrome 
class basicStackFunctions():
	def __init__(self):
		self.stack_list = []
	
	def push_ele (self, element):
		self.stack_list.append(element)

	def pop_ele (self):
		self.stack_list.pop()
		
	def top_ele (self):
		return self.stack_list[(len(self.stack_list) - 1)]

class functionsOnLinkedList():
	
	# Given a pointer to the node from a singly linked list (not the start or the end node of the linked list ), delete that node. 
	def delete_the_middle_node(self, node_ref):
		temp = node_ref
		temp1 = node_ref.next_node
		while temp1.next_node != None:
			temp.data = temp1.data
			temp = temp.next_node
			temp1 = temp1.next_node
		temp.next_node = None		

	# Given a singly linked list, find out if that linked list is a palindrome. 
	def if_linkedlist_palindrome(self, node_ref):
		slow_runner = node_ref
		fast_runner = node_ref
		while (fast_runner != None):
			if fast_runner.next_node != None:
				fast_runner = fast_runner.next_node.next_node
				slow_runner = slow_runner.next_node
			elif fast_runner.next_node == None:
				break
		temp1 = node_ref
		temp_stack = basicStackFunctions()
		while (temp1.next_node != slow_runner.next_node):
			temp_stack.push_ele(temp1.data)
			temp1 = temp1.next_node
		if fast_runner == None:
			pass
		else:
			slow_runner = slow_runner.next_node
		while (slow_runner != None):
			top_stack = temp_stack.top_ele()
			if slow_runner.data == top_stack:
				temp_stack.pop_ele()
				slow_runner = slow_runner.next_node
			else:
				return False
		return True

	# Given a singly linked list, find out if that linked list is a palindrome. (method 2: where we are reversing the given linked list and then comparing it to the given linked list )
	def if_linkedlist_palindrome_using_ll_reversal(self, node_ref):
		current_ll_elements = []
		temp = node_ref
		while temp != None:
			current_ll_elements.append(temp.data)
			temp = temp.next_node
		print current_ll_elements
		start_point = 0
		end_point = len(current_ll_elements ) - 1
		while (start_point < end_point):
			if current_ll_elements[start_point] == current_ll_elements[end_point]:
				start_point += 1
				end_point -= 1
			else:
				return False
		return True	

	# Given 2 Singly Linked List, find out if they ever intersect
	def find_if_the_2_given_linkedlists_intersect(self, ll_ref_1, ll_ref_2):
		temp1 = ll_ref_1
		temp2 = ll_ref_2
		len_of_ll_ref_1 = 0
		len_of_ll_ref_2	= 0
		while temp1.next_node != None:
			len_of_ll_ref_1 += 1
			temp1 = temp1.next_node
		while temp2.next_node != None:
			len_of_ll_ref_2 += 1
			temp2 = temp2.next_node
		if temp1 != temp2:
			return False
		else:
			if len_of_ll_ref_1 > len_of_ll_ref_2:
				diff_len = len_of_ll_ref_1 - len_of_ll_ref_2
				temp1 = ll_ref_1
				for i in range (diff_len):
					temp1 = temp1.next_node
				temp2 = ll_ref_2
			elif len_of_ll_ref_2 > len_of_ll_ref_1:
				diff_len = len_of_ll_ref_2 - len_of_ll_ref_1
				temp1 = ll_ref_2
				for i in range (diff_len):
					temp1 = temp1.next_node
				temp2 = ll_ref_1
			else:
				temp1 = ll_ref_1
				temp2 = ll_ref_2
			while (temp1.next_node ! = None):
				if temp1.next_node == temp2.next_node:
					return True
				else:
					temp1= temp1.next_node
					temp2= temp2.next_node
			return False
			
		
	# Given a Circular Linked List, find out the point at which the loop starts. 	
	def find_the_loop_in_the_circular_linked_list(self, ll_ref):
		slow_runner = ll_ref
		fast_runner = ll_ref
		while (fast_runner.next_node != slow_runner.next_node):
			if ((fast_runner.next_node == None) or (fast_runner == None)):
				return False
			slow_runner = slow_runner.next_node
			fast_runner = fast_runner.next_node.next_node
		temp1 = slow_runner
		temp2 = ll_ref
		while (temp1.next_node != temp2.next_node):
			temp1 = temp1.next_node
			temp2 = temp2.next_node
		return temp1

