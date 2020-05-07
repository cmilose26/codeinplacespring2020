"""
File: examplefor.py
------------------
Print the first 100 even numbers
"""

def main():
    big_for_loop()



def print_odd():
    for i in range (100):
        if (i % 2) != 0:
            print(i)

def print_even():
    for i in range (50):
        print(i * 2)

def print_even_alt():
    for i in range(0,100,2):
        print(i)

def for_loop_alt():
    i = 0
    while i < 100:
        print('Python rocks socks!')
        i += 1

def big_for_loop():
    for i in range(999999):
        print('You rock!')
        print('See you on Monday')

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()