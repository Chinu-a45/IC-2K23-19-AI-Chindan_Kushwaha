# AI Lab – Lab 1

## Lab 1: AI Environment Setup, Production Systems and Water Jug Problem

---

## Experiment 1: Production Rule System

### Aim
To understand the concept of a Production Rule System and implement rule-based decision making using Python.

### Problem Statement
To represent knowledge using **IF–THEN production rules** and make a decision based on given conditions.

### Algorithm
1. Define the required input conditions.
2. Define the production rules.
3. Check the conditions one by one.
4. Apply the matching rule.
5. Display the resulting decision.

### Results / Output
The Production Rule System successfully applies the defined rules and produces the appropriate decision based on the given conditions.

### Performance Analysis
The rules are checked sequentially. The execution time is small because only a limited number of rules are used.

### Screenshots / Graphs / Model Visualization
Add a screenshot of the program and its output.

### Learning Outcomes
- Understood Production Rule Systems.
- Understood IF–THEN rules.
- Learned basic rule-based decision making.
- Implemented a simple AI reasoning system.

---

## Experiment 2: Water Jug Problem

### Aim
To understand the Water Jug Problem and solve it using **State Space Representation** and search.

### Problem Statement
Given a 4-litre jug and a 3-litre jug, obtain exactly **2 litres in the 4-litre jug** while keeping the 3-litre jug empty.

**Initial State:** `(0, 0)`  
**Goal State:** `(2, 0)`

### Algorithm
1. Start from the initial state `(0, 0)`.
2. Represent each state as `(Jug A, Jug B)`.
3. Generate states using the allowed operations: fill, empty, and pour.
4. Store visited states to avoid repetition.
5. Search the state space until `(2, 0)` is reached.
6. Display the sequence of operations.

### Results / Output
The problem is successfully solved and the final state obtained is:

`(2, 0)`

This means Jug A contains 2 litres and Jug B contains 0 litres.

### Performance Analysis
The state space is small, with at most **20 possible states** for 4-litre and 3-litre jugs. Using visited states avoids repeated exploration.

### Screenshots / Graphs / Model Visualization
Add a screenshot of the program output and, if required, a state-space diagram.

### Learning Outcomes
- Understood AI problem formulation.
- Understood State Space Representation.
- Learned initial and goal states.
- Understood state transitions and operators.
- Applied search to solve an AI problem.

---

## Overall Result

Both experiments were successfully implemented and demonstrated the basic concepts of **Production Systems, Rule-Based Reasoning, State Space Representation, and intelligent problem solving**.
