sample_list = [45, 67, 87, 23, 5, 32, 60]

# Your code below

newlist = [0,0,0,0,0,0,0]

for i in range(len(sample_list)):
    newlist[(len(sample_list)-i-1)] = sample_list[i]

print(newlist)