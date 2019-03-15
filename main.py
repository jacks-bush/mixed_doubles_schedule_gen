import itertools

females = ['Lisa C', 'Lisa H', 'Jane', 'Margaret', 'Jeanine', 'Dorothy']
males = ['Dave', 'Jim', 'Evan', 'Tim', 'Scott', 'Lance']

femalePermutations = itertools.permutations(females, 2)
maleCombinations = itertools.combinations(males, 2)

allPossibleMatchCombinations = list(
    itertools.product(femalePermutations, maleCombinations))
print(allPossibleMatchCombinations)
print(len(allPossibleMatchCombinations))

# loop through creating days
# a day consists of 3 matches
# a match consists of one of the items in the allPossibleMatchCombinations list

# create copy of all possible list before going through algorithm
# for first match, pop random tuple off of list
# then in a while loop look for a tuple that does not have any of the players in the first tuple and remove it
# at this point we should know who should be in the final tuple. 
# the first tuple containing all the last 4 players (there will be more than one initially) is the one we should remove