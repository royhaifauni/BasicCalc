import sys
import os

# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    print("Test add passed!")

def test_subtract():
    assert calculator.subtract(10, 5) == 5
    assert calculator.subtract(0, 1) == -1
    print("Test subtract passed!")

def test_multiply():
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(0, 5) == 0
    print("Test multiply passed!")

def test_divide():
    assert calculator.divide(10, 2) == 5.0
    try:
        calculator.divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
        print("Test divide by zero passed!")
    print("Test divide passed!")

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")
