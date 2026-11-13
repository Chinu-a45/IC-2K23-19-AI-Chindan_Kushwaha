from dataclasses import dataclass, field

@dataclass
class Frame:
    name: str
    slots: dict = field(default_factory=dict)

def forward_chain(initial_facts, rules):
    facts = set(initial_facts)
    changed = True
    while changed:
        changed = False
        for premises, conclusion in rules:
            if set(premises).issubset(facts) and conclusion not in facts:
                facts.add(conclusion); changed = True
    return facts

def main():
    print("PREDICATE REPRESENTATION")
    predicates = [("Student", ("Chindan",)), ("Enrolled", ("Chindan", "MCA")),
                  ("Studies", ("Chindan", "Artificial Intelligence"))]
    for name, args in predicates: print(f"{name}{args}")

    print("\nSEMANTIC NETWORK")
    edges = [("Chindan", "is-a", "Student"),
             ("Student", "enrolled-in", "MCA"),
             ("MCA", "contains", "Artificial Intelligence")]
    for source, relation, target in edges:
        print(f"{source} --{relation}--> {target}")

    print("\nFRAME REPRESENTATION")
    student = Frame("Student", {"name": "Chindan", "course": "MCA",
                                "role": "Learner", "subject": "AI"})
    print(student)

    print("\nCONCEPTUAL DEPENDENCY (simplified ATRANS example)")
    print("ATRANS(actor=Chindan, object=Book, from=Library, to=Chindan)")

    print("\nRULE-BASED INFERENCE")
    facts = {("enrolled", "Chindan", "MCA"),
             ("course_has_subject", "MCA", "AI"),
             ("has_prerequisite", "AI", "Programming")}
    rules = [
        ([("enrolled", "Chindan", "MCA"),
          ("course_has_subject", "MCA", "AI")],
         ("studies", "Chindan", "AI")),
        ([("studies", "Chindan", "AI"),
          ("has_prerequisite", "AI", "Programming")],
         ("should_know", "Chindan", "Programming"))
    ]
    for fact in sorted(forward_chain(facts, rules)): print(fact)

if __name__ == "__main__":
    main()
