# Remember to import random function here
import random
my_list = [4, 5, 734, 43, 45]

# The magic goes below

for i in range(0,10):
    my_list.append(random.randint(1, 1000))

print(my_list)
