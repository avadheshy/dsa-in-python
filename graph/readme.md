# There are some concept in graph
   1. Adjecency matrix and list
   2. Depth first search
   3. Breath first search
   4. Cycle dedection in a directed graph
   5. Cycle dedection in undirected graph 
- visit all the neighbours
  ```
if v[nei]:
         visit[nei]
```
   1. Topological sorting using dfs
   2. Topological sort using kahn's algorithm
   3. Shortest path in undirected graph
   4. Shortest path directed graph
   5.  Shorted path in directed weighted grah
   6.  Single source shortest path(Dijkshtra algorithm) in weighted graph
   7.  MST using prim's algorithm 
   8.  MST using Kruskal algorith
   9.  Bridge in graph
  
  -  an array for discovery time
  -  an array for lowest visited time
  -  update d and l for the node
  -  visit all its neighbour if it is parant then continue if it is not visited then visit this and update l for the node with min(l[node],l[chile]) else if l[child]>d[node] then there is a bridge return the ans
   1.  Articular point in a graph
   2.  Kosaraju's strongly connected component algorithm
   3.  Bellmenford algorithm
