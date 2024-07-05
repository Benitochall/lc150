class Solution(object):
   
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """ 
        # step1: make a graph 
        graph = [[] for i in range(numCourses)]
        for ai, bi in prerequisites:
            graph[bi].append(ai)

        visited = [0] * numCourses
    
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for neibor in graph[node]:
                if not dfs(neibor):
                    return False
            visited[node] =2
            return True

            
        for i in range(numCourses):
            if visited[i] == 0:
                if dfs(i):
                    continue
                else:
                    return False
    
        return True
    
if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))