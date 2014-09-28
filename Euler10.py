"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import math

total = 2

def CheckPrime(number):
	while number < 2000000:
		if any(number % b == 0 for b in range(3, int(math.sqrt(number)) + 1, 2)):
			pass
		else:
			yield number
		number += 2
		

g = CheckPrime(3)
for i in range(2000000):
	total += next(g)
	print(total)