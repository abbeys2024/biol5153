#! /usr/bin/env python3
user_num = int(input('Enter the size of your table:'))
user_num += 1
for k in range(1,user_num):
    for j in range(1,user_num):
        print('{:^4}'.format(k*j), end = ' ')
    print()



