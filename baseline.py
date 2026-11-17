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
            if len(SC[i]) == CactusCounter:
                solution.append(S[i])
                for tree in SO[i]:
                    if tree in trees:
                        trees.remove(tree)
                    if not trees:
                        return solution  
        CactusCounter += 1





 # Testing


# Test 1: Modified example from the project doc

a1 = [2,6,11]
a2 = [4,8,14]
a3 = [3,7,12]
a4 = [3, 2, 1]

expectedOutput = [12, 3]
if cover(a1, a2, a3, a4) != expectedOutput:
    print("TEST 1 ERROR: algorithm is not providing correct output.")



# Test 3: Example I made up

a1 = [3,5]
a2 = [2,6,7]
a3 = [1,4,8]
a4 = [5, 1, 5]

expectedOutput = [4]
if cover(a1,a2,a3,a4) != expectedOutput:
    print("TEST 2 ERROR: algorithm is not providing correct output.")


# Test 3: Example with empty solution

a1 = [1,2,4]
a2 = [3,6,9]
a3 = []
a4 = [1,2,3]

expectedOutput = []
if cover(a1,a2,a3,a4) != expectedOutput:
    print("TEST 3 ERROR: algorithm is not providing correct output.")

# Test 4: Another example I made up

a1 = [2,7]
a2 = [1,4]
a3 = [3,6]
a4 = [2,1]

expectedOutput = [6,3]

if cover(a1,a2,a3,a4) != expectedOutput:
    print("TEST 4 ERROR: algorithm is not providing correct output.")


# Test 5: Slightly larger inputs

a1 = [4,8,15]
a2 = [2,3,11,12,17,20]
a3 = [1,5,9,14,18]
a4 = [3,1,2,1,4]

expectedOutput = [5,14,9]

if cover(a1,a2,a3,a4) != expectedOutput:
    print("TEST 5 ERROR: algorithm is not providing correct output.")