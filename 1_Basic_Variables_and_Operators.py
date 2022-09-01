
lovely_loveseat_description = "Dark Brown leather loveseat"
lovely_loveseat_price = 200

lovely_chair_description = "large reclining chair with armrests"
lovely_chair_price = 50

lovely_desk_description = "medium size L-shaped wooden desk"
lovely_desk_price = 100

sales_tax = 0.0825

customer_total = 0
customer_itemization = ""

continue_buying = True

while continue_buying:

    item = input("Do you want a loveseat, a chair, or a desk?\n")

    if item == "loveseat":
        customer_total += lovely_loveseat_price + lovely_loveseat_price * sales_tax
        customer_itemization += lovely_loveseat_description
    elif item == "chair":
        customer_total += lovely_chair_price + lovely_chair_price * sales_tax
        customer_itemization += lovely_chair_description
    elif item == "desk":
        customer_total += lovely_desk_price + lovely_desk_price * sales_tax
        customer_itemization += lovely_desk_description

    ask = input("Would you like anything else?\n")

    if ask == "yes":
        customer_itemization += ", "

    else:
        continue_buying = False

print(f"Your items: {customer_itemization}")
print(f"Total cost: {customer_total}")




    
