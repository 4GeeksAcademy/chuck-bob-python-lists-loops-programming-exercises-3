all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here

def resulting(x):
    return x[0] == "R"

resulting_names = list(filter(resulting, all_names))

print(resulting_names)




