# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)



'''
Refactoring our Tests with Fixtures to avoid repetition of code
 pytest fixtures seto[] up some helper code that should run before any tests are executed,
  and are perfect for setting-up resources that are needed by the tests.

Fixture functions are created by marking them with the @pytest.fixture decorator. 
Test functions that require fixtures should accept them as arguments.
 For example, for a test to receive a fixture called wallet, 
 it should have an argument with the fixture name, i.e. wallet.

'''
# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)

'''
For the first test function, we make use of the empty_wallet fixture, 
which provided a wallet instance with a balance of 0 to the test.

The next three tests receive a wallet instance initialized with a balance of 20. 
Finally, the last test receives the empty_wallet fixture. 
The tests can then make use of the fixture as if it was created inside the test function, 
as in the tests we had before.

Utilizing fixtures helps us de-duplicate our code. If you notice a case 
where a piece of code is used repeatedly in a number of tests, that might be a 
good candidate to use as a fixture.


Each test is provided with a newly-initialized Wallet instance,
 and not one that has been used in another test.

It is a good practice to add docstrings for your fixtures. 
To see all the available fixtures, run the following command:

$ pytest --fixtures
This lists out some inbuilt pytest fixtures, as well as our custom fixtures. 
The docstrings will appear as the descriptions of the fixtures.

wallet
    Returns a Wallet instance with a balance of 20
empty_wallet
    Returns a Wallet instance with a zero balance
'''