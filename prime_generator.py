#! /usr/bin/python
# -*-coding:utf-8 -*

import random

def is_composite(n, a, d, s):
	"""
	Try to determinate if the number n is composite.
	n : the number tested
	a : a random number < n-1
	d, s : numbers verifying 2**s * d == n-1
	"""
	if(pow(a, d, n) == 1):
		return False

	for i in range (s):
		if(pow(a, pow(2,i) * d, n) == n-1):
			return False

	return True

def miller_rabin(n, k=10):
	"""
	Implementation of the Miller-Rabin which try to evaluate if a number
	is prime.
	n : the number tested
	k : number of iteration (increase the probability of finding a true prime number)
	"""
	d = n-1
	s = 0

	while(True):
		quotient, reminder = divmod(d, 2)
		if(reminder == 1):
			break
		s += 1
		d = quotient

	for i in range (k):
		a = random.randint(2, n-2)
		if(is_composite(n, a, d, s)):
			return False

	return True

def is_prime(n):
	"""
	Return true if the given number n is prime, false otherwise.
	The algorithm has a small chance of evaluate prime a number which is not, 
	because it uses the Miller-Rabin algorithm.
	"""
	if(n <= 2):
		return False
	if(n % 2 == 0):
		return False

	return miller_rabin(n)

def generate_prime_number(bit_number=1000):
	"""
	Return a prime number of bit_number bits.
	"""
	i = 1
	while True:
		a = random.getrandbits(bit_number)
		if(is_prime(a)):
			print(str(i) + ' iterations')
			print('Number found : ' + str(a))
			return a
		i += 1


if __name__ == '__main__':
	generate_prime_number()
