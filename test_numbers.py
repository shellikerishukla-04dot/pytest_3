from sum import sum_numbers
def test_add_positive_numbers():
    assert sum_numbers(2, 3) == 5
def test_add_negative_numbers():
    assert sum_numbers(-4,-6) == -10
def test_add_zero():
    assert sum_numbers(0, 5) == 5
