# Python3 program to implement Disjoint Set Data 
# Structure. 

class DisjSet: 
    def __init__(self, n): 
        # Initialize Parent array 
        self.Parent = list(range(1,n+1)) 
  
        # Initialize Size array with 1s 
        self.Size = [1] * n 
  
    # Function to find the representative (or the root node) for the set that includes i 
    def find(self, i): 
        if self.Parent[i-1] != i: 
            # Path compression: Make the parent of i the root of the set 
            self.Parent[i-1] = self.find(self.Parent[i-1]) 
        return self.Parent[i-1] 
  
    # Unites the set that includes i and the set that includes j by size 
    def Union(self, i, j): 
        # Find the representatives (or the root nodes) for the set that includes i 
        irep = self.find(i) 
  
        # And do the same for the set that includes j 
        jrep = self.find(j) 
  
        # Elements are in the same set, no need to unite anything. 
        if irep == jrep: 
            return
  
        # Get the size of i’s tree 
        isize = self.Size[irep-1] 
  
        # Get the size of j’s tree 
        jsize = self.Size[jrep-1] 
  
        # If i’s size is less than j’s size 
        if isize < jsize: 
            # Then move i under j 
            self.Parent[irep-1] = jrep 
  
            # Increment j's size by i's size 
            self.Size[jrep-1] += self.Size[irep-1] 
            return self.Size[jrep-1]
        # Else if j’s size is less than i’s size 
        else: 
            # Then move j under i 
            self.Parent[jrep-1] = irep 
  
            # Increment i's size by j's size 
            self.Size[irep-1] += self.Size[jrep-1] 
            return self.Size[irep-1]


class Solution(object):
    def addSeperateEdges(self, edgesSep, Dijset, n, edgelen):
        for edge in edgesSep:
            _, node1, node2 = edge
            
            size = Dijset.Union(node1, node2)
            if size == n:
                return edgelen - (2*(n-1))
        return -1

    def maxNumEdgesToRemove(self, n, edges):
        

        # I think we need to construct a graph for alice and a graph for bob
        # so I create a disjoint set for alice and bob by first using all the edges that both of them share 
        edgesTogether = [x for x in edges if x[0] == 3]
        edgesAlice = [x for x in edges if x[0] == 1]
        edgesBob = [x for x in edges if x[0] == 2]


        # so I create a dijoint set of size n for alice and bob
        AliceDijSet = DisjSet(n)
        BobDijSet = DisjSet(n)
		
        # so now start with the edges together, after each edges together check if rank is n
        for edge in edgesTogether:
            _, node1, node2 = edge
            sizeAlice = AliceDijSet.Union(node1, node2)
            sizeBob = BobDijSet.Union(node1, node2)
            if sizeAlice == n and sizeBob == n:
                return len(edges) - (n - 1)
        
        # now we add each edge of alice in until size
        edgelen = len(edges)

        return min(self.addSeperateEdges(edgesAlice,AliceDijSet,n,edgelen), self.addSeperateEdges(edgesBob, BobDijSet,n, edgelen))


        # after I add an edge, I check the size of each set to see if it is = to n 
        # at this point we start adding the edges for both alice and bob
        # i think we can add random until we have both of their disjoint sets the size we want to be 
        # the larger size of the two sets is the minimum amount of edges we can remove 
        

if __name__ == '__main__':
    s = Solution()
    # n = 4
    # edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
    n=2
    edges = [[1,1,2],[2,1,2],[3,1,2]]


    print(s.maxNumEdgesToRemove(n,edges))
