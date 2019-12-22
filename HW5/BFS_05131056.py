from collections import defaultdict

class Graph:
     def __init__(self):
          self.graph = defaultdict(list)

     def addEdge(self, u, v):
          self.graph[u].append(v)

     #檢查i是否存在於M與N
     def check(self, M, N, i):
          if i in M:
               return True
          if i in N:
               return True
          return False
     
     def BFS(self, s):
          M = [s]
          N = self.graph[s]
          while len(N) != 0:
               M.append(N[0])
               N = N[1:len(N)]
               for i in self.graph[M[-1]]:
                    if self.check(M, N, i) == False:
                         N.append(i)
          return M
     
     #先進先出
     def DFS(self, s):
          M = [s]
          N = []
          L = len(self.graph[s])
          for i in range(L):
               N.append(self.graph[s][L-1-i])
          while len(N) != 0:
               if self.check(M,[],N[-1]) == True:
                    N = N[0:-1]
               else:
                    M.append(N[-1])
                    N = N[0:-1]
                    L = len(self.graph[M[-1]])
                    for ii in range(L):
                         i = self.graph[M[-1]][L-1-ii]
                         if self.check(M, [], i) == False:
                              N.append(i)
          return M
          
     #後進先出
     def DFS2(self, s):
          M = [s]
          N = self.graph[s]
          while len(N) != 0:
               M.append(N[-1])
               N = N[0:-1]
               for i in self.graph[M[-1]]:
                    if self.check(M, N, i) == False:
                         N.append(i)
          return M
     
'''
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(1, 5)
g.addEdge(2, 4)
g.addEdge(2, 6)
g.addEdge(3, 5)
g.addEdge(4, 1)
g.addEdge(4, 5)
g.addEdge(5, 0)
g.addEdge(6, 4)

print(g.BFS(2))
#DFS可製成迷宮
print(g.DFS(2))
print(g.DFS2(2))
'''

#參考資料:自己
