#7_bst.py

class Node:
	def __init__(self, val):
			self.val = val
			self.left = None
			self.right = None
	
def toBST(arr):
	
	if not arr:
		return None

	mid = (len(arr)) // 2
	root = Node(arr[mid])
	
	root.left = toBST(arr[:mid])
	root.right = toBST(arr[mid+1:])
	return root

def preOrder(node):
	if not node:
		return
	
	print(node.val, end = " ")    
	preOrder(node.left)
	preOrder(node.right)

if __name__ == "__main__":

    Strings = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
				"W", "X", "Y", "Z"]
    root = toBST(Strings)
    print("The Original String: ", " ".join(Strings))
    print("PreOrder Traversal of constructed BST: ", end = "")
    preOrder(root)