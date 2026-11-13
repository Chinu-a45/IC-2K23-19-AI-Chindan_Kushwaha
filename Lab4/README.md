# Lab 4 — Knowledge Representation and Logical Reasoning

**Aim:** Represent facts and relations using predicates, semantic networks,
frames and conceptual dependency, then infer new facts with rules.

**Algorithm:** Store known facts; repeatedly apply forward-chaining rules whose
premises are all known; add each new conclusion until no rule adds a fact.

**Run:** `python Lab4/knowledge_representation.py`.

**Results:** Console output displays predicate tuples, semantic-network edges,
a Student frame, a simplified ATRANS conceptual-dependency representation and
facts inferred by forward chaining.

**Performance analysis:** This is a symbolic reasoning example. Evaluate
expressiveness, rule coverage and number of inference rounds rather than
classification accuracy.

**Learning outcomes:** Knowledge structures, relations, frames, actions,
logical inference and rule-based reasoning.
