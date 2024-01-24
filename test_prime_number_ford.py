import pytest
from prime_number_ford import check_prime

test_data = { '1' : [1,False], # Scenario 1 : Number 1
              '2' : [0,False], # Scenario 2 : number 0 
              '3' : [-1,False], # Scenario 3 : Negative number
              '4' : [10.4, (False,"Incorrect datatype")], # Scenario 4 : Floating point number
              '5' : ['abc', (False,"Incorrect datatype")], # Scenario 5 : String
              '6' : [2, True], # Scenario 6 : Number 2 => first prime number
              '7' : [3, True], # Scenario 7 : Number 3 => second prime number
              '8' : [1009, True], # Scenario 8 : Larger prime number
              '9' : [800, False], # Scenario 9 : Larger non-prime number
              '10': [7919, True], # Scenario 10 : Very large prime number
              '11': [100000, False] # Scenario 11 : Very large non-prime number
}

@pytest.mark.parametrize("dataset", test_data.values())
def test_check_prime(dataset):
    assert check_prime(dataset[0]) == dataset[1]