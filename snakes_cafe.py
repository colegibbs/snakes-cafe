# render dictionaries
def create_dictionary(*dish_list):
  dishes = {}
  for list in dish_list:
    for dish in list:
      dishes[dish] = 0
  return dishes

# loop and print functions for the dish lists

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
