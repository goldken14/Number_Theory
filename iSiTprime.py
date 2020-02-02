# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:16:31 2020

@author: goldk
"""

#Sieve of Eratosthenes
"""
Let's hunt for prime numbers
"""
N=300
sqrt_N=int(N**0.5)
primes=list(range(2,N+1))

i=0
d=primes[i]
while d <= sqrt_N:
  for n in primes:
    if n%d==0 and n!=d:
      primes.remove(n)
  i=i+1
  d=primes[i]
print(primes)

gap_prime = [0]*(len(primes)-1)
for n in range(0,len(gap_prime)):
    gap_prime[n] = primes[n+1] - primes[n]
    
gap_avg = [0]*(len(primes)-1)
for n in range(0,len(gap_prime)):
    gap_avg[n] = sum(gap_prime[0:n+1])/len(gap_prime[0:n+1])
    
import matplotlib.pyplot as g

n=list(range(1,len(gap_avg)+1))
g.plot(n,gap_avg)
g.show()
#Prime Factorization
"""
Now let's factor
"""
'''
I=60
sqrt_I=int(I**0.5)
factors=[1]
for i in range(0,primes[sqrt_I]):
    if I%primes[i]==0:
        factors.append(primes[i])
        I=I/primes[i]
'''
        
        

    

