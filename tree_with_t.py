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
	if height == 0 or root.data == INFINITY or branchingFactor == 0:
		return
	randomlyChosenDaughter = random.randint(0, branchingFactor-1)
	for branches in range(0, branchingFactor):
		negatedValue = -(tValue)
		level = height-1
		delta = random.randint(-approx, approx) if level != 0 else 0
		if negatedValue == INFINITY+1 or tValue == INFINITY+1:
			# print("-----------GAME WON POSITION--------at node E: {}, T : {}--------".format(root.data, tValue))
			return
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
	# 90% chances of b, 5% of b+1, 5% of b-1
	randomPercentage = random.randrange(0,100) 
	if randomPercentage < 90:
		b = branching
	elif 90 < randomPercentage < 95:
		b = branching + 1
	else:
		b = branching - 1
	return b

def main():
	# Input branching factor b , Height h and approximation approx

	b = 2 #int(input("Enter Branching factor: "), 10)
	h = 3 #int(input("Enter Height: "), 10)
	approx = 5 #int(input("Enter Approximation: "), 10)

	tValue= random.randint(-2500,2500)
	delta = random.randint(-approx,approx)
	root = Node( tValue + delta)
	b = calculateBranchingFactorChance(b)
	print("Adding root node at height {}: T Value: {}".format(h, tValue))
	insertNodes(root, b, h, delta, approx, tValue)
	printTree(root, b, h)

if __name__ == "__main__":
    main()
