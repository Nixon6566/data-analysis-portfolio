'''Using Continue'''

num = 0
while num < 10:
    num += 1
    if num == 5:
        continue  # Skip printing when num is 5
    print(num)