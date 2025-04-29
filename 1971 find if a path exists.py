class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Initialize dictionary of nodes/connections
        graph = {node:[] for node in range(n)}
        # print(graph)
        # add in eddges
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # print(graph)

        # now loop through each graph starting at source node
        #BFS
        # queue = [source]
        # visited = set()
        # while len(queue) >0:
        #     # print(f'current queue {queue}')
        #     current_node = queue.pop(0)
        #     if current_node == destination:
        #         return True
        #     for node in graph[current_node]:
        #         if node not in visited:
        #             queue.append(node)   
        #             visited.add(node)
        # return False
        #DFS

        visited = set()
        def visit(node):
            if node == destination:
                return True
            # print(f'current node {node}')
            visited.add(node)
            for vert in graph[node]:
                # print(f'verts {vert}')
                # print(f'visitied {visited}')
                if vert not  in visited:
                    if visit(vert):
                        return True
                   
            return False

        return visit(source)

