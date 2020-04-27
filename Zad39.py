class SimpleGraph(object):
   def __init__(self):
      self.vertex_nbh = {}

   def vertices(self):
      """ zwraca wierzcholki grafu"""
      return list(self.vertex_nbh.keys())

   def edges(self):
      """ zwraca krawedzie grafu"""
      edges = []
      for x in self.vertex_nbh:
         for y in self.vertex_nbh[x]:
            if{y, x} not in edges:
               edges.append({x, y})
      return edges

   def add_vertex(self, x):
      """ Jesli "vertex" nie jest w self.vertex_nbh to
         klucz "vertex" z pusta lista sasiadow jest dodany
         do slownika .
         W przeciwnym przypadku nic sie nie dzieje .
      """
      if x not in self.vertex_nbh:
         self.vertex_nbh[x] = []

   def _add_edge(self, x, y):
      if x in self.vertex_nbh:
         if y not in self.vertex_nbh[x]:
            self.vertex_nbh[x].append(y)
      else:
         self.vertex_nbh[x] = [y]
 
   def add_edge(self, x, y):
      self._add_edge(x, y)
      self._add_edge(y, x)
 
   def neighbors(self, v):
      return self.vertex_nbh[v]

   def generateTree(self, treeDict):
      top = list(treeDict.keys())[0]
      stack = [treeDict[top]]
      tree = {top: treeDict[top]}
      del treeDict[top]

      while len(stack):
         top = stack.pop(0)

         for child in top.keys():
            top[child] = treeDict[child]
            stack.append(treeDict[child])
            del treeDict[child]
         
         if not stack and treeDict:
            top = list(treeDict.keys())[0]
            stack.append(treeDict[top])
            tree[top] = treeDict[top]
            del treeDict[top]

      return tree

   def spanningTree(self):
      top = self.vertices()[0]
      queue = [top]
      visited = [top]
      tree = {}

      while len(queue):
         top = queue.pop(0)
         unvisitedNeighbors = list(filter(lambda neighbor: neighbor not in visited, self.neighbors(top)))

         queue += unvisitedNeighbors

         for neighbor in unvisitedNeighbors:
            visited.append(neighbor)

         neighborDict = {}
         for neighbor in unvisitedNeighbors:
            neighborDict[neighbor] = {}
         tree[top] = neighborDict

         # If there is unvisited node, go to this node
         if not queue and len(visited) != len(self.vertices()):
            subTree = list(filter(lambda v: v not in visited, self.vertices()))
            queue.append(subTree[0])
            visited.append(subTree[0])
      
      return self.generateTree(tree)

if __name__ == "__main__":
   graph = SimpleGraph()
   graph.add_edge("a", "b")
   graph.add_edge("a", "c")
   graph.add_edge("a", "d")
   graph.add_edge("b", "a")
   graph.add_edge("c", "a")
   graph.add_edge("c", "d")
   graph.add_edge("d", "a")
   graph.add_edge("d", "c")
   graph.add_edge("d", "e")
   graph.add_vertex("f")

   print("Vertices of graph:")
   print(graph.vertices())

   print("Edges of graph:")
   print(graph.edges())
   print(graph.spanningTree())