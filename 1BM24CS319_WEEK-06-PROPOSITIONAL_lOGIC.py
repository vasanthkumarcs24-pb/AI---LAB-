
import itertools

# 1. Define the implication operator
def implies(a, b):
    return not a or b


# 2. Define the Knowledge Base
def evaluate_kb(m):

    s1 = implies(m['Q'], m['P'])       # Q -> P
    s2 = implies(m['P'], not m['Q'])   # P -> ~Q
    s3 = m['Q'] or m['R']              # Q v R

    kb = s1 and s2 and s3

    return s1, s2, s3, kb


# 3. Define the queries
queries = {
    "R": lambda m: m['R'],
    "R -> P": lambda m: implies(m['R'], m['P']),
    "Q -> R": lambda m: implies(m['Q'], m['R'])
}


# 4. Generate and print the truth table
def print_truth_table():

    symbols = ['P', 'Q', 'R']

    headers = [
        'P', 'Q', 'R',
        'Q -> P', 'P -> ~Q', 'Q v R', 'KB',
        'R', 'R -> P', 'Q -> R'
    ]

    print("\n" + "=" * 105)
    print("             KNOWLEDGE BASE AND ENTAILMENT TRUTH TABLE")
    print("=" * 105)

    header_str = " | ".join(f"{h:^9}" for h in headers)
    print(header_str)
    print("-" * len(header_str))

    valid_models = []

    for values in itertools.product([False, True], repeat=3):

        m = dict(zip(symbols, values))

        # Evaluate KB sentences
        s1, s2, s3, kb = evaluate_kb(m)

        # Evaluate all queries
        q_values = [
            query_fn(m) for query_fn in queries.values()
        ]

        row = [
            m['P'], m['Q'], m['R'],
            s1, s2, s3, kb,
            *q_values
        ]

        row_str = " | ".join(
            f"{'T' if v else 'F':^9}" for v in row
        )

        if kb:
            valid_models.append(m)
            row_str += "  <-- KB MODEL"

        print(row_str)

    # 5. Display valid models
    print("\n" + "=" * 55)
    print("MODELS WHERE KB IS TRUE")
    print("=" * 55)

    for i, model in enumerate(valid_models, start=1):
        print(f"Model {i}: {model}")

    # 6. Display entailment results
    print("\n" + "=" * 55)
    print("ENTAILMENT RESULTS")
    print("=" * 55)

    print(f"{'Query':<12} {'Result':<15}")
    print("-" * 30)

    for name, query_fn in queries.items():

        # KB entails query if query is true
        # in every model where KB is true
        entails = all(
            query_fn(model) for model in valid_models
        )

        print(
            f"{name:<12} "
            f"{'YES' if entails else 'NO':<15}"
        )

    print("-" * 30)


# 7. Main program
print_truth_table()
