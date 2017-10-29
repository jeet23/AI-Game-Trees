import random
from tree_with_t import *
from PVA_negamax import orderMoves

alpha = -10000
beta = 10000
iterativeDeepening = 5 #Based on resources available
heightChecked = 0
numberOfStaticEvaluation = 0
numberOfStaticEvaluation_with_pva = 0

def pvs(root, branching, height, alpha, beta, Modified):
	global heightChecked, numberOfStaticEvaluation, numberOfStaticEvaluation_with_pva
	if len(root.children) == 0 or heightChecked == iterativeDeepening:
		if Modified:
			numberOfStaticEvaluation_with_pva += 1
		else:
			numberOfStaticEvaluation += 1
		return root.data
	else:
		for m in range(0, branching):
			if Modified:
				root = orderMoves(root)
			if m == 0:
				score = -pvs(root.children[m], branching, height - 1,
							 -beta, -alpha, Modified)
			else:
				score = -pvs(root.children[m], branching, height - 1, 
							-alpha -1 , -alpha, Modified)
				if alpha < score < beta:
					score = -pvs(root.children[m], branching, height-1, 
								-beta, -score, Modified)
			alpha = max(alpha, score)
			if alpha > beta:
				break
		heightChecked += 1
	return alpha


def main():
	# Input branching factor b , Height h and approximation approx

	b = 2 #int(input("Enter Branching factor: "), 10)
	h = 4 #int(input("Enter Height: "), 10)
	approx = 5 #int(input("Enter Approximation: "), 10)

	tValue= random.randint(-2500,2500)
	delta = random.randint(-approx,approx)
	root = Node( tValue + delta)
	b = calculateBranchingFactorChance(b)
	print("Adding root node at height {}: T Value: {}".format(h, tValue))
	insertNodes(root, b, h, delta, approx, tValue)
	printTree(root, b, h)

	pvsValue = pvs(root, b, h, alpha, beta, False)
	print("PVS value without re-ordering is : {} ".format(pvsValue))
	print("numberOfStaticEvaluation without re-ordering is : {} ".\
			format(numberOfStaticEvaluation))

	pvsValue1 = pvs(root, b, h, alpha, beta, True)
	print("PVS value with re-ordering is : {} ".format(pvsValue1))
	print("numberOfStaticEvaluation with re-ordering is : {} ".\
			format(numberOfStaticEvaluation_with_pva))

if __name__ == "__main__":
    main()
