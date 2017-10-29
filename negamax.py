import random
from tree_with_t import *

alpha = -10000
beta = 10000

numberOfStaticEvaluation = 0
iterativeDeepening = 5 #User has to input
heightChecked = 0
Modified = False

def negamax(root, branching, height, alpha, beta):
	global heightChecked, iterativeDeepening
	# Check if leaf node or Iterative deepening reached limit
	if len(root.children) == 0 or heightChecked == iterativeDeepening:
		global numberOfStaticEvaluation
		numberOfStaticEvaluation += 1
		return root.data
	else:
		for move in range(0, branching):
			# Implement OrderMoves(root.children) here if parameter Modified == True
			# orderMoves(root.children)
			newNode = root.children[move]
			temp = -(negamax(newNode, branching, height - 1, -beta, -alpha))
			# Do nothing ---> destroy newNode
			if temp > beta:
				return temp
			alpha = max(temp, alpha)
		heightChecked += 1 # Next level being checked now
	return alpha


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


	negamaxValue = negamax(root, b, h, alpha, beta)
	print("Negamax value is : {} ".format(negamaxValue))
	print("numberOfStaticEvaluation is : {} ".format(numberOfStaticEvaluation))

if __name__ == "__main__":
    main()
