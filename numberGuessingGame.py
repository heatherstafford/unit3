#Heather Stafford
#2/28/18
#numberGuessingGame.py

from random import randint

num = randint(1,100)

total = 0 

while True:
    guess = int(input('Enter a number between 1 and 100: '))
    total = total + 1
    if guess == num:
        print('You got it in', total, 'tries')
        break
    elif guess > num:
        print('too high')
    else:
        print('too low')
