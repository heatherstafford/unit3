#Heather Stafford
#2/28/18
#betterAdditionGameDemo.py - more practice

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    answer = int(input('What is ' + str(num1) + ' + ' + str(num2) + '? '))
    if answer == num1 + num2:
        numCorrect += 1
    else:
        print('WRONG!')
        print('The answer is ', num1 + num2)

print('You win!')
