from dataclasses import dataclass
from typing import Callable

@dataclass
class Rule:
    name: str
    condition: Callable[[dict], bool]
    action: Callable[[dict], None]

def run_system(state, rules, max_steps=50):
    current = dict(state)
    history = []
    for _ in range(max_steps):
        rule = next((r for r in rules if r.condition(current)), None)
        if rule is None:
            return current, history
        before = current.copy()
        rule.action(current)
        if current == before:
            raise RuntimeError(f"Rule '{rule.name}' did not change the state")
        history.append((rule.name, current.copy()))
    raise RuntimeError("Production system exceeded maximum steps")

def main():
    rules = [
        Rule("Boil water", lambda s: not s["water_hot"],
             lambda s: s.update(water_hot=True)),
        Rule("Add tea", lambda s: s["water_hot"] and not s["tea_added"],
             lambda s: s.update(tea_added=True)),
        Rule("Serve tea", lambda s: s["tea_added"] and not s["served"],
             lambda s: s.update(served=True)),
    ]
    final_state, history = run_system(
        {"water_hot": False, "tea_added": False, "served": False}, rules)
    for number, (name, state) in enumerate(history, 1):
        print(f"{number}. {name}: {state}")
    print("Goal reached:", final_state["served"])

if __name__ == "__main__":
    main()
