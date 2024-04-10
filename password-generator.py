import random

print('welcome to password generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount of password to generate: ')
number = int(number)

length = input('Tnput your password length: ')
length = int(length)

print('\n here are your password length: ')

for pwd in range(number):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
  print(passwords)    