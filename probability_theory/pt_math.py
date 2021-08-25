import math

def combination(n,k):

    numerator, denominator = 1, 1
    
    if k < n/2:
        for i in range(n-k, n):
            numerator = numerator*(i+1)
            denominator = denominator*(n-i)

    return numerator/denominator

def get_dividers(number):

    if number < 0:
        number = number * (-1)
    dividers = []
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            number = number // i
            dividers.append(i)

    return dividers
