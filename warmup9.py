#Heather Stafford
#3/1/18
#warmup9.py

text = input('Enter text: ')

for ch in text:
    if ch=='i' or ch=='a' or ch=='e' or ch=='o':
        print(ch.upper())
    else:
        print(ch.lower())