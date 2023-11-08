############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Using sets to find common elements
# OK - 1 Nov 2023

fruit = {"orange", "apple", "banana", "cherry", "pineapple"}
print(fruit)

red_things = {"car", "hat", "apple", "cherry"}
print(red_things)

red_fruit = fruit.intersection(red_things)
print('Red fruit:', red_fruit)

no_red_fruit = fruit.difference(red_things)
print('Not red fruit:', no_red_fruit)

lots_of_things = fruit.union(red_things)
print('Everything:', lots_of_things)
