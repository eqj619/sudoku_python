from sudoku_resolver import sudokuMap

'''
pytest -v --capture=no --durations=0
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

    test09answer = [
        8,4,2,5,1,9,3,6,7,
        1,5,9,6,7,3,2,8,4,
        3,7,6,4,8,2,9,5,1,
        7,3,5,2,6,1,4,9,8,
        6,2,1,8,9,4,7,3,5,
        4,9,8,3,5,7,1,2,6,
        5,1,3,7,2,8,6,4,9,
        9,6,4,1,3,5,8,7,2,
        2,8,7,9,4,6,5,1,3
        ]
    mySudoku = sudokuMap()
    mySudoku.fillNumMap(testmap)
    mySudoku.print()

    mySudoku.resolveSudoku(0)
    mySudoku.print()

    mySudoku.getNumMap(testmap)
    assert test09answer == testmap
    del mySudoku

def test_case02():
    testmap = [
    1,5,7,6,4,0,0,9,8,
    2,0,9,0,0,0,0,0,0,
    0,0,0,9,1,0,0,0,4,

    8,0,0,4,3,0,0,5,0,
    0,0,0,0,0,0,0,0,0,
    0,2,0,0,6,8,0,0,7,

    7,0,0,0,8,6,0,0,0,
    0,0,0,0,0,0,0,0,1,
    0,9,0,0,0,4,8,6,2
    ]
    test02answer = [
    1,5,7,6,4,2,3,9,8,
    2,4,9,8,5,3,1,7,6,
    3,6,8,9,1,7,5,2,4,
    8,7,6,4,3,1,2,5,9,
    4,1,5,7,2,9,6,8,3,
    9,2,3,5,6,8,4,1,7,
    7,3,2,1,8,6,9,4,5,
    6,8,4,2,9,5,7,3,1,
    5,9,1,3,7,4,8,6,2,
    ]

    mySudoku = sudokuMap()
    mySudoku.fillNumMap(testmap)
    mySudoku.print()

    mySudoku.resolveSudoku(0)
    mySudoku.print()
    mySudoku.getNumMap(testmap)
    assert test02answer == testmap
    del mySudoku

def test_case03():
    testmap = [
    0,0,5,4,0,1,6,0,0,
    0,0,0,0,6,0,0,0,0,
    0,9,4,0,0,7,0,2,0,

    3,7,0,0,2,0,0,4,0,
    0,0,0,0,1,0,0,0,0,
    0,1,0,0,4,0,0,5,6,

    0,5,0,8,0,0,2,6,0,
    0,0,0,0,9,0,0,0,0,
    0,0,2,3,0,6,9,0,0
    ]
    test03answer = [
    8,2,5,4,3,1,6,9,7,
    1,3,7,2,6,9,4,8,5,
    6,9,4,5,8,7,3,2,1,
    3,7,8,6,2,5,1,4,9,
    5,4,6,9,1,8,7,3,2,
    2,1,9,7,4,3,8,5,6,
    9,5,1,8,7,4,2,6,3,
    4,6,3,1,9,2,5,7,8,
    7,8,2,3,5,6,9,1,4
    ]
    mySudoku = sudokuMap()
    mySudoku.fillNumMap(testmap)
    mySudoku.print()

    mySudoku.resolveSudoku(0)
    mySudoku.print()
    mySudoku.getNumMap(testmap)
    assert test03answer == testmap
    del mySudoku

def test_case04():
    testmap = [
    5,0,4,0,0,0,0,0,1,
    0,0,6,4,0,0,0,7,0,
    0,0,0,6,0,8,0,0,0,

    0,0,0,0,5,0,0,1,3,
    0,0,0,0,0,0,0,0,0,
    8,3,0,0,2,0,0,0,0,

    0,0,0,9,0,4,0,0,0,
    0,4,0,0,0,7,6,0,0,
    2,0,0,0,0,0,8,0,9
    ]
    test04answer = [
    5,8,4,3,7,2,9,6,1,
    9,2,6,4,1,5,3,7,8,
    3,1,7,6,9,8,4,5,2,
    4,6,2,8,5,9,7,1,3,
    7,9,5,1,4,3,2,8,6,
    8,3,1,7,2,6,5,9,4,
    6,5,8,9,3,4,1,2,7,
    1,4,9,2,8,7,6,3,5,
    2,7,3,5,6,1,8,4,9
    ]
    mySudoku = sudokuMap()
    mySudoku.fillNumMap(testmap)
    mySudoku.print()

    mySudoku.resolveSudoku(0)
    mySudoku.print()
    mySudoku.getNumMap(testmap)
    assert test04answer == testmap
    del mySudoku

def test_case05():
    testmap = [
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,5,0,4,
    1,2,9,0,6,0,0,0,0,

    0,6,0,0,2,0,0,9,0,
    5,0,0,0,0,0,0,0,0,
    0,1,0,3,0,0,0,0,0,

    3,0,0,5,0,4,0,0,0,
    0,0,0,7,0,0,0,0,0,
    0,0,0,0,0,0,0,2,0
    ]
    test05answer = [
    6,4,5,8,7,3,2,1,9,
    7,3,8,2,9,1,5,6,4,
    1,2,9,4,6,5,8,3,7,
    8,6,4,1,2,7,3,9,5,
    5,9,3,6,4,8,1,7,2,
    2,1,7,3,5,9,6,4,8,
    3,7,2,5,1,4,9,8,6,
    9,8,6,7,3,2,4,5,1,
    4,5,1,9,8,6,7,2,3
    ]
    mySudoku = sudokuMap()
    mySudoku.fillNumMap(testmap)
    mySudoku.print()

    mySudoku.resolveSudoku(0)
    mySudoku.print()
    mySudoku.getNumMap(testmap)
    assert test05answer == testmap
    del mySudoku

def test_case06():
    testmap = [
    8,0,0,0,0,0,0,0,0,
    0,0,3,6,0,0,0,0,0,
    0,7,0,0,9,0,2,0,0,

    0,5,0,0,0,7,0,0,0,
    0,0,0,0,4,5,7,0,0,
    0,0,0,1,0,0,0,3,0,

    0,0,1,0,0,0,0,6,8,
    0,0,8,5,0,0,0,1,0,
    0,9,0,0,0,0,4,0,0
    ]
    test06answer = [
    8,1,2,7,5,3,6,4,9,
    9,4,3,6,8,2,1,7,5,
    6,7,5,4,9,1,2,8,3,
    1,5,4,2,3,7,8,9,6,
    3,6,9,8,4,5,7,2,1,
    2,8,7,1,6,9,5,3,4,
    5,2,1,9,7,4,3,6,8,
    4,3,8,5,2,6,9,1,7,
    7,9,6,3,1,8,4,5,2
    ]
    mySudoku = sudokuMap()
    mySudoku.fillNumMap(testmap)
    mySudoku.print()

    mySudoku.resolveSudoku(0)
    mySudoku.print()
    mySudoku.getNumMap(testmap)
    assert test06answer == testmap
    del mySudoku

def test_case07():
    testmap = [
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,1,0,6,0,
    2,0,7,0,9,0,0,0,0,

    3,0,0,0,0,4,2,0,9,
    0,1,0,6,0,5,0,0,0,
    0,0,0,0,0,0,0,0,0,

    0,6,4,0,0,0,0,5,0,
    0,0,0,0,2,0,3,0,0,
    0,0,0,0,0,0,0,0,0
    ]
    test07answer = [
    6,4,1,7,5,3,9,2,8,
    5,8,9,2,4,1,7,6,3,
    2,3,7,8,9,6,5,4,1,
    3,5,6,1,7,4,2,8,9,
    9,1,2,6,8,5,4,3,7,
    4,7,8,9,3,2,6,1,5,
    7,6,4,3,1,9,8,5,2,
    1,9,5,4,2,8,3,7,6,
    8,2,3,5,6,7,1,9,4
    ]
    mySudoku = sudokuMap()
    mySudoku.fillNumMap(testmap)
    mySudoku.print()

    mySudoku.resolveSudoku(0)
    mySudoku.print()
    mySudoku.getNumMap(testmap)
    assert test07answer == testmap
    del mySudoku

def test_case08():
    testmap = [
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,1,0,8,0,
    6,4,0,0,0,0,7,0,0,

    0,0,0,0,0,3,0,0,0,
    0,0,1,8,0,5,0,0,0,
    9,0,0,0,0,0,4,0,2,

    0,0,0,0,0,9,3,5,0,
    0,0,0,0,6,0,0,0,0,
    0,0,0,0,2,0,0,0,0
    ]
    test08answer = [
    1,8,7,4,5,2,9,6,3,
    2,3,9,6,7,1,5,8,4,
    6,4,5,9,3,8,7,2,1,
    7,6,4,2,9,3,8,1,5,
    3,2,1,8,4,5,6,7,9,
    9,5,8,7,1,6,4,3,2,
    4,7,2,1,8,9,3,5,6,
    8,1,3,5,6,4,2,9,7,
    5,9,6,3,2,7,1,4,8
    ]
    mySudoku = sudokuMap()
    mySudoku.fillNumMap(testmap)
    mySudoku.print()

    mySudoku.resolveSudoku(0)
    mySudoku.print()
    mySudoku.getNumMap(testmap)
    assert test08answer == testmap
    del mySudoku
