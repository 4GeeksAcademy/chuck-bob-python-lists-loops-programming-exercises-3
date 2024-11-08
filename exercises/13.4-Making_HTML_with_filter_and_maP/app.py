all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here

def sexy_colors(color):
    return color["sexy"]

true_sexy_colors = list(filter(sexy_colors, all_colors))

# print(true_sexy_colors)



def format_color(color):
    # Your code here
    color_list = color["label"]
    return f"<li>{color_list}<li>"


new_color_list = list(map(format_color, true_sexy_colors))

print(new_color_list)
