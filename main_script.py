#! /usr/bin/env python3

import say_hello

def main():
    name = input("Enter a name: ")

    say_hello.greeting(name)

    fav = input('Whats your favorite? ')

    say_hello.favorite(fav)

# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
    main()