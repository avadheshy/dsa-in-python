from collections import deque
class Graph:
    def __init__(self,V) -> None:
        """making empty graph and the size of the graph"""
        self.el={i:[] for i in range(V)}
        self.v=V
    def addEdge(self,u,v):
        """adding edge u<-->v with weight s"""
        self.el[u].append(v)
        self.el[v].append(u)
    def bfs(self,i,v):
        v[i]=True
        que=deque()
        que.append(i)
        while len(que)>0:
            u=que.popleft()
            print(u,end=" ")
            for j in self.el[u]:
                if not visited[j]:
                    visited[j]=True
                    que.append(j)
        
        

        
    
if __name__=='__main__':
    gf=Graph(9)
    gf.addEdge(0, 7)
    gf.addEdge(0, 1)
    gf.addEdge(1, 2)
    gf.addEdge(1, 7)
    gf.addEdge(2, 3)
    gf.addEdge(2, 8)
    gf.addEdge(2, 5)
    gf.addEdge(3, 4)
    gf.addEdge(3, 5)
    gf.addEdge(4, 5)
    gf.addEdge(5, 6)
    gf.addEdge(6, 7)
    gf.addEdge(6, 8)
    gf.addEdge(7, 8)
    visited=[False for i in range(gf.v)]
    for i in range(gf.v):
        if not visited[i]:
            gf.bfs(i,visited)