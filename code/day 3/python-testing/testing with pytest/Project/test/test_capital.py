# test_capital.py   (file name should start with test_xxx)
# $ pip install pytest
# import pytest and write the code and run it
#   To run type "pytest" in terminal           or 
# $ pytest -q test_capital.py

import pytest
def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

'''
#handlilng errors
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)

'''