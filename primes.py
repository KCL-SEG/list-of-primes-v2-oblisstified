import math
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
     ##good variable names 
    if number_of_primes<=0:
        raise ValueError('has to be larger than 0')
    else:
        list =[] ##have a more appropriate name for the list
        num = 1
        count = 0
        while count!= number_of_primes:
            if isPrime(num):
                list.append(num)
                count+=1
            num+=1
        return list
  
def isPrime(num):
    if num ==1:
        return False
    for i in range(2, int(math.sqrt(num)//1) +1):
        if num% i ==0:
            return False
    return True