class Graph:
    def __init__(self,V) -> None:
        """making empty graph and the size of the graph"""
        self.adj={i:[] for i in range(V)}
        self.v=V
    def addEdge(self,u,v):
        """adding edge u<-->v with weight s"""
        self.adj[u].append(v)
        # self.el[v].append(u)
    def bfs(self,i,v,dv,p):
        v[i]=True
        dv[i]=True
        for j in self.adj[i]:
            if not v[j]:
                if self.bfs(j,v,dv,p):
                    return True
            elif dv[j] and j!=p:
                return True
            
        dv[i]=False
        return False
        
        

        
    
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
    dv=[False for i in range(gf.v)]
    
    for i in range(gf.v):
        if not v[i]:
            if gf.bfs(i,v,dv,-1):
                print('cycle present')
                exit()
    print('no cycle')