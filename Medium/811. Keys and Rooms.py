from Queue import Queue
class Solution(object):
    def canVisitAllRooms(self, rooms):
        Visited = [False]*len(rooms)
        Visited[0] = True
        q = Queue()
        for i in range(len(rooms[0])):
            q.put(rooms[0][i])
        while not q.empty():
            x = q.get()
            for i in range(len(rooms[x])):
                if Visited[rooms[x][i]]==False:
                    q.put(rooms[x][i])
            Visited[x] = True
        for a in Visited:
            if a == False: return a
        return a
        