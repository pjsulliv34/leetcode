class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()

        def visit(room):
            # base case to return,
            if room in visited:
                return
            visited.add(room) #adding each vertice
            for room in rooms[room]: #loop through each key in room:
                visit(room)

        visit(0)
        if len(visited) == len(rooms):
            return True
        else:
            return False

