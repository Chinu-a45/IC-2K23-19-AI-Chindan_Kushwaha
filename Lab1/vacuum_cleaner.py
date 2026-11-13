def vacuum_cleaner(environment, start="A"):
    if start not in environment:
        raise ValueError("Starting room must exist in environment")
    state = dict(environment)
    location = start
    actions = []
    rooms = list(state)
    while any(status != "Clean" for status in state.values()):
        if state[location] not in ("Clean", "Dirty"):
            raise ValueError("Room status must be Clean or Dirty")
        if state[location] == "Dirty":
            state[location] = "Clean"
            actions.append(f"Suck dirt in {location}")
        else:
            location = rooms[(rooms.index(location) + 1) % len(rooms)]
            actions.append(f"Move to {location}")
    return state, actions

def main():
    final_state, actions = vacuum_cleaner({"A": "Dirty", "B": "Dirty"})
    print("Actions:")
    for action in actions:
        print("-", action)
    print("Final state:", final_state)

if __name__ == "__main__":
    main()
