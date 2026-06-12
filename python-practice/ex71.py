def fizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return f"{x} is FIZZ BUZZ!"
    elif x % 3 == 0:
        return f"{x} is FIZZ"
    elif x % 5 == 0:
        return f"{x} is BUZZ"
    else:
        return f"{x} is Boring"

# Prompt the user
num = int(input("Enter a number: "))

# Call the function and show the result
print(fizz_buzz(num))

'''Re-write the fizz_buzz function to prompt a user to enter a
number and then return the function result'''