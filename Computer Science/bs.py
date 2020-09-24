import math as mt 
  
prime = [0 for i in range(1000000)] 
def eratosthenes(n): 
    for i in range(1, n + 2): 
        prime[i] = True
  
    prime[1] = False
  
    for p in range(2, mt.ceil(n**(0.5))):
  
        if (prime[p] == True): 
            for i in range(p * p, n + 1, p): 
                prime[i] = False


 def power_of_two(n):
     return (n and (n &(n-1)) == False)

def proth_number(n):
    k=1
    while(k < (n // k)):
        if (n % k == 0):

            if (power_of_two(n // k)):
                return True
        k = k + 2
    return False

def proth_prime(n):
    if (proth_number(n-1)):

        if (prime[n]):
            return True
        else:
            return False
    else:
        return False



n = 40
eratosthenes(n)
for i in range(1, n+1):
    if proth_prime(i) == True:
        print(i)