'''
1. The Modulo 6 Shortcut Every single prime number in the universe greater than 3 can be written in the form 6k + 1 or 6k - 1.
This means if you take any prime number and divide it by 6, the remainder will always be either 1 or 5.
'''

def prime_num(n):
    if n<=1:
        return False
    limit_num = int(n**0.5)  ## basically square root 

    for i in range(2, limit_num+1):
        if n%i==0:
            return False
    return True

print(prime_num(11))






def is_prime_fast(n):
    # Quick base filters
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    
    # THE MODULO 6 SHORTCUT: 
    # If the remainder isn't 1 or 5, it CANNOT be prime. Exit instantly!
    if n % 6 != 1 and n % 6 != 5:
        return False
        
    # Only if it passes the shortcut do we run a small loop up to the square root
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
            
    return True

# print(is_prime_fast(11))