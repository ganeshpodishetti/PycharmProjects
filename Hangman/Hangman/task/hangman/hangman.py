# Write your code here
import random
a = ['python', 'java', 'kotlin', 'javascript']
b = random.choice(a)
c = input()
if c == b:
    print('You survived')
else:
    print('You are hanged!')
