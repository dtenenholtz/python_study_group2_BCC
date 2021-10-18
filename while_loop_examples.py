# basic while loops for Python Study Group meeting Oct 2021

# while loop example 1
number = 0
while number < 10:
    print(number)
    number = number + 2


# while loop example 2
keep_going = 'y'
while keep_going == 'y':
    user_says = input('Enter a few words: ')
    allcaps = user_says.upper().rstrip()
    print(allcaps)
    keep_going = input('Do you want to enter another group of words? Type y or n: ')
