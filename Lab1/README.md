# Lab 1 — AI Environment, Production Systems and State-Space Problems

**Aim:** Model AI problems as states, actions, rules and goal tests.

**Algorithm:** The production-system program repeatedly selects the first
applicable rule. Water Jug and Missionaries & Cannibals use BFS over legal
states. The vacuum agent senses the current room and applies Suck or Move.

**Programs:** `production_system.py`, `water_jug.py`,
`missionaries_cannibals.py`, `vacuum_cleaner.py`.

**Run:** `python Lab1/production_system.py` (repeat for each file).

**Results:** The water-jug program finds a shortest state path to 2 litres.
The missionaries-and-cannibals program finds a legal crossing sequence. The
vacuum agent cleans both rooms. Console output is reproducible.

**Performance analysis:** BFS is complete for these finite state spaces and
returns a shortest path in number of actions. Time and explored states are
printed by the water-jug program. The other examples are small deterministic
demonstrations.

**Learning outcomes:** State-space modelling, production rules, legal-state
constraints, goal testing and agent actions.
