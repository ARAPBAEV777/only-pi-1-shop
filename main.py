import random
from itertools import count

num1 =  int(input(''))
num2 =  int(input(''))

word = random.randint(num1,num2)

count = 0

while True:
    number = int(input())
    if number == word:
        print()