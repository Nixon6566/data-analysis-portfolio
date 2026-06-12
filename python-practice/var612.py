'''FIZZ BUZZ
The problem is simple. Print out every number between 1 and 100, one
number per line, but if the number is divisible by three, print out "Fizz";
if the number is divisible by five, print out "Buzz"; and if the number is
divisible by both three AND five, print out FIZZ BUZZ.
Now we need to break it down further and check to see if x is divisible
by JUST 3 or JUST 5. Sounds like a job for Elif. '''

for x in range(1, 101):
	if x % 3 == 0 and x % 5 == 0:
		print (f"{x} FIZZ BUZZ!")
	elif x % 3 == 0:
		print (f"{x} FIZZ")
	elif x % 5 == 0:
		print (f"{x} BUZZ")
	else:
		print (x)
