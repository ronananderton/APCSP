teacher = "Ms Orret"
print(teacher)

print(25*3+10/2)

print(10%4)


lovely_loveseat_description = "This is a wonderful loveseat"
lovely_loveseat_price = 100

lovely_chair_description = "This is a wonderful chair"
lovely_chair_price = 30

lovely_desk_description = "This is a wonderful desk"
lovely_desk_price = 50

sales_tax = .0825

customer_total = 0
customer_itemization = ""

item = input("Do you want a loveseat, a chair, or a desk?")
if item == "loveseat":
    customer_total += loevely_loveseat_price
    customer_itemization += lovely_loveseat_description
if item == "chair":
    customer_total += loevely_chair_price
    customer_itemization += lovely_chair_description
if item == "desk":
    customer_total += loevely_desk_price
    customer_itemization += lovely_desk_description




    