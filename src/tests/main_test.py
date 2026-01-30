"""
main_test.py
Test file for main.py.
"""


from src import main

def test_main():
    """
    Tests the main function 
    (NOTE that it is important to have "test_*" or "*_test" as the function name)
    """
    C = main.main(a=1, b=1)
    assert C == 2