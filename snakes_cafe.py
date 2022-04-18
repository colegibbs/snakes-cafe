# render dictionaries
def create_dict(*dish_list):
  dishes = {}
  for list in dish_list:
    for dish in list:
      dishes[dish] = 0
  return dishes

# loop and print functions for the dish lists
def print_dishes(dish_type):
  for dish in dish_type:
    print(dish)

# dish types
appetizers =["Wings", "Cookies", "Spring Rolls"]
entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
desserts = ["Ice Cream", "Cake", "Pie"]
drinks = ["Coffee", "Tea", "Unicorn Tears"]

print("""$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")

print("""Appetizers
----------""")

#loop function to render appetizers
print_dishes(appetizers)

print("""Entrees
-------""")

#loop function to render entrees
print_dishes(entrees)

print("""Desserts
--------""")

#loop function to render desserts
print_dishes(desserts)

print("""Drinks
------""")
 
#loop function to render drinks
print_dishes(drinks)

print("""***********************************
** What would you like to order? **
***********************************""")

# while loop that handles input 
  # needs to input("> ")
  #plural vs non-plural
dishes = create_dict(appetizers, entrees, desserts, drinks)

while True:
  order = input("> ")
  if order == "quit":
    break
  dishes[order] += 1
  if(order.endswith("s")):
    print(f'There is {dishes[order]} order of {order} in your order' if dishes[order] == 1 else f'There are {dishes[order]} orders of {order} in your order')
  elif dishes[order] == 1:
    print(f"There is {dishes[order]} {order} dish in your order")
  else:
    print(f"There are {dishes[order]} {order} dishes in your order")
  
