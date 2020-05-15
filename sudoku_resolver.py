import sys

class aslot:
    def __init__(self):
        self.fixed = 0
        self.numList = [1,2,3,4,5,6,7,8,9]

class sudokuMap:
    sudokuForm = [ [aslot() for i in range(9)] for j in range(9) ]

    initalCall = 0
    fLoop = 0
    sudokuCheckerLastNum = 0

    def __init__(self):
        print(f'you made sudokuMap instance')

    def print(self):
        print(f'print sudoku map')
        for i in range (0,9):
            for j in range (0,9):
                if (self.sudokuForm[i][j].fixed != 0):
                    sys.stdout.write("%d "% self.sudokuForm[i][j].fixed)
                else:
                    sys.stdout.write("- ")
            sys.stdout.write("\n")

    def numOfList(self, row, col):
        cnt = 0
        if(self.sudokuForm[row][col].fixed !=0):
            return(0)
        else:
            for nL in self.sudokuForm[row][col].numList:
                if(nL != 0):
                    cnt += 1
            return(cnt)

    def printNumOfList(self):
        for i in range (0,9):
            for j in range (0,9):
                sys.stdout.write("%d "% self.numOfList(i,j))
            sys.stdout.write("\n")

    def fillNumMap(self, pS):
        cnt = 0
        for i in range (0,9):
            for j in range (0,9):
                self.sudokuForm[i][j].fixed = pS[cnt]
                cnt += 1

    def NumOfNoneResolvedSlot(self):
        result = 0
        for i in range (0,9):
            for j in range (0,9):
                if(self.sudokuForm[i][j].fixed == 0):
                    result += 1
        return(result)

    def VerifyNumber(self, row, col):
        cnt = 0
        #it's already fixed number
        if(self.sudokuForm[row][col].fixed !=0):
            return(self.sudokuForm[row][col].fixed)

        #Check at Horizontal line
        for i in range(0,9):
            if(i != col):
                if(self.sudokuForm[row][i].fixed !=0):
                    self.sudokuForm[row][col].numList[ self.sudokuForm[row][i].fixed - 1 ] = 0

        #check at Verrical line
        for i in range(0,9):
            if(i != row):
                if(self.sudokuForm[i][col].fixed !=0):
                    self.sudokuForm[row][col].numList[ self.sudokuForm[i][col].fixed - 1 ] = 0

        #Check at Block
        blockmap = [[0,0,0,1,1,1,2,2,2],
        [0,0,0,1,1,1,2,2,2],
        [0,0,0,1,1,1,2,2,2],
        [3,3,3,4,4,4,5,5,5],
        [3,3,3,4,4,4,5,5,5],
        [3,3,3,4,4,4,5,5,5],
        [6,6,6,7,7,7,8,8,8],
        [6,6,6,7,7,7,8,8,8],
        [6,6,6,7,7,7,8,8,8]]

        checkCnt = 8
        targetBlock = blockmap[row][col]
        for i in range (0,9):
            for j in range (0,9):
                if(blockmap[i][j] == targetBlock):
                    if( i != row and j != col):
                        if(self.sudokuForm[i][j].fixed != 0):
                            self.sudokuForm[row][col].numList[ self.sudokuForm[i][j].fixed - 1 ] = 0
                        checkCnt -= 1
                        if(checkCnt == 0):
                            break

        #check how many candidate in numList
        cnt = 0
        for nL in self.sudokuForm[row][col].numList:
            if(nL != 0):
                cnt += 1
                self.sudokuForm[row][col].fixed = nL

        #cnt = 0 ... ERROR cannot find a number. all number are already there.
        #cnt = 1 ... find a number
        #cnt > 1 ... cannot fix because of 2 and more candidate remain. then, reset fixed value.
        if(cnt > 1):
            self.sudokuForm[row][col].fixed = 0
        if(self.sudokuForm[row][col].fixed == 0 and cnt == 0):
            return (-1)
        return(self.sudokuForm[row][col].fixed)

    def checkWholeNumMap(self):
        result = 1
        for i in range (0,9):
            for j in range (0,9):
                result = self.VerifyNumber(i,j)
                if(result == -1):
                    return(-1)
        return(1)

    #count the number of none-resolved slot
    #when result is ZERO, that's mean resolved all.
    def NumOfNoneResolvedSlot(self):
        result = 0
        for i in range (0,9):
            for j in range (0,9):
                if( self.sudokuForm[i][j].fixed == 0):
                    result += 1
        return(result)
    # Check then fill the number in resolved slot
    # return value
    #  -1 ... Sudoku Numbering Failure. need try another candidate number.
    #  0 ... complete
    #  1-81 ... the number of unresolved slot
    def sudokuChecker(self):
        openSlot = -1
        result = 0

        while (result != -1):
            result = self.checkWholeNumMap()
            openSlot = self.NumOfNoneResolvedSlot()
            if(openSlot == self.sudokuCheckerLastNum):
                break
            else:
                self.sudokuCheckerLastNum = openSlot
        if (result == -1):
            return(result)
        return(openSlot)

    """
    # Capture the snapshot of intrim Sudoku Form
    # Intrim captured form is used when rollback then try another candidate number.
    """
    def captureNumMap(self, pNm):
        for i in range (0, 81):
            pNm[i] = self.sudokuForm[int(i/9)][int(i%9)].fixed

    # Restore the captured intrim numbers to resume trial when rollback.
    def restoreNumMap(self, pNm):
        for i in range (0, 81):
            if(pNm[i] == 0):
                    self.sudokuForm[int(i/9)][int(i%9)].fixed = 0
                    self.sudokuForm[int(i/9)][int(i%9)].numList = [1,2,3,4,5,6,7,8,9]

    def SetFixedValue(self, row, col, TrialNum):
        self.sudokuForm[row][col].fixed = TrialNum

    def getNextSlotNum(self, slotNo):
        min = 9
        minSlotNo = slotNo

        for i in range(0,81):
            if (self.sudokuForm[int(i/9)][int(i%9)].fixed == 0):
                if (min > self.numOfList(int(i/9), int(i%9))):
                    min = self.numOfList(int(i/9), int(i%9))
                    minSlotNo = i
        return(minSlotNo)

    def resolveSudoku(self, sN):
        result = 0

        #DEBUG print('resolve_sudoku %d for slot %d(%d:%d)'% (self.fLoop, sN, int(sN/9), int(sN%9)))
        self.fLoop += 1

        if (self.initalCall == 0):
            result = self.sudokuChecker()
            print("initial sudokuChecker ", result)
            #DEFBUG self.printNumOfList()

            if (result == 0):
                return(0)
            self.initalCall = 1

        #find next unresolved slot
        sN = self.getNextSlotNum(sN)

        #capture a list of possible numbers
        possibleList = self.sudokuForm[int(sN/9)][int(sN%9)].numList
        #DEBUG print(possibleList)

        #Loop until try all possible numbers or Resolved
        capMap = [0]*81
        self.captureNumMap(capMap)

        for i in range(0,9):
            if(possibleList[i] == 0):
                continue
            self.restoreNumMap(capMap)

            #// set trial number
            self.SetFixedValue(int(sN/9), int(sN%9), possibleList[i])
            #DEBUG print('slot %d (%d:%d) try %d'% (sN, int(sN/9), int(sN%9), possibleList[i]) )
            #// execute sudoku checker
            result = self.sudokuChecker()
            #//printf(" RESULT for slot %d at sudokuChecker %d\n", slotNum, result);

            if (result == 0):
                return(0)
            #// if Unresolved, then re-store and try next number
            if (result == -1):
                continue
            #// succeed to fill in candidate number. then, try next slot.
            if (result > 0):
                ret = 0
                if (sN < 81):
                    ret = self.resolveSudoku(self.getNextSlotNum(sN))
                else:
                    print("reach slot number > 81")
                    return(-1)

                if(ret == 0):
                    return(0)
                if(ret == -1):
                    #print('Return from nesting resolve_sudoku call i=%d'% i)
                    continue

        #// Unresolved if un-resolved instead of try all candidates
        #print('Unresolved slot %d - Rollback'% sN);
        return(-1)

"""
example:
python3 sudoku_resolver.py 020000000000600003074080000000003002080040010600500000000010780500009000000000040
"""
#########################################################
#main
if __name__ == '__main__':
    test09 = [ 0,0,0,0,0,0,0,0,0,
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
