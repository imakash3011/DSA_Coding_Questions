def divisor(n1):
    result = []
    for i in range(1, (n1//2) + 1): ## prefer using square root for more optimal solution
        if n1%i==0:
            result.append(i)
    return result

print(divisor(16))




import math

def divisor(n1):
    result = []
    # Loop only up to the square root of n1
    for i in range(1, int(math.isqrt(n1)) + 1):
        if n1 % i == 0:
            result.append(i)          # Add the smaller divisor
            
            # If the paired divisor is different, add it too
            if i != n1 // i:
                result.append(n1 // i)
                
    # Optional: Sort the result if you want them in increasing order
    result.sort()
    return result

print(divisor(16)) # Output: [1, 2, 4, 8, 16]