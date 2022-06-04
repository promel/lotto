import random 
from sys import argv

LIMIT = 6
RANGE = 52
LINES = 3

print(argv)
for arg in argv:
    if '--limit' in arg:
        LIMIT = int(arg.split('--limit=')[1])   

    if '--range' in arg:
        RANGE = int(arg.split('--range=')[1])  

    if '--lines' in arg:
        LINES = int(arg.split('--lines=')[1])

    if '--type=powerball' in arg:
        LIMIT = 5

lines = []
for i in range(LINES):
    numbers = []
    while len(numbers) < LIMIT:
        number = random.randrange(1, 52)
        if number not in numbers:
            numbers.append(number)

    lines.append(numbers)

print(lines)