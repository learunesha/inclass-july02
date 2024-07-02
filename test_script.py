
from mypackage import greet

def test_greet():
    name = "Alice"
    expected = "Hello, Alice!"
    result = greet(name)
    assert result == expected, f"Expected '{expected}', but got '{result}'"

if __name__ == "__main__":
    test_greet()
    print("Tests passed successfully!")

