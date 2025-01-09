"""
Nathan Maher Levy

Implementation of Uniform Cost Search
"""
import utility as util


def uniform_cost_search(pancake_list: list):
    num_iterations = 0
    stack_size = len(pancake_list)
    initial_state = util.Node(pancake_list, None, None, None)
    visited = [pancake_list]
    frontier = util.PriorityQueue()

    # Initialize the frontier
    for i in range(stack_size):
        # Create a new state for each possible configuration
        new_stack = util.flip(pancake_list, i)
        new_state = util.Node(new_stack, initial_state, stack_size - i, i)
        frontier.push(new_state, new_state.priority)

    while True:
        # Check frontier for next state
        if frontier.is_empty():
            return "FAILURE: No solution found."

        current_state = frontier.pop()
        visited.append(current_state.current_stack)

        # Perform Goal Test on state
        # If Goal State found
        if util.goal_test(current_state.current_stack):
            return util.get_solution(current_state, initial_state)

        # For each child, create new state
        for i in range(stack_size):
            new_stack = util.flip(current_state.current_stack, i)
            new_state = util.Node(new_stack, current_state, stack_size - i, i)

            # If the new state is not in frontier or visited, add to frontier
            if frontier.contains(new_state) is False and visited.count(new_stack) <= 0:
                frontier.push(new_state, stack_size - i)
            elif frontier.contains(new_state) and frontier.get_cost(new_state) > stack_size - i:
                frontier.remove(new_state)
                frontier.update_priority(new_state, stack_size - i)
