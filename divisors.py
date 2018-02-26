#Heather Stafford
#2/28/18
#divisors.py

num = int(input('Enter a number: '))

for i in range(1,num):
    newnum= num%i
    if newnum%2== 0:
        print(newnum)
