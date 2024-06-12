from collections import deque
def minMutation(startGene, endGene, bank):
    """
    :type startGene: str
    :type endGene: str
    :type bank: List[str]
    :rtype: int
    """
    # idea create a queue
    if startGene == endGene:
        return 0

    
           
    def findEditDistance(gene1, gene2):
        return sum(1 for a, b in zip(gene1, gene2) if a != b)
    

    min_mutations = float('inf')
    for r in bank:
        d = findEditDistance(startGene, r)
        if d ==1:
            new_bank = list(set(bank) - {r})
            s = minMutation(r, endGene, new_bank)
            if s != float('inf'):
                min_mutations = min(min_mutations, 1 + s)
    return min_mutations if min_mutations != float('inf') else -1



    # now everything is sorted

print(minMutation("AACCGGTT", "AAACGGTA",["AACCGGTA","AACCGCTA","AAACGGTA"]))