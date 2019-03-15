import itertools
import random


def main():
    females = ['Lisa C', 'Lisa H', 'Jane', 'Margaret', 'Jeanine', 'Dorothy']
    males = ['Dave', 'Jim', 'Evan', 'Tim', 'Scott', 'Lance']

    femalePermutations = itertools.permutations(females, 2)
    maleCombinations = itertools.combinations(males, 2)

    allPossibleMatchCombinations = list(
        itertools.product(femalePermutations, maleCombinations))
    print(len(allPossibleMatchCombinations))

    # loop through creating days
    # a day consists of 3 matches
    # a match consists of one of the items in the allPossibleMatchCombinations list

    # create copy of all possible matches before going through algorithm
    days = []
    while True:
        # for first match, pop random tuple off of list
        availableMatches = allPossibleMatchCombinations.copy()
        currentDayMatches = []
        currentDayMatches.append(availableMatches.pop(
            random.randint(0, len(availableMatches) - 1)))

        # filter the remaining matches so they do not contain any of players in the first match
        availableMatches = [match for match in availableMatches if matchDoesNotContainPlayersInTuple(
            currentDayMatches[0], match)]
        # grab random match in available matches
        currentDayMatches.append(availableMatches.pop(
            random.randint(0, len(availableMatches) - 1)))

        # at this point we should know who should be in the final tuple.
        # the first tuple containing all the last 4 players (there will be more than one initially) is the one we should remove
        # filter the remaining matches so they do not contain any of players in the first match
        availableMatches = [match for match in availableMatches if matchDoesNotContainPlayersInTuple(
            (currentDayMatches[0], currentDayMatches[1]), match)]

        if(len(availableMatches) == 0):
            print(len(days))
            continue

        # grab random match in available matches
        currentDayMatches.append(availableMatches.pop(
            random.randint(0, len(availableMatches) - 1)))

        # add list of matches to day
        days.append(currentDayMatches)
        # remove matches from all available matches
        for match in currentDayMatches:
            allPossibleMatchCombinations.remove(match)

        if (len(allPossibleMatchCombinations)) == 0:
            break

    print(days)


def matchDoesNotContainPlayersInTuple(previousMatchesTuple, currentMatchTuple):
    currentList = stripTupleofTuplesDownToList(currentMatchTuple)
    previousList = stripTupleofTuplesDownToList(previousMatchesTuple)
    return not any([person for person in currentList if person in previousList])


def stripTupleofTuplesDownToList(obj):
    # make sure object is tuple
    if (not isinstance(obj, tuple)):
        return []

    # check if objects in tuple are tuples
    # if objects in tuple are not tuples, return the contents of the tuple as a list
    if (not isinstance(obj[0], tuple)):
        return list(obj)

    # if objects in tuple are tuples, then loop through tuple and call this function on them, adding results together into one list
    returnList = []
    for tup in obj:
        returnList += stripTupleofTuplesDownToList(tup)
    return returnList


main()
