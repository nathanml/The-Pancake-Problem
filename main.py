"""
Nathan Maher Levy

Main File for running program and providing user interface.
"""
from a_star import a_star
from ucs import uniform_cost_search

pancakes = []
print("Welcome to the pancake flipping program! Let's make pancakes\n")
num_pancakes = int(input("How many pancakes would you like to make?"))
size = 0
for i in range(num_pancakes):
    print("Building your stack : ", pancakes)
    size = int(input("Enter the size of the pancake:"))
    if size > num_pancakes or size < 1 or pancakes.__contains__(size):
        print("Invalid size, please pick a size between 1 and the number of"
              "pancakes. Please pick a unique size:")
        raise ValueError
    else:
        pancakes.append(size)
print("Here is your initial pancake stack: \n")
print(pancakes)
selection = 0
while selection != 1 and selection != 2:
    print("1. A*")
    print("2. Uniform Cost Search")
    selection = int(input("Which algorithm would you like to use to search for the correct state?"))
if selection == 1:
    a_star(pancakes)
else:
    uniform_cost_search(pancakes)
