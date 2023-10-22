from collections import deque
class Graph:
    def __init__(self,V) -> None:
        """making empty graph and the size of the graph"""
        self.el={i:[] for i in range(V)}
        self.v=V
        self.arr=[0 for i in range(V)]
    def addEdge(self,u,v):
        """adding edge u<-->v with weight s"""
        self.el[u].append(v)
        self.arr[v]+=1
    def topological_sort(self,i,v,s):
        v[i]=True
        for j in self.el[i]:
            if not v[j]:
                self.topological_sort(j,v,s)
        s.appendleft(i)
    def kahn_algo(self):
        que=deque()
        ans=[]
        for i in range(self.v):
            if self.arr[i]==0:
                que.append(i)
        while len(que)>0:
            u=que.popleft()
            ans.append(u)
            for i in self.el[u]:
                self.arr[i]-=1
                if self.arr[i]==0:
                    que.append(i)
        return ans
                
        

        
    
if __name__=='__main__':
    gf=Graph(6)
    gf.addEdge(5, 2)
    gf.addEdge(5, 0)
    gf.addEdge(4, 0)
    gf.addEdge(4, 1)
    gf.addEdge(2, 3)
    gf.addEdge(3, 1)
    visited=[False for i in range(gf.v)]
    st=deque()
    for i in range(gf.v):
        if not visited[i]:
            gf.topological_sort(i,visited,st)
    print(st)
    print(gf.kahn_algo())