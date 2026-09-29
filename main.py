from task1_number import run as run_number
from task2_name import run as run_name
from task3_list import run as run_list

while True:
    print('Choose a program')
    print('1 - Check number')
    print('2 - Check name')
    print('3 - Check multiples')
    print('4 - Exit')
    
    choice = input('Your choice: ')
    
    if choice == '1':
        run_number()
    elif choice == '2':
        run_name()
    elif choice == '3':
        run_list()
    elif choice == '4':
        print('Program finished.')
        break
    else: print('wrong choice')
        