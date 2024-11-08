incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here

def data_transformer(array):
    return list(map(lambda name_obj: f"{name_obj['name']} {name_obj['last_name']}", array))


print(data_transformer(incoming_ajax_data))
