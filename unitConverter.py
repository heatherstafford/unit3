#Heather Stafford
#1/29/18
#unitConverter.py

print('1: kilometers to Miles')
print('2: Kilograms to Pounds')
print('3: Liters to Gallons')
print('4: Celsius to Fahrenheit')
num = int(input('Choose a number: '))

if num == 4:
    celcius = int(input('Enter Degrees in Celcius: '))
    fahrenheit = celcius * 1.8 + 32
    print(celcius,'degrees Celsius is', fahrenheit,'degres in Fahrenheit')
elif num == 3:
    liters = int(input('Enter amount in liters: '))
    gallons = liters/3.785411784
    print(liters,'liters is', gallons,' gallons')
elif num == 2:
    kilograms = int(input('Enter a number of Kilograms: '))
    pounds = kilograms/0.453592
    print(kilograms,'Kilograms is', pounds,'pounds')
elif num == 1:
    kilometers = int(input('Enter a number of Kilometers'))
    miles = kilometers/1.60934
    print(kilometers,'kilometers is', miles,'miles')
else:
    print('Error, number not an option')
