# render dictionaries
def create_dictionary(*dish_list):
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


print("""Entrees
-------""")

#loop function to render entrees

print("""Desserts
--------""")

#loop function to render desserts

print("""Drinks
------""")
 
 #loop function to render drinks

print("""***********************************
** What would you like to order? **
***********************************""")

# while loop that handles input 
  # needs to input("> ")
  #plural vs non-plural
