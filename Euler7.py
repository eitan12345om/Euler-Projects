"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""
primes = []
primes.append(2)

def checkPrime(a, number_of_primes):
	while len(primes) < number_of_primes:
		if any(a % b == 0 for b in range(3, int(a/2), 2)):
			pass
		else:
			primes.append(a)
		a += 2
	print(primes)

checkPrime(3, int(input('Number of primes: ')))