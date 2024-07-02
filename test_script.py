
from mypackage import main_func

def test_main_func():
    result = main_func()
    expected = "Hello from main_func!"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

if __name__ == "__main__":
    test_main_func()
    print("Tests passed successfully!")


