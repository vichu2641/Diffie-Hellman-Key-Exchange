import os
import sys
from tqdm import tqdm
from termcolor import colored,cprint

import math
import base64
import random


def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p%i == 0:
            return False
    return True


def get_prime(size):
    while True:
        p = random.randrange(size, size*2)
        if is_prime(p):
            break
    return p


def is_generator(g, p):
    for i in range(1, p-1):
        if (g**i) % p == 1:
            return False
    return True


def get_generator(g):
    for g in range(2, p):
        if is_generator(g, p):
            return g


# p = get_prime(1000)
# g = get_generator(p)
# print(g, p)


# Public Area
p = get_prime(10)
g = get_generator(p)
print("Public generator: ",g, "\nPublic Prime Number: ", p)

# Alice (private)
a = random.randrange(0, p)
g_a = (g**a) % p
# Alice (public)
print("Alice sends this to an unsecure domain: ", g_a)

# Bob (private)
b = random.randrange(0, p)
g_b = (g**b) % p
# Bob (public)
print("Bob sends this to an unsecure domain: ", g_b)

print("\n")

# Alice (private)(received Bob's generator)
g_ab = (g_b**a) % p
print("Key created by Alice: ", g_ab)

# Bob (private)(received Alice's generator)
g_ba = (g_a**b) % p
print("Key created by Bob: ", g_ba)

print()

# Confirming crypto key
c_key = int

if g_ba == g_ab:
    c_key = g_ab
    print('collective cryptographic key: ', c_key)
else:
    print('Diffie-Hellman process failed \t No key')

class Encryption:

	def __init__(self,filename):	# Constructor
		self.filename = filename

	def encryption(self): # Allows us to perfrom file operation

		try:
			original_information = open(self.filename,'rb')

		except (IOError, FileNotFoundError):
			cprint('File with name {} is not found.'.format(self.filename), color='red',attrs=['bold','blink'])
			sys.exit(0)

		try:

			encrypted_file_name = 'cipher_' + self.filename
			encrypted_file_object = open(encrypted_file_name,'wb')

			content = original_information.read()
			content = bytearray(content)


			key = 10
			cprint('Encryption Process is in progress...!',color='green',attrs=['bold'])
			for i,val in tqdm(enumerate(content)):
				content[i] = val ^ key
			
			encrypted_file_object.write(content)
			

		except Exception:
			cprint('Something went wrong with {}'.format(self.filename),color='red',attrs=['bold','blink'])
		finally:
			encrypted_file_object.close()
			original_information.close()

class Decryption:

	def __init__(self,filename):
		self.filename = filename

	def decryption(self):	# produces the original result
		
		try:
			encrypted_file_object = open(self.filename,'rb')

		except (FileNotFoundError,IOError):
			cprint('File with name {} is not found'.format(self.filename),color='red',attrs=['bold','blink'])
			sys.exit(0)

		try:

			decrypted_file = input('Enter the filename for the Decryption file with extension:') # Decrypted file as output

			decrypted_file_object = open(decrypted_file,'wb')

			cipher_text = encrypted_file_object.read()

			key = 10

			cipher_text = bytearray(cipher_text)

			cprint('Decryption Process is in progress...!',color='green',attrs=['bold'])

			for i,val in tqdm(enumerate(cipher_text)):
				cipher_text[i] = val^key
		
			decrypted_file_object.write(cipher_text)
			

		except Exception:
				cprint('Some problem with Ciphertext unable to handle.',color='red',attrs=['bold','blink'])

		finally:
			encrypted_file_object.close()
			decrypted_file_object.close()

space_count = 30 * ' '
cprint('{} File Encryption And Decryption Tool. {}'.format(space_count,space_count), 'red')
while True:
		cprint('1. Encryption',color='magenta')
		cprint('2. Decryption',color='magenta')
		cprint('3. Exit', color='red')
		# cprint('Enter your choice:',color='cyan',attrs=["bold"])
		cprint('~Python3:',end=' ', color='green')
		choice = int(input())

		if choice == 1:
			cprint('Enter the filename for Encryption with proper extension:',end=' ',color='yellow',attrs=['bold'])
			file = input()
			E1 = Encryption(file)
			E1.encryption()
			cprint('{} Encryption is done Sucessfully...!'.format(file), color='green',attrs=['bold'])
			cprint('Do you want to do it again (y/n):',end = ' ', color='red',attrs=['bold','blink'])
			again_choice  = input()
			if (again_choice.lower() == 'y'):
				continue
			else:
				break

		elif choice == 2:
			cprint('Enter the Encrypted filename with proper extension:',end=' ',color='yellow',attrs=['bold'])
			file = input()
			D1 = Decryption(file)
			D1.decryption()
			cprint('{} Decryption is done Sucessfully...!'.format(file),color='green',attrs=['bold'])
			cprint('Do you want to do it again (y/n):',end = ' ', color='red',attrs=['bold','blink'])
			again_choice  = input()
			if (again_choice.lower() == 'y'):
				continue
			else:
				break
		elif choice == 3:
			sys.exit(0)
		else:
			print('Your choice of selection is not available. Sorry to see you again.')