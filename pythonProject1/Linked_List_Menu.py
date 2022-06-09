import sys
import os
import numpy as np
# Imported from Linked_List python file
from Linked_List import Node
from Linked_List import linked_list


sys.tracebacklimit = 0
menu_options = {}
dllist = linked_list()
current_list = []

# Main Menu Options

def main_menu():
    os.system('cls')
    print('Please choose from the following: ')
    print('1. Insert 10 element')
    print('2. Insert 100 elements')
    print('3. Insert 1000 elements')
    print('4. Insert 10000 elements')
    print('5. Remove all elements')
    print('6. Print List')
    print('7. Exit')
    choice = int(input())
    exec_menu(choice)

# Function to execute menu

def exec_menu(choice):
    os.system('cls')
    if choice == 1:
        sed = np.loadtxt('num10.dat', unpack=True)
        with open('num10.dat','r') as elements:
            for line in elements:
                current_list.insert(line)
        main_menu()
    elif choice == 2:
        sed = np.loadtxt('num100.dat', unpack=True)
        with open('num100.dat', 'r') as elements:
            for line in elements:
                current_list.append(line)
        main_menu()
    elif choice == 3:
        sed = np.loadtxt('num1000.dat', unpack=True)
        with open('num1000.dat', 'r') as elements:
            for line in elements:
                current_list.append(line)
        main_menu()
    elif choice == 4:
        sed = np.loadtxt('num10000.dat', unpack=True)
        with open('num10000.dat', 'r') as elements:
            for line in elements:
                current_list.append(line)
        main_menu()
    elif choice == 5:
        dllist.clear()
    elif choice == 6:
        dllist.print()
        main_menu()
    elif choice == 7:
        print("GoodBye")
        sys.exit()
    else:
        print('Invalid option, please try again')
        main_menu()

main_menu()