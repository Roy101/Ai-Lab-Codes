turn = int(input("Enter turns for both:"))
branches = int(input("Number of notes from which the choice has to be made at certain time:"))
minimum, maximum = input("Minimum and Maximum value for the range of notes:").split()
minimum = int(minimum)
maximum = int(maximum)
depth = 2 * turn
leafNodes = branches ** depth
print("Depth:", depth)
print("Branch:", branches)
print("Terminal States (Leaf Nodes):", leafNodes)
import random as rnd

pruned = 0
l = []

for i in range(leafNodes):
    numbers = rnd.randint(minimum, maximum)
    l.append(numbers)
print("Random Generated Terminas are:", l)

LIST = []


def alphaBetaPruning_Algo(position, depth, alpha, beta, maximizingPlayer, n, track):
    if depth == 0:
        return n[position], track

    result = 0
    if maximizingPlayer:
        maxEval = -1000
        for i in range(0, branches):
            eval, track = alphaBetaPruning_Algo(position * branches + i, depth - 1, alpha, beta, False, n, track)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                track += 1
                break

        return maxEval, track
    else:
        minEval = 1000
        for i in range(0, branches):
            eval, track = alphaBetaPruning_Algo(position * branches + i, depth - 1, alpha, beta, True, n, track)

            minEval = min(minEval, eval)
            beta = min(beta, minEval)
            if beta <= alpha:
                track += 1
                break

        return minEval, track


def before_ABPAlgo(position, depth, alpha, beta, maximizingPlayer, n, track):
    if depth == 0:
        track += 1
        return n[position], track

    result = 0
    if maximizingPlayer:
        maxEval = alpha
        for i in range(0, branches):
            eval, track = before_ABPAlgo(position * branches + i, depth - 1, alpha, beta, False, n, track)
            maxEval = max(maxEval, eval)

        return maxEval, track
    else:
        minEval = beta
        for i in range(0, branches):
            eval, track = before_ABPAlgo(position * branches + i, depth - 1, alpha, beta, True, n, track)

            minEval = min(minEval, eval)

        return minEval, track


mini_witout, count = before_ABPAlgo(0, depth, -1000, 1000, True, l, 0)  ##Without alphabeta pruning
maxAmm, pruned_NUM = alphaBetaPruning_Algo(0, depth, -1000, 1000, True, l, 0)
print("Maximum ammount :", maxAmm)  # For Riyad
print("Before Alpha-beta Pruning:", count)

print("After Alpha-beta Pruning: ", count - pruned_NUM)
