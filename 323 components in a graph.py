class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = graph.get(i,[])
        print(graph)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
        for node in graph:
            if node not in visited:
                dfs(node)
                components+=1
        return components

