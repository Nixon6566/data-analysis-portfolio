'''FIZZ BUZZ
The problem is simple. Print out every number between 1 and 100, one
number per line, but if the number is divisible by three, print out "Fizz";
if the number is divisible by five, print out "Buzz"; and if the number is
divisible by both three AND five, print out FIZZ BUZZ. '''

for x in range(1, 101):
	if x % 3 == 0 and x % 5 == 0:
		print (f"{x} FIZZ BUZZ!")
	else:
		print (x)

	