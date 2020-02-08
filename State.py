num = [0]
class State(object):

    def __init__(self, missionaries, cannibals, boat,  level):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.level = level

        self.moves = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)] #(m, c)


    # pass True to count forward
    def successors(self):
        listChild = []
        if self.isGoalState():
            return listChild

        if self.boat:
            sgn = -1
        else:
            sgn = 1

        for i in self.moves:
            (m, c) = i
            self.addValidSuccessors(listChild, m, c, sgn)

        return listChild

    def addValidSuccessors(self, listChild, m, c, sgn):
        newState = State(self.missionaries + sgn * m, self.cannibals + sgn * c, self.boat + sgn, num[0] + 1)
        num[0] += 1
        if newState.isValidBound():
            listChild.append(newState)

    def isValidBound(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        return True

    def isValidDead(self):
        # then check whether missionaries outnumbered by cannibals in any shore
        if (self.cannibals > self.missionaries > 0) or (
                3 - self.cannibals > 3 - self.missionaries > 0):  # more cannibals then missionaries on original shore
            return False
        return True

    def isGoalState(self):
        return self.cannibals == 0 and self.missionaries == 0 and self.boat == 0
    
    def isSame(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat
    
    def notParent(self, other):
        return self.missionaries != other.missionaries or self.cannibals != other.cannibals or self.boat != other.boat
    
    def stateValue(self):
        return "<%d, %d, %d>" % (self.missionaries, self.cannibals, self.boat)

    def __repr__(self):
        return "<%d, %d, %d, %d>" % (self.missionaries, self.cannibals, self.boat, self.level)

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat and self.level == other.level

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __ne__(self, other):
        return not (self == other)


TERMINAL_STATE = State(-1, -1, 0, 0)
