#! /usr/bin/env python3

def get_input():    
    #get the input
    number = input("Enter the Number: ")
    return number

def calculate(n):
    #initialze varriables for calculating the Fibonacci number at this position in the sequence
    a,b = 0,1

    #one way to calculate the Fibonacci number
    for i in range(int(n)):
        a,b = b,a+b

    # store the result so its obvious
    fibonacci_number = a
    return fibonacci_number

def print_line(original,fib):

    #print the output
    print('The Fibonacci number for', original, 'is:', fib)

def main():
    original_number = get_input()
    fib = calculate(original_number)
    print_line(original_number,fib)

# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
    main()

