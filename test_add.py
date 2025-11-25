from add import add_numbers

def test_add_numbers():
    assert add_numbers(10, 20) == 30
    assert add_numbers(-5, 5) == 0
    assert add_numbers(2, 3) == 5