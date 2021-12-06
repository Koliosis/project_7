import math

class Graph:
    def __init__(self):
        self.verts = []
        self.edge = [[ math.inf for i in range(len(self.verts)) ] for j in range(len(self.verts)) ]
        
        
    def add_vertex(self, label):
        self.verts.append(label)
        self.edge.append([math.inf for i in range(len(self.verts))])
        for i in self.edge:
            i.append(math.inf)
        
        
    
    def add_edge(self, src, dest, w):
        source = self.verts.index(src)
        destination = self.verts.index(dest)
        self.edge[source][destination] = w
        
        
    def get_weight(self, src, dest):
        return self.edge[src][dest]
    
    
    def dfs(self, starting_vertex):
        pass
    
    
    def bfs(self, starting_vertex):
        pass
    
    
    def dsp(self, src, dest):
        pass
    
    
    def dsp_all(self, src):
        pass
        
        
    def __str__(self):
        output = ''
        for i in self.edge:
            src = self.edge.index(i)
            for j in i:
                dest = i.index(j)
                if j != math.inf:
                    output += f"{self.verts[src]} -> {self.verts[dest]} [weight='{j}]'\n"
        return output
                    
        
        
        

def main():
    new_graph = Graph()
    new_graph.add_vertex("A")
    new_graph.add_vertex("B")
    new_graph.add_vertex("C")
    new_graph.add_vertex("D")
    new_graph.add_edge("A", "D", 5)
    new_graph.add_edge("B", "C", 3)
    print(new_graph)
    
    
main()