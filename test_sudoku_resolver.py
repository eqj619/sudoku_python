from sudoku_resolver import sudokuMap

'''
$pytest -v --capture=no  
'''

def test_case09():
    testmap = [
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,2,8,0,
    3,7,6,4,0,0,0,0,0,

    7,0,0,0,0,1,0,0,0,
    0,2,0,0,0,0,0,0,0,
    4,0,0,3,0,0,0,0,6,

    0,1,0,0,2,8,0,0,0,
    0,0,0,0,0,5,0,0,0,
    0,0,0,0,0,0,0,0,3
    ]

    mySudoku = sudokuMap()
    mySudoku.fillNumMap(testmap)
    mySudoku.print()

    mySudoku.resolveSudoku(0)
    mySudoku.print()
