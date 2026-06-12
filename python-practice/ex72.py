def fizz_buzz():
    for x in range(1, 100):
        if x % 3 == 0 and x % 5 == 0:
            print(f"{x} is FIZZ BUZZ!")
        elif x % 3 == 0:
            print(f"{x} is FIZZ")
        elif x % 5 == 0:
            print(f"{x} is BUZZ")
        else:
            print(x)

fizz_buzz()



'''Write some code using the same fizz_buzz function but have it
print out all numbers between 1 and 100 by calling the function
100 times.'''




