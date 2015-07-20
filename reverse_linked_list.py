#reverse linked list

class Node:
	def __init__(self, data):
		self.data = None
		self.next = None

# class LinkedList:

#step through or traverse the linked list
#for each node, create a new pointer going backwards pointing to previous node .last
#return a linked list such that node.next is node.last

def reverse(node):
	while node.next is not None:
		temp = node.data
		next_node = node.next
		next_node.last = temp
		node = next_node

		return node

# this will give us back c, where node.last is = 
	while node.last is not None:
		node.next = node.last
		node = node.next
	
	node.next = None	
	return head 

if __name__=="__main__":
	Node(5)
	reverse(5)