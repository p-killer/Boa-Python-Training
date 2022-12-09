'''
Parametrized Test Functions
Having tested the individual methods in the Wallet class, 
the next step we should take is to test various combinations of these methods.
 This is to answer questions such as “If I have an initial balance of 30, and spend 20, then add 100, 
 and later on, spend 50, how much should the balance be?”

As you can imagine, writing out those steps in the tests would be tedious, 
and pytest provides quite a delightful solution: Parametrized test functions

# test_advwallet.py
'''

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected

'''
This enables us to test different scenarios, all in one function. 
We make use of the @pytest.mark.parametrize decorator, 
where we can specify the names of the arguments that will be passed
 to the test function, and a list of arguments corresponding to the names.

The test function marked with the decorator will then be run once for each set of parameters.

For example, the test will be run the first time with the 
earned parameter set to 30, spent set to 10, and expected set to 20. 
The second time the test is run, the parameters will take the second 
set of arguments. We can then use these parameters in our test function.

This elegantly helps us capture the scenario:

My wallet initially has 0,
I add 30 units of cash to the wallet,
I spend 10 units of cash, and
I should have 20 units of cash remaining after the two transactions.
This is quite a succinct way to test different combinations of values without writing a lot of repeated code.

Combining Test Fixtures and Parametrized Test Functions
To make our tests less repetitive, we can go further and combine test fixtures and parametrize test functions. To demonstrate this, let’s replace the wallet initialization code with a test fixture as we did before.

The end result will be:

# test_wallet.py
'''
@pytest.fixture
def my_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected

 '''   
We will create a new fixture called my_wallet that is exactly the same as the 
empty_wallet fixture we used before. It returns a wallet instance with a balance of 0.
 To use both the fixture and the parametrized functions in the test, we include the fixture 
 as the first argument and the parameters as the rest of the arguments.

The transactions will then be performed on the wallet instance provided by the fixture.

You can try out this pattern further, e.g. with the wallet instance with a non-empty
 balance and with other different combinations of the earned and spent amounts.
 '''