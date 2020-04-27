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

   def smallDelta(self):
      """ Computes δ(G) of graph """
      return min([len(self.neighbors(v)) for v in self.vertices()])

   def d(self):
      """ Computes d¯(G) of graph """
      return sum([len(self.neighbors(v)) for v in self.vertices()]) / len(self.vertices())

   def bigDelta(self):
      """ Computes Δ(G) of graph """
      return max([len(self.neighbors(v)) for v in self.vertices()])

   def ecc(self, v):
      """ Computes excentity of vertex """
      L = 0
      visited = [v]
      active  = self.neighbors(v)
      while active != []:
         L += 1
         visited += active
         active = [y for x in active for y in self.neighbors(x) if y not in visited] 
      return L

   def radius(self):
      """ Computes radius of graph """
      return min([self.ecc(v) for v in self.vertices()])

   def diameter(self):
      """ Computes diameter of graph """
      return max([self.ecc(v) for v in self.vertices()])

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
   #graph.add_vertex("f")

   print("Vertices of graph:")
   print(graph.vertices())

   print("Edges of graph:")
   print(graph.edges())
   print(graph.smallDelta())
   print(graph.d())
   print(graph.bigDelta())
   
   print('ecc')
   for v in graph.vertices():
      print(graph.ecc(v))

   print("Radius")
   print(graph.radius())
   print(graph.diameter())