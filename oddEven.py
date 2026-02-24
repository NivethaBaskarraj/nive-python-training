#get user input as an integer
number=int(input('Enter the number you want to check:'))
if (number == 0):
    print('the number', number, 'is neither odd nor even')
elif (number % 2 == 0):
    print('the number', number, 'is even')
else:
    print('the number', number, 'is odd')