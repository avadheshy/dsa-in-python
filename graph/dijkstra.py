import heapq as hq
import sys
mx=sys.maxsize
class Graph:
    def __init__(self,V) -> None:
        """making empty graph and the size of the graph"""
        self.el={i:[] for i in range(V)}
        self.v=V
    def addEdge(self,u,v,s):
        """adding edge u<-->v with weight s"""
        self.el[u].append((v,s))
        self.el[v].append((u,s))
    def dijkstra(self,s):
        li=[]
        hq.heapify(li)
        hq.heappush(li,(0,s))
        # making heap and inserting the source in the heap
        arr=[mx for i in range(self.v)]
        arr[s]=0
        # making distance of all the nodes to infinite
        while len(li)>0:
            w,n=hq.heappop(li)
            for i in self.el[n]:
                # checkig if old distance is greater than source+w the 
                # update the distance and push that node in 
                # the heap with his weight
                if arr[i[0]]>w+i[1]:
                    hq.heappush(li,(w+i[1],i[0]))
                    arr[i[0]]=w+i[1]
        return arr
        #returning the ans array 
        

        
    
if __name__=='__main__':
    gf=Graph(9)
    gf.addEdge(0, 7, 8)
    gf.addEdge(0, 1, 4)
    gf.addEdge(1, 2, 8)
    gf.addEdge(1, 7, 11)
    gf.addEdge(2, 3, 7)
    gf.addEdge(2, 8, 2)
    gf.addEdge(2, 5, 4)
    gf.addEdge(3, 4, 9)
    gf.addEdge(3, 5, 14)
    gf.addEdge(4, 5, 10)
    gf.addEdge(5, 6, 2)
    gf.addEdge(6, 7, 1)
    gf.addEdge(6, 8, 6)
    gf.addEdge(7, 8, 7)
    print(gf.dijkstra(0))