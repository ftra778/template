"""
main.py
Test file for GitHub. Pylint will score the coding style and pytest will test the functionality
"""


import numpy as np

def main(a=1, b=1) -> int:
    """
    main asserts a simple calculation that ensures the application runs clean
    """
    return int(a + b)


if __name__ == "__main__":
    C = main(a=np.int32(1), b=np.int32(1))
