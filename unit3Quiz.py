#Heather Stafford
#3/5/18
#unit3Quiz

"""
i = -15
while i < -8:
    print(i)
    i += 1
    
for i in range(50,17,-4):
    print(i)
    
total = 0
for i in range(-100,1000,2):
    total = total + i
print(total)
"""

while True:
    text = input('Enter text: ')
    for ch in text:
        if ch in 'alpaca':
            break
    print(text)