from enum import Enum

class Corner(Enum):
    URF = 0
    UFL = 1
    ULB = 2
    UBR = 3
    DFR = 4
    DLF = 5
    DBL = 6
    DRB = 7

class Edge(Enum):
    UF = 0
    UL = 1
    UB = 2
    UR = 3
    RF = 4
    FL = 5
    LB = 6
    BR = 7
    DF = 8
    DL = 9
    DB = 10
    DR = 11

class Cube:
    # See http://kociemba.org/math/coordlevel.htm for cube representation
    # Base 3 representation of corner orientations, 0 <= cornerOrientation < 3^7
    cornerOrientation = 0
    # Base 2 representation of edge orientations, 0 <= edgeOrientatio < 2^11
    edgeOrientation = 0
    # Variable base representation of corner permutations, 0 <= cornerPermutation <= 8!
    cornerPermutation = 0
    # Variable base representation of edge permutations, 0 <= edgePermutation <= 12!
    edgePermutation = 0

    def __init__(self):

    def getCornerOrientations(self):
        a = self.cornerOrientation
        result = [0] * 9
        for corner in Corner:
            result[-corner.value - 2] = a % 3
            a //= 3
        result[-1] = (-sum(result) % 3) % 3
        return result[1:]

    def getEdgeOrientations(self):
        a = self.edgeOrientation
        result = [0] * 13
        for edge in Edge:
            result[-edge.value - 2] = a % 2
            a //= 2
        result[-1] = (-sum(result) % 2) % 2
        return result[1:]


