# Document to define functions for the Simple Calculator
import os

def welcome():
    welcome = '𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆 𝕋ℍ𝔼 𝕊𝕀𝕄ℙ𝕃𝔼 ℂ𝔸𝕃ℂ𝕌𝕃𝔸𝕋𝕆ℝ\n'
    print(welcome)

def main():
    first_number = input('Type the first number of your operation: ')
    second_number = input('Type the second number of your operation: ')
    operation = input('Type the operation you want to make with these numbers ( + - * / ): ')
    exec(operation, first_number, second_number)
    input('\nPress any key to restart')
    os.system('cls')
    main()

def sum(x, y):
    x = int(x)
    y = int(y)
    return(x + y)

def min(x, y):
    x = int(x)
    y = int(y)
    return(x - y)

def mult(x, y):
    x = int(x)
    y = int(y)
    return(x * y)

def div(x, y):
    x = int(x)
    y = int(y)
    return(x / y)

def exec(operation, first_number, second_number):
    match operation:
        case '+':
            sum_result = sum(first_number, second_number)
            print(f'The result of {first_number} + {second_number} is {sum_result}')

        case '-':
            min_result = min(first_number, second_number)
            print(f'The result of {first_number} - {second_number} is {min_result}')

        case '*':
            mult_result = mult(first_number, second_number)
            print(f'The result of {first_number} * {second_number} is {mult_result}')

        case '/':
            div_result = div(first_number, second_number)
            print(f'The result of {first_number} / {second_number} is {div_result}')