"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

primes = []
n = int(input('number: '))
x = 2

while n>1:
	if n % x == 0:
		primes.append(x)
		n = n // x
		x = 1
	x += 1

print(max(primes))