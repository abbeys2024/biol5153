#! /usr/bin/env python3
import argparse

def get_args():
    # create an argumentParser object
    parser = argparse.ArgumentParser(description = 'This script rerturns the Fibonacci number at\
                                     a specified location in the Fibonacci sequence')
    
    # add positional arguments (these are the ones that are absolutely essential/required)
    parser.add_argument("num", help="The Fibonacci number you wish to calculate", type = int)

    # add optional arguments
    # if 'store_true, this means assign 'True' if the argument is specified on the command
    # line, so the default for 'store_true' is false
    parser.add_argument("-v", "--verbose", help = "Print verbose output or not", action = 'store_true')

    #parse the actual arguments
    args = parser.parse_args()
    return args


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
    if args.verbose: 
        print('The Fibonacci number for', original, 'is:', fib)
    else:
        print(fib)

def main():
    fib = calculate(args.num)
    print_line(args.num,fib)

# get the command line arguments
args = get_args()    

# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
    main()

