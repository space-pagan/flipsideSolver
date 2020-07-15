class FlipSide:
    def __init__(self, state, solvePath="Self", parent=None):
        if len(state) == 10:
            self.state = state
            self.solvePath = solvePath
            self.parent = parent
        else:
            raise wrongArgumentException

    # needs to do One Thing Well
    @staticmethod
    def solveWithBFS(testPerm):
        # Setup
        found = set([str([1,2,3,4,5,6,7,8,9,0])])
        foundAtDepth = [[FlipSide([1,2,3,4,5,6,7,8,9,0])]]
        for i in range(11):
            foundAtDepth.append([])

        # Edge case
        if testPerm.isSolution():
            return testPerm

        # [1,2,3,4,5,6,7,8,9,0] is already found
        print("Found at depth  0:\t\t\t\t 1")

        # maximum depth = 11 from empirical testing
        for thisDepth in range(1,12):
            for parent in foundAtDepth[thisDepth-1]:
                childlist = parent.getCurrentStatePermutations()
                childset = set([str(c.state) for c in childlist])
                newchildren = childset.difference(found)
                found.update(newchildren)
                for child in childlist:
                    if str(child.state) in newchildren:
                        foundAtDepth[thisDepth].append(child)
                if str(testPerm.state) in newchildren:
                    for child in childlist:
                        if child.state == testPerm.state:
                            print("Found at depth {:2d}".format(thisDepth) + ":\t\t\t\t", len(foundAtDepth[thisDepth]))
                            print("Found solution at depth {:2d}".format(thisDepth) + "!\tTotal searched:\t",len(found), "/ 3628800 (~{:3.1f}%)".format(100*len(found)/3628800))
                            return child
            print("Found at depth {:2d}".format(thisDepth) + ":\t\t\t\t", len(foundAtDepth[thisDepth]))
        print("No solution found.\t\tTotal searched:\t",len(found))
        print()
        print("Last found permutation is " + str(foundAtDepth[-1][-1].state))
        return foundAtDepth[-1][-1]

    def solvePathConstructor(self, startingpoint=False):
        out = self.solvePath
        if self.parent is not None:
            if startingpoint:
                out = "Self -> " + out
            return out + " -> " + self.parent.solvePathConstructor()
        if self.isSolution():
            return "Solved!"
        return "Solution Path Broken -> |"

    def getPermuteI(self, i):
        [A,B,C,D,E,F,G,H,I,J] = self.state
        if i < 1 or i > 9:
            raise wrongArgumentException
        if i == 1:
            return FlipSide([A,B,H,I,J,F,G,C,D,E], solvePath="(0,0)", parent=self)
        if i == 2:
            return FlipSide([A,H,I,J,E,F,G,B,C,D], solvePath="(1,0)", parent=self)
        if i == 3:
            return FlipSide([H,I,J,D,E,F,G,A,B,C], solvePath="(2,0)", parent=self)
        if i == 4:
            return FlipSide([A,B,G,H,I,F,C,D,E,J], solvePath="(0,1)", parent=self)
        if i == 5:
            return FlipSide([A,G,H,I,E,F,B,C,D,J], solvePath="(1,1)", parent=self)
        if i == 6:
            return FlipSide([G,H,I,D,E,F,A,B,C,J], solvePath="(2,1)", parent=self)
        if i == 7:
            return FlipSide([A,B,F,G,H,C,D,E,I,J], solvePath="(0,2)", parent=self)
        if i == 8:
            return FlipSide([A,F,G,H,E,B,C,D,I,J], solvePath="(1,2)", parent=self)
        if i == 9:
            return FlipSide([F,G,H,D,E,A,B,C,I,J], solvePath="(2,2)", parent=self)

    def getCurrentStatePermutations(self):
        permutations = []
        for i in range(1,10):
            permutations.append(self.getPermuteI(i))
        return permutations

    def isSolution(self):
        return self.state == [1,2,3,4,5,6,7,8,9,0]

class wrongArgumentException(Exception):
    pass

def main():
    solution = FlipSide.solveWithBFS(FlipSide([1,9,2,8,3,7,4,6,5,0]))
    print("\n")
    print("Solve Path for " + str(solution.state) + ":")
    print(solution.solvePathConstructor(startingpoint=True))

if __name__ == '__main__':
    main()
