class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #maybe not valid tree if a cycly?

        # dict_ = {}
        # #create graph hash
        

        #     #initalize empty list
        #     dict_[a] = dict_.get(a,[])
        #     dict_[b] = dict_.get(b,[])

        dict_ = {i:[] for i in range(n)}
        for a,b in edges:
            #append to each key
            dict_[a].append(b)
            dict_[b].append(a)

        print(dict_)

        visited = set()
        #if number of nodes visited = number of nodes, connected
        



        visited = set() #so if it goes back to any in visited, then return false:?

        def visit(node, prev):

            if node in visited:
                return False
            visited.add(node)
            for key in dict_[node]:
                if key == prev:
                    continue # dont visit the previous node again
                if not visit(key,node):
                    return False
            return True

        
        return visit(0,-1) and n == len(visited)

