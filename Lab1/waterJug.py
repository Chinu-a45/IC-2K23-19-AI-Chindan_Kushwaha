from collections import deque


def water_jug_problem(capacity_a, capacity_b, target):
    initial_state = (0, 0)
    queue = deque()
    queue.append((initial_state, []))
    visited = set()
    visited.add(initial_state)

    while queue:

        current_state, path = queue.popleft()
        a, b = current_state

        if current_state == (target, 0):
            print("Solution found!\n")

            print("Initial State: (0, 0)")

            for i, (state, action) in enumerate(path, start=1):
                print(f"{i}. {action} -> {state}")

            return

        possible_moves = []

        possible_moves.append(
            ((capacity_a, b), "Fill Jug A")
        )

        possible_moves.append(
            ((a, capacity_b), "Fill Jug B")
        )

        possible_moves.append(
            ((0, b), "Empty Jug A")
        )

        possible_moves.append(
            ((a, 0), "Empty Jug B")
        )

        amount = min(a, capacity_b - b)

        possible_moves.append(
            ((a - amount, b + amount),
             "Pour Jug A -> Jug B")
        )

        amount = min(b, capacity_a - a)

        possible_moves.append(
            ((a + amount, b - amount),
             "Pour Jug B -> Jug A")
        )

        for new_state, action in possible_moves:

            if new_state not in visited:

                visited.add(new_state)

                new_path = path + [(new_state, action)]

                queue.append((new_state, new_path))

    print("No solution exists.")


capacity_a = 4
capacity_b = 3
target = 2

water_jug_problem(capacity_a, capacity_b, target)