"""
Author: Soumil Ramesh Kulkarni
Functions Covered: 
1) Insert a Node in the BST ---- O(log n)
2) Search a Node in the BST ---- O(log n)
3) Find the Minimum element in the BST ---- O(log n)
4) Find the MAximum element in the BST ---- O(log n)
5) Find the Height of the Binary Search Tree 
6) DFS (Preorder Traversal)
7) DFS (Postorder Traversal)
8) DFS (Inorder Traversal)
9) BFS (Level Order Traversal)
"""
import sys 


class Node():
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None


class BST_Operations():
	def __init__(self):
		self.root = None

	def insert_new_node(self, data, ref_node):
		if ref_node == None:
			new_node = Node()
			new_node.data = data
			self.root = new_node
		else:
			new_node = Node()
			new_node.data = data
			if data <= ref_node.data:
				if ref_node.left == None:
					ref_node.left = new_node
				else:
					self.insert_new_node(data, ref_node.left)
			else:
				if ref_node.right == None:
					ref_node.right = new_node
				else:
					self.insert_new_node(data, ref_node.right)

	def search_node(self, data, ref_node):
		if ref_node == None:
			print "The BST is Empty"
		else:
			temp = ref_node
			while(temp != None):
				if temp.data == data:
					print "The Element %s is present in the BST" %str(data)
					return
				elif temp.data < data:
					temp = temp.right
				else:
					temp = temp.left
		print "The Element %s is not present in the BST " %str(data)
	
	def find_minimum_element(self, ref_node):
		if ref_node == None:
			print "The BST is empty"
		else:
			temp = ref_node
			while (temp.left != None):
				temp = temp.left
			print "The minimum element in the BST is: %s" %str(temp.data)

	def find_maximum_element(self, ref_node):
		if ref_node == None:
                        print "The BST is empty"
                else:
                        temp = ref_node
                        while (temp.right != None):
                                temp = temp.right
                        print "The maximum element in the BST is: %s" %str(temp.data)

	def height_of_the_bst(self, ref_node):
		temp = ref_node
		if temp == None:
			return -1
		left_sub_tree = self.height_of_the_bst(temp.left)
		right_sub_tree = self.height_of_the_bst(temp.right)
		return max(left_sub_tree, right_sub_tree) + 1

	def preorder_traversal (self, ref_node):
		temp = ref_node
		if temp == None:
			return
		print temp.data
		self.preorder_traversal(temp.left)
		self.preorder_traversal(temp.right)

	def inorder_traversal (self, ref_node):
		temp = ref_node
		if temp == None:
			return 
		self.inorder_traversal(temp.left)
		print temp.data
		self.inorder_traversal(temp.right)

	def postorder_traversal (self, ref_node):
		temp =ref_node
		if temp == None:
			return 
		self.postorder_traversal(temp.left)
		self.postorder_traversal(temp.right)
		print temp.data

	def level_order_traversal(self, ref_node):
		temp = ref_node
		fifo = [temp]
		while len(fifo) != 0:
			temp1 = fifo[0]
			if temp1.left != None:
				fifo.append(temp1.left)
			if temp1.right != None:
				fifo.append(temp1.right)
			print temp1.data
			del fifo[0]
 

def main():
	bst1 = BST_Operations()
	bst1.find_minimum_element(bst1.root)
	bst1.insert_new_node(15,bst1.root)
	bst1.insert_new_node(10,bst1.root)
	bst1.insert_new_node(20,bst1.root)
	bst1.insert_new_node(8,bst1.root)
	bst1.insert_new_node(13,bst1.root)
	bst1.insert_new_node(7,bst1.root)
	bst1.insert_new_node(11,bst1.root)
	bst1.insert_new_node(17,bst1.root)
	bst1.insert_new_node(28,bst1.root)
	bst1.search_node(15,bst1.root)
	bst1.search_node(20,bst1.root)
	bst1.search_node(25,bst1.root)
	bst1.search_node(10,bst1.root)
	bst1.find_minimum_element(bst1.root)
	bst1.find_maximum_element(bst1.root)	
	#print bst1.height_of_the_bst(bst1.root)
	bst1.insert_new_node(12,bst1.root)
	#print bst1.height_of_the_bst(bst1.root)
	#bst1.inorder_traversal(bst1.root)
	bst1.level_order_traversal(bst1.root)

if __name__ == '__main__':
	main()
