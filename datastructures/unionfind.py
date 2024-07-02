# this is a unionfind datastructure that can find easily detect cycles in a graph in a mst algo
class Unionfind():
    def __init__(self, n) -> None:
        # initially we start with a array of parents
        # this tells u what each nodes parent is
        self.parents = list(range(n))
        self.size = [1] *n
        # also we have an array of sizes 
        # this tells you the size of each dijoint set
        # node 1 will have parent at self.parents[1]
    def find(self, node):
        # this returns the representitivle node for each node passed in
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node]) # builds the parents as we find
        return self.parents[node]

    def union(self, node1, node2):
        
        repnode1 = self.find(node1)
        repnode2 = self.find(node2)

        if repnode1 == repnode2:
            # nodes are in the same set
            return 
        
        if self.size[repnode1] < self.size[repnode2]:
            self.size[repnode2] += self.size[repnode1]
            self.parents[repnode1] = repnode2

        else:
            self.size[repnode1] += self.size[repnode2]
            self.parents[repnode2] = repnode1


if __name__ == '__main__':
    n = 5
    uf = Unionfind(n)

    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    print(uf.find(2))  # Output: 0 (since 0 is the root of the set containing 2)
    print(uf.find(4))  # Output: 3 (since 3 is the root of the set containing 4)


