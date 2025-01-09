"""
Implementation of A* Search
"""
import utility as util


def a_star(pancake_list: list):
    stack_size = len(pancake_list)
    initial_state = util.Node(pancake_list, None, gap_heuristic(pancake_list), None)
    visited = [pancake_list]
    frontier = util.PriorityQueue()

    # Initialize the frontier
    for i in range(stack_size):
        # Create a new state for each possible configuration
        new_stack = util.flip(pancake_list, i)
        forward_cost = gap_heuristic(new_stack)
        backward_cost = stack_size - i + gap_heuristic(pancake_list)
        total_cost = forward_cost + backward_cost
        new_state = util.Node(new_stack, initial_state, total_cost, i)
        frontier.push(new_state, forward_cost + backward_cost)

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
            forward_cost = gap_heuristic(new_stack)
            backward_cost = stack_size - i + gap_heuristic(current_state.current_stack)
            total_cost = forward_cost + backward_cost
            new_state = util.Node(new_stack, current_state, total_cost, i)
            # If the new state is not in frontier or visited, add to frontier
            if frontier.contains(new_state) is False and visited.count(new_stack) <= 0:
                frontier.push(new_state, total_cost)
            # Else if child in frontier with higher cost, replace child in frontier
            elif frontier.contains(new_state) and frontier.get_cost(new_state) > total_cost:
                frontier.remove(new_state)
                frontier.update_priority(new_state, total_cost)


def gap_heuristic(current_stack: list):
    gap_value = 0
    for i in range(len(current_stack) - 1):
        current = current_stack[i]
        next_pancake = current_stack[i + 1]
        if current != next_pancake + 1 and next_pancake != current + 1:
            gap_value += 1
    return gap_value
