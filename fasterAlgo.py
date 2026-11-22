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
                for tree in SO[i]:
                    if tree in trees:
                        trees.remove(tree)
                    if not trees:
                        return solution  
        CactusCounter += 1