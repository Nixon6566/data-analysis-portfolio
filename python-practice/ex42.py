'''
Write some code that asks for a person's full name (first and last
name) and then output their name with both first and last name
capitalized
'''
#capitalize() Capitalize just first letter

first_name = input("What is your first Name: ")
first_name = first_name.capitalize() 
last_name = input("What is your last Name: ")
last_name= last_name.capitalize() 
print(f'Hello {first_name} {last_name}')