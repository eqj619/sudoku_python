import sys

# Each digit 1..9 is represented by one bit (bit d-1). A "used" mask for a
# row/col/box is the OR of the bits of the digits already placed there.
ALL = 0x1FF  # bits 0..8 set -> digits 1..9 all available

# Precomputed tables indexed by a 9-bit mask:
#   BITCOUNT[m] -> number of set bits (how many candidate digits)
#   DIGITS[m]   -> list of the digits (1..9) whose bit is set
BITCOUNT = [bin(m).count('1') for m in range(512)]
DIGITS = [[d + 1 for d in range(9) if m & (1 << d)] for m in range(512)]


class sudokuMap:
    def __init__(self):
        print('you made sudokuMap instance')
        self.cells = [0] * 81   # 0 = empty, otherwise the fixed digit 1..9
        self.rows = [0] * 9     # used-digit bitmask per row
        self.cols = [0] * 9     # used-digit bitmask per column
        self.boxes = [0] * 9    # used-digit bitmask per 3x3 box

    # Place digit v at flat index i, updating the row/col/box masks.
    def _place(self, i, v):
        bit = 1 << (v - 1)
        r, c = i // 9, i % 9
        self.cells[i] = v
        self.rows[r] |= bit
        self.cols[c] |= bit
        self.boxes[(r // 3) * 3 + c // 3] |= bit

    # Undo a placement at flat index i.
    def _remove(self, i, v):
        bit = 1 << (v - 1)
        r, c = i // 9, i % 9
        self.cells[i] = 0
        self.rows[r] &= ~bit
        self.cols[c] &= ~bit
        self.boxes[(r // 3) * 3 + c // 3] &= ~bit

    def fillNumMap(self, pS):
        for i in range(81):
            if pS[i]:
                self._place(i, pS[i])

    def print(self):
        print('print sudoku map')
        for r in range(9):
            for c in range(9):
                v = self.cells[r * 9 + c]
                sys.stdout.write("%d " % v if v else "- ")
            sys.stdout.write("\n")

    # Recursive DFS with MRV (minimum remaining values) heuristic and
    # incremental candidate computation via the row/col/box masks.
    def solve(self):
        best_i = -1
        best_mask = 0
        best_count = 10
        for i in range(81):
            if self.cells[i] == 0:
                r, c = i // 9, i % 9
                mask = ALL & ~(self.rows[r] | self.cols[c] |
                               self.boxes[(r // 3) * 3 + c // 3])
                cnt = BITCOUNT[mask]
                if cnt == 0:
                    return False          # dead end: empty cell with no candidate
                if cnt < best_count:
                    best_count = cnt
                    best_i = i
                    best_mask = mask
                    if cnt == 1:
                        break             # cannot do better than a forced cell

        if best_i == -1:
            return True                   # no empty cell left -> solved

        for v in DIGITS[best_mask]:
            self._place(best_i, v)
            if self.solve():
                return True
            self._remove(best_i, v)
        return False

    # Kept for CLI compatibility. Returns 0 on success, -1 if unsolvable.
    def resolveSudoku(self, sN=0):
        return 0 if self.solve() else -1


"""
example:
time python3 sudoku_resolver.py 020000000000600003074080000000003002080040010600500000000010780500009000000000040
time python3 sudoku_resolver.py 800000000003600000070090200050007000000045700000100030001000068008500010090000400
"""
#########################################################
#main
if __name__ == '__main__':
    test09 = [
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,2,8,0,
        3,7,6,4,0,0,0,0,0,

        7,0,0,0,0,1,0,0,0,
        0,2,0,0,0,0,0,0,0,
        4,0,0,3,0,0,0,0,6,

        0,1,0,0,2,8,0,0,0,
        0,0,0,0,0,5,0,0,0,
        0,0,0,0,0,0,0,0,3]

    args = sys.argv
    if(len(args[1]) == 81 and str.isdecimal(args[1])):
        for i in range(0,81):
            test09[i] = int(args[1][i])

    mySudoku1 = sudokuMap()
    mySudoku1.fillNumMap(test09)
    mySudoku1.print()

    mySudoku1.resolveSudoku(0)
    mySudoku1.print()
