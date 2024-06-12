from itertools import combinations

def choose_k(n, k):
    # Generate a list of numbers from 0 to n-1
    elements = list(range(n))

    # Use itertools.combinations to generate all combinations
    all_combinations = list(combinations(elements, k))


    return all_combinations