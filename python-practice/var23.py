
'''
Table Of Assignment Operators
= Assigns something from the right to the left
+= Adds and Assigns
-= Subtracts and Assigns
*= Multiplies and Assigns
/= Divides and Assigns
%= Modulus and Assigns
**= Exponents and Assigns
input()
By default, input() thinks you're entering a string (text) when you enter
things. You have to tell it that you're looking for a number (integer).
You can do that using the int() function…(int as in integer).
'''

num1 = input("Enter A Number: ")
num2 = input("Enter Another Number: ")
print(f'{num1} + {num2} = {int(num1) + int(num2)}')