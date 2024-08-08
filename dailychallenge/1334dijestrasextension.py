
import heapq
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """

        # city count
        city_count = {}

        # need to create an edge matrix
        node_edges = [[] for _ in range(n)]
        for u, v, w in edges:
            node_edges[u].append((v, w))
            node_edges[v].append((u, w))

        # need to run dijestras for every node. 
        distance_matrix = [[ 0 if i==j else distanceThreshold +1 for i in range(n)] for j in range(n)]
        
        for current_node in range(n):
            # now we run dijestras
            pq = []
            explored = []
            heapq.heappush(pq, (0,current_node)) 

            while pq:
                curr_dist, exploring_node = pq.pop(0)

                # for each edge see if the know distance is less 
                for node, dist in node_edges[exploring_node]:
                    # for each node compare the known distance to the 
                    if curr_dist + dist < distance_matrix[current_node][node]:
                        # need to add to pq
                        heapq.heappush(pq, (curr_dist+ dist, node))
                        distance_matrix[current_node][node] =  curr_dist + dist

                
                explored.append(exploring_node)

            for a in distance_matrix[current_node]:
                if a != 0 and a <= distanceThreshold:
                    city_count[current_node] = city_count.get(current_node, 0) + 1
        
        b = sorted(city_count.items(), key= lambda x: (x[1],-x[0]))
        return b[0][0]
                    

        

if __name__ == '__main__':
    S = Solution()
    n = 6
    edges = [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]]
    distanceThreshold = 417
    print(S.findTheCity(n,edges,distanceThreshold)) 
