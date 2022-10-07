import math
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <=0:
        raise Exception (ValueError)
    list =[]
    num =1
    count = 0
    while count!= number_of_primes:
        if isPrime(num):
            print(count)
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

print(primes(-1))