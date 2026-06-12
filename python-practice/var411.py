
#MCHOOSE YOUR OWN ADVENTURE

'''from os import system
system ("clear")
'''
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear_screen()

print("Welcome To Choose Your Own Adventure!")
print("The goal is to find the Python Princess ...")
name = input ("Enter Your Name:")
name = name.lower()
#system("clear")
clear_screen()
print("You're standing in front of two doors...")
print("Do you want the door on the left or right?")
question = input().lower()
if question == "left":
#	system("clear")
	clear_screen()
	print("You fell into a pit and died! GAME OVER")
elif question == "right":
#	system("clear")
	clear_screen()
	print(f"Congratulations {name.capitalize()} you found ")
	print("the Python Princess! YOU WIN!")
else:
#	system("clear")
	clear_screen()
	print("Sorry, I don't recognize your response GAME OVER")