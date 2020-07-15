class FlipSide:
    def __init__(self, state, solvePath="Self", parent=None):
        if len(state) == 10:
            self.state = state
            self.solvePath = solvePath
            self.parent = parent
        else:
            raise wrongArgumentException

    @staticmethod
    def getUniqueChildrenAndUpdateFound(found, parent):
        unique = []
        childlist = parent.getCurrentStatePermutations()
        newchildren = set([c.state for c in childlist]).difference(found)
        found.update(newchildren)
        for child in childlist:
            if child.state in newchildren:
                unique.append(child)
        return unique

    @staticmethod
    def printSolutionStats(found, thisDepth):
        print("Found solution at depth {:2d}!".format(thisDepth), end="")
        print("Total searched: {:7d}".format(len(found)).rjust(29), end="")
        print(" / 3628800 (~{:3.1f}%)".format(100*len(found)/3628800))

    def solveWithBFS(self):
        found = set(["1234567890"])
        parents = [FlipSide("1234567890")]
        maxDepth = 11 # from empirical testing

        if self.isSolution(): # Edge case
            return self

        # 1234567890 is already found
        print("Found at depth  0:" + "{:7d}".format(len(parents)).rjust(38))
        return self.solveWithBFSHelper(found, parents, maxDepth)

    def solveWithBFSHelper(self, found, parents, maxDepth):
        for thisDepth in range(1, maxDepth+1):
            parents, solution = self.searchDepth(found, parents)
            print("Found at depth {:2d}:".format(thisDepth) + "{:7d}".format(len(parents)).rjust(38))
            if solution:
                FlipSide.printSolutionStats(found, thisDepth)
                return solution
        print("No solution found." + "Total searched: {:7d}".format(len(found)).rjust(38))
        return self

    def searchDepth(self, found, parents):
        children = []
        for p in parents:
            unique = FlipSide.getUniqueChildrenAndUpdateFound(found, p)
            children += unique
            match = [child for child in unique if self.state == child.state]
            if len(match):
                return children, match[0]
        return children, None

    def solvePathConstructor(self, startingpoint=False):
        out = self.solvePath
        if startingpoint:
            out = "Self -> " + out
        if self.parent is not None:
            return out + " -> " + self.parent.solvePathConstructor()
        if self.isSolution():
            return "Solved!"
        return "Solution Path Broken -> |"

    def getPermuteI(self, i):
        if i < 1 or i > 9:
            raise wrongArgumentException
        [A,B,C,D,E,F,G,H,I,J] = self.state
        if i == 1:
            return FlipSide(''.join([A,B,H,I,J,F,G,C,D,E]), solvePath="(0,0)", parent=self)
        if i == 2:
            return FlipSide(''.join([A,H,I,J,E,F,G,B,C,D]), solvePath="(1,0)", parent=self)
        if i == 3:
            return FlipSide(''.join([H,I,J,D,E,F,G,A,B,C]), solvePath="(2,0)", parent=self)
        if i == 4:
            return FlipSide(''.join([A,B,G,H,I,F,C,D,E,J]), solvePath="(0,1)", parent=self)
        if i == 5:
            return FlipSide(''.join([A,G,H,I,E,F,B,C,D,J]), solvePath="(1,1)", parent=self)
        if i == 6:
            return FlipSide(''.join([G,H,I,D,E,F,A,B,C,J]), solvePath="(2,1)", parent=self)
        if i == 7:
            return FlipSide(''.join([A,B,F,G,H,C,D,E,I,J]), solvePath="(0,2)", parent=self)
        if i == 8:
            return FlipSide(''.join([A,F,G,H,E,B,C,D,I,J]), solvePath="(1,2)", parent=self)
        if i == 9:
            return FlipSide(''.join([F,G,H,D,E,A,B,C,I,J]), solvePath="(2,2)", parent=self)

    def getCurrentStatePermutations(self):
        permutations = []
        for i in range(1,10):
            permutations.append(self.getPermuteI(i))
        return permutations

    def isSolution(self):
        return self.state == "1234567890"

    def prettyPrint(self):
        out = []
        for pos in self.state:
            out.append(int(pos))
        return str(out)

class wrongArgumentException(Exception):
    pass

def main():
    solution = FlipSide("1928374650").solveWithBFS()
    print("\n")
    print("Solve Path for " + solution.prettyPrint() + ":")
    print(solution.solvePathConstructor(startingpoint=True))

if __name__ == '__main__':
    main()
