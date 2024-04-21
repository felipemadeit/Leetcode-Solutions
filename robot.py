orders = input()

list_of_orders = orders.split(" ")

up = list_of_orders.count("up")
down = list_of_orders.count("down")
left = list_of_orders.count("left")
right = list_of_orders.count("right")


unique_orders = []

for order in list_of_orders:
    if order not in unique_orders:
        unique_orders.append(order)


final_string = ''

for orderss in unique_orders:
    if orderss == 'up':
        if up == 1:
            final_string += "^"
        else:
            final_string += f"^{up}"
    elif orderss == 'down':
        if down == 1:
            final_string += "v"
        else:
            final_string += f"v{down}"      
    elif orderss == "left":
        if left == 1:
            final_string += "<"
        else:
            final_string += f"<{left}"
    elif orderss == "right":
        if right == 1:
            final_string += ">"
        else:   
            final_string += f">{right}"
    elif orderss == ' ':
        final_string += ''
        
print(final_string)