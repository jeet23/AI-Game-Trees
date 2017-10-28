import random
import pdb
INFINITY = 10000
class Node(object):
	def __init__(self, data):
		self.data = data
		self.children = []
		self.copy_of_children = []
	def add_child(self, obj):
		self.children.append(obj)
		self.copy_of_children.append(obj)


def insertNodes(root, branchingFactor, height, delta, approx, tValue):
	branchingFactor = calculateBranchingFactorChance(branchingFactor)

	if height == 0 or root.data == INFINITY or branchingFactor == 0:
		return
	randomlyChosenDaughter = random.randint(0, branchingFactor-1)
	for branches in range(0, branchingFactor):
		negatedValue = -(tValue)
		level = height-1
		delta = random.randint(-approx, approx) if level != 0 else 0
		# pdb.set_trace()
		if branches == randomlyChosenDaughter:
			E = negatedValue + delta
			# print("Copying parent Negated node ----> Adding child node at height {} with T Value: {}".format(level, negatedValue))
			root.add_child(Node(E))
			insertNodes(root.children[branches], branchingFactor, level, delta, approx, negatedValue)
		else:
			randomNumberGreaterThanNegatedValue = random.randint(negatedValue+1,INFINITY+1)
			E = randomNumberGreaterThanNegatedValue + delta
			# print("Creating random node ----> Adding child node at height {} with T Value: {}".format(level, randomNumberGreaterThanNegatedValue))
			root.add_child(Node(E))
			insertNodes(root.children[branches], branchingFactor, level, delta, approx, randomNumberGreaterThanNegatedValue)



def printTree(root, branching, height):
	print("----------------------- T R E E ---------------------")
	print("----------------------- E Values ---------------------")
	for level in range(0, height + 1):
		# if level > 1:
		# 	branchingFactor = calculateBranchingFactorChance(branching)
		# else:
		# 	branchingFactor = branching
		# flagBranchChanged = True if branching != branchingFactor else False
		# TODO :: Printing tree with branching factor b+1 or b-1 is BUGGY right now. (>90% chance cases)

		printGivenLevel(root, level, branching)
		print("\n")

def printGivenLevel(root, level, branchingFactor):
	if root is None:
		return
	elif level == 0:
		print(root.data, end=" ")
	elif level > 0:
		for j in range(0, branchingFactor):				
			printGivenLevel(root.children[j], level-1, branchingFactor)
			print(end = "   ")

def calculateBranchingFactorChance(branching):
	if (90 < branching % 100 < 95):
		branchingFactor = branching + 1
	elif ( branching % 100 > 95):
		branchingFactor = branching - 1
	else:
		branchingFactor = branching
	return branchingFactor

def main():
	# Input branching factor b , Height h and approximation approx

	b = 2 #int(input("Enter Branching factor: "), 10)
	h = 3 #int(input("Enter Height: "), 10)
	approx = 5 #int(input("Enter Approximation: "), 10)

	tValue= random.randint(-2500,2500)
	delta = random.randint(-approx,approx)
	root = Node( tValue + delta)
	print("Adding root node at height {}: T Value: {}".format(h, tValue))
	insertNodes(root, b, h, delta, approx, tValue)
	printTree(root, b, h)

if __name__ == "__main__":
    main()
