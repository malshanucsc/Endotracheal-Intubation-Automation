import label2

def test_getNextDirection():
    val1=label2.getNextDirection(2,"forward")
    assert val == 1

    val1=label2.getNextDirection(7,"forward")
    assert val == 1

    val1=label2.getNextDirection(4,"forward")
    assert val == 2

    val1=label2.getNextDirection(5,"forward")
    assert val == 3

    val1=label2.getNextDirection(8,"forward")
    assert val == 4

    val1=label2.getNextDirection(10,"forward")
    assert val == 6

    val1=label2.getNextDirection(9,"forward")
    assert val == 5

    val1=label2.getNextDirection(20,"forward")
    assert val == 7

    val1=label2.getNextDirection(2,"backward")
    assert val == 8

    val1=label2.getNextDirection(7,"backward")
    assert val == 9        
 