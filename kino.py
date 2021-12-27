from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

N = 10
ra = 0
my_number = set()

while ra != N:

    rand_number = randrange(1, 50)
    if rand_number not in my_number:
        my_number.add(rand_number)
        ra += 1

print(my_number)
