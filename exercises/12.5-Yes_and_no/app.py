the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

new_bools = []

for i in the_bools:
    if i == 1:
        new_bools.append("wiki")
    else:
        new_bools.append("woko")

print(new_bools)