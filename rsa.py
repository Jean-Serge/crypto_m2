#! /usr/bin/python
# -*-coding:utf-8 -*

import prime_generator as prime

class RSA:
	def __init__(self):
		self.p = prime.generate_prime_number()
		while(True):
			self.q = prime.generate_prime_number()
			if(self.q != self.p):
				break




if __name__ == '__main__':
	rsa = RSA()
