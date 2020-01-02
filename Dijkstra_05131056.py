class Graph():
     def __init__(self, vertices):
          self.V = vertices
          self.graph = []
          self.graph_matrix = [[0 for column in range(vertices)]
                               for row in range(vertices)]

     def addEdge(self, u, v, w):
          if self.graph == []:
               self.graph = [[0 for column in range(self.V)]
                             for row in range(self.V)]
          self.graph[u][v] = w
          self.graph[v][u] = w
          return True

     def Dijkstra(self, s):
          distance = {}
          for i in range(self.V):
               distance[str(i)] = self.graph[s][i]
          choises = [x for x in range(self.V)]
          choises[s] = None
          item = self.min_in_distance(distance, choises)
          choises[item[0]] = None
          for i in range(1, self.V-1):
               for j in choises:
                    if j != None:
                         if g.graph[item[0]][j] != 0:
                              d = distance[str(item[0])]+g.graph[item[0]][j]
                              if distance[str(j)] == 0:
                                   distance[str(j)] = d
                              else:
                                   if d < distance[str(j)]:
                                        distance[str(j)] = d
               item = self.min_in_distance(distance, choises)
               distance[str(item[0])] = item[1]
               choises[item[0]] = None
          return distance
     
     def min_in_distance(self, distance, choises):
          which = float('inf')
          for i in choises:
               if i != None and distance[str(i)] != 0:
                    if distance[str(i)] < which:
                         which = distance[str(i)]
                         ii = i
          return [ii, which]

     def Kruskal(self):
          k = {}
          choises = self.graph
          sub = [-1 for i in range(self.V)]
          while len(k) < self.V-1:
               item = self.min_in_graph(choises)
               choises[item[0]][item[1]] = 0
               if sub[item[0]] == -1 and sub[item[1]] == -1:
                    sub[item[0]] = item[0]
                    sub[item[1]] = item[0]
                    k[str(item[0])+'-'+str(item[1])] = item[2]
               elif sub[item[0]] != -1 and sub[item[1]] != -1:
                    if sub[item[0]] != sub[item[1]]:
                         for i in range(self.V):
                              if sub[i] == sub[item[1]]:
                                   sub[i] = sub[item[0]]
                         k[str(item[0])+'-'+str(item[1])] = item[2]
               else:
                    if sub[item[0]] == -1:
                         sub[item[0]] = sub[item[1]]
                    else:
                         sub[item[1]] = sub[item[0]]
                    k[str(item[0])+'-'+str(item[1])] = item[2]
          return k
          
     def min_in_graph(self, choises):
          which = float('inf')
          for j in range(1, self.V):
               for i in range(j):
                    if choises[i][j] != 0:
                         if choises[i][j] < which:
                              which = choises[i][j]
                              u = i
                              v = j
          return [u, v, which]
'''
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]
print(g.Dijkstra(0))

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
print(g.Kruskal())
'''
#參考資料(Dijkstra):自己
#參考資料(Kruskal):http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html
#之原理解說

