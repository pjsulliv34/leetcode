class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected) #number of nodes
        print(n)
        visited = set()
        def dfs(i):
            print(f'running dfs {i}')
            visited.add(i)
            for j in range(n):
                print(f'current j {j}')
                if j not in visited and isConnected[i][j]==1:
                    print(f'met condition i {i}, j {j} ')
                    dfs(j)
        provinces= 0
        for i in range(n):
            print(f'i {i}')
            if i not in visited:
                dfs(i)
                provinces +=1

        return provinces