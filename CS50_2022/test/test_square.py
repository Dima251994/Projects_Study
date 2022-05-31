from square_pro import square # импортируем мою функцию 


def test_positive():
    assert square(2) == 4  # якщо результат множення 2 не рівний 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

