"""
File contains functions/classes shared by UCS and A* Implementation

flip() -> Flips input pancake stack at specified index
goalTest() -> Checks if pancake stack is goal state
Node -> For representing program state
Priority Queue -> Custom priority queue class using heaps
"""
import heapq


# Splits the pancake stack at the position
# specified. Flips all pancakes above that
# position by reversing the subset of the
# list.
def flip(pancake_stack: list, position: int):
    tmp_stack = pancake_stack.copy()
    flip_stack = []
    for i in range(len(pancake_stack)):
        # Don't flip pancakes that don't need to be flipped
        if i < position:
            flip_stack.append(pancake_stack[i])
        # Flip pancakes above specified position
        else:
            flip_stack.append(tmp_stack.pop())
    return flip_stack


# Test for checking goal state.
def goal_test(pancake_list: list):
    # Loop through pancake list
    for i in range(len(pancake_list) - 1):
        # If pancake is smaller than the next, FAIL
        if pancake_list[i] < pancake_list[i + 1]:
            return False
    # If pancakes are ordered, SUCCEED
    return True


# Function used by A* and UCS to print
# the solution implementation.
def get_solution(current_state, initial_state):
    solution = []
    flips = []
    while current_state is not initial_state:
        solution.append(current_state.current_stack)
        flips.append(current_state.last_flip)
        current_state = current_state.parent
    for i in range(len(solution)):
        if i == 0:
            print("Initial Stack : ", initial_state.current_stack)
            print("Flipping at index ", flips.pop())
            print("Resulting stack ", i, ": ", solution.pop())
        else:
            print("Flipping at index ", flips.pop())
            print("Resulting stack ", i, ": ", solution.pop())
    return solution


'''
Node:
    Current Stack: List of integers representing ordering of the pancakes
    Parent: Previous state before flip
    Priority: Current weight in priority queue
    last_flip: The index which was last flipped.
'''


class Node:
    def __init__(self, current_stack, parent, priority, last_flip):
        # Represents current stack and previous stacks to get there
        self.current_stack = current_stack
        # Parent Node
        self.parent = parent
        self.priority = priority
        self.last_flip = last_flip

    # Less than comparator. Required for priority queue
    def __lt__(self, other):
        return self.priority < other.get_priority()

    def get_priority(self):
        return self.priority


'''
PriorityQueue:
    Queue: List of key value pairs <Priority, Node>
'''


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    # for checking if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # for inserting a node in the queue
    def push(self, element, priority):
        heapq.heappush(self.queue, (priority, element))

    # for removing the next node from the queue
    def pop(self):
        if self.is_empty():
            raise IndexError("Empty priority queue")
        else:
            return heapq.heappop(self.queue)[1]

    # for removing a specific node from the queue
    def remove(self, item):
        self.queue.remove(item)

    # for adjusting the priority of a node in the queue
    def update_priority(self, item, new_priority):
        self.remove(item)
        self.push(item, new_priority)

    def contains(self, item):
        for i in range(len(self.queue)):
            if self.queue[i] == item:
                return True
        return False

    def get_cost(self, child):
        for i in range(len(self.queue)):
            if self.queue[i] == child:
                return self.queue[i][1]
