'''
You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.
'''


############# FIRST APPROACH #####################

def gcd(n1, n2):
    small_num = min(n1, n2)
    for i in range(small_num,0, -1):
        if n1%i==0 and n2%i==0:
            return i
        
# print(gcd(6, 12))

############# ANOTHER APPROACH #####################

def gcd(n1, n2):
    # Keep looping until the remainder becomes 0
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

# print(gcd(9, 8))   # Output: 1
print(gcd(6, 12))  # Output: 6