import random


with open('nums.txt', 'w') as f:
    [f.write(str(random.randint(0, 100000000))+"\n") for i in range(10000)]
