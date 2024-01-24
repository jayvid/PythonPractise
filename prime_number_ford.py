def check_prime(number):
    if(type(number) != int): # return false for incorrect type and error message
        return (False, "Incorrect datatype")
    elif number <= 1 : # return false, not prime
        return False
    else : # check if the decimal number is prime or not 
        for num in range (2, int(number ** 0.5)+1): # most optimal way to check for primes
            if number % num == 0 :
                return False
        else:
            return True