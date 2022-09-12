import random

max_number = input('Maximum number: ')
max_number = int(max_number)
n = random.randint(0, max_number)
while True:
    x = input('Guess number: ')
    x = int(x)
    if x < n:
        print('higher')
    if x > n:
        print('lower')
    if x == n:
        print('You guessed it', n)
        break