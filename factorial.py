def factorial (number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

number = int(input('Enter a number:'))
print('The factorial of ', number, 'is ', factorial(number))