# The Pancake Problem
## Instructions to run and test
From the root directory, run the following command in the 
command line:
```
python main.py
```
Upon startup, the user will be asked how many pancakes they
would like to make. After entering the number of pancakes, 
the user will input the size of each pancake relative to 
the other pancakes in the stack. This number must be less
than the total number of pancakes, greater than 0, and not
equal to any number in the stack already. The stack will be 
printed as it is built. Once the stack is built, the user 
can select which algorithm they would like to run. The user
can enter 1 for A* implementation, or 2 for Uniform Cost Search.

In the example below, 2 is at the bottom of the stack of 3
pancakes created.
```
How many pancakes would you like to make?3
Building your stack :  []
Enter the size of the pancake:2
Building your stack :  [2]
Enter the size of the pancake:1
Building your stack :  [2, 1]
Enter the size of the pancake:3
Here is your initial pancake stack: 

[2, 1, 3]
1. A*
2. Uniform Cost Search
Which algorithm would you like to use to search for the correct state?

```
Upon completion, the user will see the actions
selected by the algorithm to achieve the goal.
```
Which algorithm would you like to use to search for the correct state?1
Initial Stack :  [2, 1, 3]
Flipping at index  2
Resulting stack  0 :  [2, 1, 3]
Flipping at index  0
Resulting stack  1 :  [3, 1, 2]
Flipping at index  1
Resulting stack  2 :  [3, 2, 1]
```
## Search Problem Definitions
### Initial State
Set by the user per the instructions above.

### Possible Actions Available
There are n possible actions available at each iteration of this program,
where n is the number of pancakes selected by the user. This represents
the number of positions in the stack at which the program can flip.

### Successor Function
The successor function flip() takes as input the stack
of pancakes and the position at which to flip, then flips the pancakes
above that position, reversing the order of that subset of pancakes.

### Goal Test
The goal test goal_test() takes as input the stack of 
pancakes and returns True iff every pancake in the 
stack is smaller than the pancake below it.

### Path Cost Function

#### A*
A* implementation uses the gap heuristic to 
assign costs to paths. The gap heuristic represents
the total number of "gaps" that exist between the 
state and the goal_state, which should have no gaps. 
Gaps refer to the number of adjacent sets of pancakes that 
should not be adjacent. When paths get weighted in A*,
this heuristic is added to a backward cost representing the 
cost to undo the previous flip if the program needs to backtrack.
#### UCS
Uniform Cost Search is an uninformed search algorithm,
so it has no knowledge of the goal state, and therefore
cannot use the gap heuristic. Instead, it uses the
number of flips required to weight the paths. This means
flipping only pancakes at the top of the stack will be
cheaper than flipping the entire stack. As running this
program shows, UCS can be used to solve this problem; however,
an informed search algorithm like A* can find the solution
faster and with fewer actions.

## Design
### External Libraries
This program imports heapq to use a heap to 
build the custom Priority Queue class.
### Project Structure
This project is split into 4 python files:
```
main.py: File for running the project, implementing the UI
a_star.py: Implements a* algorithm
ucs.py: Implements uniform cost search algorithm
utility.py: Implements logic that is shared by ucs and
            a_star (Node, Priority Queue, flip(), goal_
            test(), and get_solution() for returning
            solution steps.

## What I learned
1. Search agent design
2. Uninformed search
3. Informed search
4. Priority queue implementation with heapq
```
