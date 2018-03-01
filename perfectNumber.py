#Heather Stafford
#2/28/18
#perfectNumber.py

num = int(input('Enter a number: '))

total = 0
for i in range(1,num):
    if num % i == 0:
        total = total + i
print(total)
if total == num:
    print('Perfect')
else:
    print('Not perfect')

        
        
        
        
        
        