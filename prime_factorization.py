#Finding the prime factors of a number
import math


def prime_factors(n):

    prime_fact = []
    remainder = True
    
    while remainder:

        if n % 2 != 0:
            remainder = False

        else:
            n = int(n / 2) 
            prime_fact.append(2)
            remainder = True

    
    for i in range(3, int(math.sqrt(n))+1, 2):

        while n % i == 0:
            n = int(n/i)
            prime_fact.append(i)

        else:
            i+=1

    if n > 2:
        prime_fact.append(n)

    return prime_fact
        

    
            

    

    
