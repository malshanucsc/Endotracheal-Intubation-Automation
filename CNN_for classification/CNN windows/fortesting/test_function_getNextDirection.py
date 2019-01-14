import function_getNextDirection


def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(2, "forward")
    assert val == 1

def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(7, "forward")
    assert val == 1

def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(4, "forward")
    assert val == 2

def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(5, "forward")
    assert val == 3

def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(8, "forward")
    assert val == 4

def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(10, "forward")
    assert val == 6

def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(9, "forward")
    assert val == 5

def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(20, "forward")
    assert val == 7

def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(2, "backward")
    assert val == 8

def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(7, "backward")
    assert val == 8

def test_getNextDirection():
    val = function_getNextDirection.getNextDirection(23, "backward")
    assert val == 9


