#link:  https://www.youtube.com/watch?v=V8qIqJxCioo
# logic steps: 1) sort all nodes in order of largest finishing time using Topo Sort logic, time: O(n + E)
# 2) Transpose the graph so that the path got disconnected to reach any other components, time: O(n + E)
# 3) Call DFS acc to the largest finishing time got in step 1 on the transposed graph, time: O(n +E)
# Space : O(n)


from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V= n
        self.visited= [False]*n
        self.visited_reverse= [False]*n
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)

    def DFS(self, adj,src, stack):
        self.visited[src]= True
        for u in adj[src]:
            if not self.visited[u]:
                self.DFS(adj, u, stack)  
        
        stack.append(src) # will contain node with largest finishing time at the top

    def PrintScc(self, transpose1, src):
        self.visited_reverse[src]= True
        print(src, end=" ")
        for v in transpose1[src]:
            if not self.visited_reverse[v]:
                self.PrintScc(transpose1, v)

    def KosaRaju(self, adj, n):
        stack= []
        for i in range(n):
            if self.visited[i]== False:
                self.DFS(adj,i, stack)
        # print(stack)
        
        # now transpose the graph
        transpose= defaultdict(list)
        for i  in range(n):
            for j in adj[i]:
                transpose[j].append(i)
        # print(transpose)
        
        # now call the DFS according to the largest finishing time on the transposed graph
        # top of the stack will store the  ele with largest finishing time
        # for this first make visited of all node as False (did using visited_reverse array)

        print("the strongly connected components are: ")
        while stack:
            u= stack.pop()
            if self.visited_reverse[u]== False:
                print()
                self.PrintScc(transpose, u)

g= Graph(5)
g.addEdge(1,0)
g.addEdge(2,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(3,4)
g.KosaRaju(g.AdjList, 5)