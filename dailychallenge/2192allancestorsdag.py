from collections import defaultdict
class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        # run dfs on each node 
        # we can bulid the graob in opposite order 
        graph = defaultdict(list) # allows for null values in a dictionary \
        for parent,child in edges:
            graph[child].append(parent)

        ancestors = [[] for _ in range(n)]

        def dfs(node, ancestors):
            # the key in dfs is to keep going until there is no node left
            if ancestors[node]:
                return ancestors[node]

            for parent in graph[node]:
                ancestors[node].extend(dfs(parent, ancestors))

            ancestors[node].extend(graph[node])
            
            ancestors[node] = sorted(set(ancestors[node]))
            
            return ancestors[node]


        for node in range(n):
            dfs(node, ancestors)

        pass
    
if __name__ == '__main__':
    s= Solution()
    s.getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])