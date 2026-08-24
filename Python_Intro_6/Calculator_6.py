number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
action = input('Choose the operator(+,-,*,/): ')
while action not in('+','-','*','/'):
    action = input('Invalid input. Try again\n')
if action == '+':
    result = number1 + number2
elif action == '-':
    result = number1 - number2
elif action == '*':
    result = number1 * number2
elif action == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error:division by zero"
print(f'The result is:{result}')
