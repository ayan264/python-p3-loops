#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for i in range (10, 0, -1):
        print(i)
        print ("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    result = []
    for num in int_list:
        result.append(num * num) 
    return result
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        # Always check the most restrictive condition first
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass
