#! /usr/bin/python
# -*-coding:utf-8 -*

import random

def is_composite(n, a, d, s):
	if(pow(a, d, n) == 1):
		return False

	for i in range (s):
		if(pow(a, pow(2,i) * d, n) == n-1):
			return False

	return True

def miller_rabin(n, k=10):
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
	if(n <= 2):
		return False
	if(n % 2 == 0):
		return False

	return miller_rabin(n)

def generate_prime_number(digit_number=500):
	i = 1
	while True:
		a = random.randint(10**digit_number, 10**(digit_number+1)-1)
		if(is_prime(a)):
			print(str(i) + ' itérations')
			return a
		i += 1


if __name__ == '__main__':
	print(generate_prime_number())
