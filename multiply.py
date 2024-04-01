#! /usr/bin/env python3

def get_input():
    user_num = int(input('Enter the size of your table:'))
    user_num += 1
    return user_num

def print_table(user_num):
    cell_width = len(str((user_num * user_num))) + 1
    for k in range(1,user_num):
        for j in range(1,user_num):
            print('{:>{cell_width}}'.format(k*j,cell_width = cell_width), end = '')
        print()

def main():
    input_num = get_input()
    print_table(input_num)

# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
    main()



