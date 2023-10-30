from collections import deque
class Graph:
    def __init__(self,V) -> None:
        """making empty graph and the size of the graph"""
        self.adj={i:[] for i in range(V)}
        self.v=V
    def addEdge(self,u,v):
        """adding edge u<-->v with weight s"""
        self.adj[u].append(v)
        self.adj[v].append(u)
    def bfs(self,i,v,p):
        v[i]=True
        que=deque()
        que.append(i)
        while len(que)>0:
            u=que.popleft()
            for j in self.adj[u]:
                if not v[j]:
                    que.append(j)
                    v[j]=True
                    p[j]=u

    
    def sort(self,p,s,d):
        ans=[]
        while s!=d:
            ans.append(p[d])
            d=p[d]
        return ans
        
        

        
    
if __name__=='__main__':
    gf=Graph(9)
    gf.addEdge(0, 7)
    gf.addEdge(0, 1)
    gf.addEdge(1, 0)
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
    v=[False for i in range(gf.v)]
    p=[-1 for i in range(gf.v)]
    
    for i in range(gf.v):
        if not v[i]:
            gf.bfs(i,v,p)
    print(gf.sort(p,0,5))
    