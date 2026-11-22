# Ochwar Okuori, wos583, #11344666, CMPT-360

"""algorithm for option 4 of the algorithm design module.
    Inputs:
    O - an array of positive integers representing placement of trees
    C - an array of positive integers representing placement of cacti
    S - an array of positive integers representing placement of sprinklers
    R - an array of positive integers representing radius of each sprinkler
    
    Output: an array of sprinklers that water all trees and the least amount of cacti
    """

def cover(O, C, S, R):
    # if no sprinklers in S, there is no solution
    if not S:
        return []

    # e is meant to contain the range of each sprinkler
    e = []
    for i in range(0,len(S)):
        e.append((S[i]-R[i], S[i]+R[i]))

    # SC is meant to list all cacti watered by each sprinkler    
    SC = []
    for i in range(0, len(e)):
        SC.append([])
        for cactus in C:
            if e[i][0] <= cactus and cactus <= e[i][1]:
                SC[i].append(cactus)


    # SO is meant to list all trees watered by each sprinkler            
    SO = []
    for i in range(0, len(e)):
        SO.append([])
        for tree in O:
            if e[i][0] <= tree and tree <= e[i][1]:
                SO[i].append(tree)


    trees = O[:]
    CactusCounter = 0
    solution = []

    while len(trees) > 0:
        # iterate through SC, picking the sprinklers that cover the least cacti. Add that sprinkler
        # to the solution set and cross off all the trees it covers as well. Keep going until all
        # trees have been watered
        for i in range(0, len(SC)):
            if len(SC[i]) == CactusCounter and SO[i]: 
                solution.append(S[i])
                if SO[i][0] in trees:
                    trees.remove(SO[i][0])
                if not trees:
                    return solution  
        CactusCounter += 1


# Testing


# Test 1: 

a1 = [3,6]
a2 = [5,10,11]
a3 = [2,4,7,9]
a4 = [1,1,1,1]

expectedOutput = [2,7]
if cover(a1, a2, a3, a4) != expectedOutput:
    print("TEST 1 ERROR: algorithm is not providing correct output.")


# Test 2:

a1 = [3,9,12]
a2 = [5,7,11]
a3 = [1,2,6,8,10,13]
a4 = [1,1,1,1,1,1]

expectedOutput = [2,13,8]
if cover(a1, a2, a3, a4) != expectedOutput:
    print("TEST 2 ERROR: algorithm is not providing correct output.")


# Test 3:

a1 = [2,15,37,41,50,79]
a2 = [4,13,30,36,40,56]
a3 = [1,14,21,36,42,51,80]
a4 = [1,1,1,1,1,1,1]

expectedOutput = [1, 42, 51, 80, 14, 36]
if cover(a1, a2, a3, a4) != expectedOutput:
    print("TEST 3 ERROR: algorithm is not providing correct output.")