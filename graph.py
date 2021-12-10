"""
Project 7
Kole Davis
"""

import math

class Graph:
    """
    Creates a graph ADT
    """
    def __init__(self):
        """Intitializes the class
        """
        self.verts = []
        self.edge = [[ math.inf for i in range(len(self.verts)) ] for j in range(len(self.verts)) ]


    def add_vertex(self, label):
        """Adds a vertex to the graph

        :param label: Name of the vertex
        :type label: str
        """
        self.verts.append(label)
        self.edge.append([math.inf for i in range(len(self.verts))])
        for i in self.edge:
            i.append(math.inf)



    def add_edge(self, src, dest, w):
        """Adds an edge between two verteces

        :param src: The source vertex
        :type src: str
        :param dest: the destination vertex
        :type dest: str
        :param w: The weight of the edge
        :type w: int
        :raises ValueError: argument is invalid
        :raises ValueError: argument is invalid
        :raises ValueError: argument is invalid
        """
        # possibles = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if type(src) is not str:
            raise ValueError
        if type(dest) is not str:
            raise ValueError
        if type(w) is not float:
            raise ValueError
        source = self.verts.index(src)
        destination = self.verts.index(dest)
        self.edge[source][destination] = w


    def get_weight(self, src, dest):
        """gets the weight of an edge

        :param src: source vertex
        :type src: str
        :param dest: destination vertex
        :type dest: str
        :return: returns the weight of the edge
        :rtype: int
        """
        return self.edge[src][dest]


    def bfs(self, starting_vertex):
        """Does bfs

        :param starting_vertex: the starting vertex
        :type starting_vertex: str
        """
        def bfs_helper(cursor, visited):
            neighbors = self.get_neighbor(cursor)
            for i in neighbors:
                i = self.verts[i]
                if i not in visited:
                    if i not in queue:
                        queue.append(i)
            while queue != []:
                to_visit = queue.pop(0)
                visited.append(to_visit)
                bfs_helper(to_visit, visited)
            return visited
        visited = [starting_vertex]
        queue = []
        cursor = starting_vertex
        bfs_helper(cursor, visited)
        for i in visited:
            yield i


    # def dfs(self, starting_vertex):
    #     """
    #     :param starting_vertex: the starting vertex
    #     :return: returns the dfs path
    #     """
    #     stack = []
    #     cursor = starting_vertex
    #     stack.append(starting_vertex)
    #     visited = []
    #     path = []
    #     while stack != []:
    #         cursor = stack[-1]
    #         stack.pop(-1)
    #         path.append(cursor)
    #         visited.append(cursor)
    #         children = self.get_neighbor(cursor)
    #         for child in children:
    #             children[child] = self.verts[children(child)]
    #         for i in children:
    #             if i not in visited:
    #                 stack.append(i)
    #     return path


# def dfs_helper(self, v, visited):
#     """helps the dfs method

#     :param v: [description]
#     :type v: [type]
#     :param visited: [description]
#     :type visited: [type]
#     """
#     visited.add(v)
#     print(v, end=' ')
#     for neighbour in self.graph_lyst[v]:
#         if neighbour not in visited:
#             self.dfs_helper(neighbour, visited)


    def get_neighbor(self, starting_vertex):
        """
        :param starting_vertex: starting vertex
        :return: returns neighbors to the vertex
        """
        output_list = []
        index = self.verts.index(starting_vertex)
        print(self.edge[index])
        counter = 0
        while counter < len(self.edge[index]):
            # print(self.edge[index][counter])
            if self.edge[index][counter] is not math.inf:
                # print(i, self.edge[index].index(i))
                output_list.append(counter)
            counter += 1
        return output_list


    # def dfs(self, starting_vertex):
    #     """
    #     :param starting_vertex:
    #     :return:
    #     """
    #     queue = []
    #     stack = []
    #     cursor = starting_vertex
    #     queue.append(starting_vertex)
    #     visited = []
    #     path = []
    #     while queue != []:
    #         cursor = queue[0]
    #         cursor = stack.pop(0)
    #         path.append(cursor)
    #         visited.append(cursor)
    #         if cursor == dest:
    #             queue.append(dest)
    #             return path
    #         else:
    #             children = self.get_neighbor(cursor)
    #             for child in children:
    #                 children[child] = self.label_lyst[cursor][child]
    #             for i in children:
    #                 if i not in visited and i not in children:
    #                     queue.append(i)


    def dsp(self, src, dest):
        """Dijkstras shortest paht

        :param src: source vertex
        :type src: str
        :param dest: destination vertex
        :type dest: str
        """
        pass


    def dsp_all(self, src):
        """[summary]

        :param src: [description]
        :type src: [type]
        """
        pass


    def __str__(self):
        output = ''
        for i in self.edge:
            src = self.edge.index(i)
            for j in i:
                dest = i.index(j)
                if j != math.inf:
                    output += f"{self.verts[src]} -> {self.verts[dest]} [label='{j}', weight='{j}]'\n"
        return output





def main():
    """main function of program
    """
    new_graph = Graph()
    # new_graph.add_vertex("A")
    # new_graph.add_vertex("B")
    # new_graph.add_vertex("C")
    # new_graph.add_vertex("D")
    # new_graph.add_vertex("E")
    # new_graph.add_vertex("F")
    # new_graph.add_vertex("G")
    # new_graph.add_edge("A", "B", 2.0)
    # new_graph.add_edge("A", "F", 9.0)
    # new_graph.add_edge("B", "C", 8.0)
    # new_graph.add_edge("B", "D", 15.0)
    # new_graph.add_edge("B", "F", 6.0)
    # new_graph.add_edge("C", "D", 1.0)
    # new_graph.add_edge("E", "C", 7.0)
    # new_graph.add_edge("E", "D", 3.0)
    # new_graph.add_edge("F", "B", 6.0)
    # new_graph.add_edge("F", "E", 3.0)
    new_graph.add_vertex("A")
    new_graph.add_vertex("B")
    new_graph.add_vertex("C")
    new_graph.add_vertex("D")
    new_graph.add_vertex("E")
    new_graph.add_vertex("F")
    new_graph.add_edge("A", "B", 1.0)
    new_graph.add_edge("A", "C", 1.0)
    new_graph.add_edge("B", "D", 1.0)
    new_graph.add_edge("C", "E", 1.0)
    new_graph.add_edge("E", "F", 1.0)
    print(new_graph)
    for vertex in new_graph.bfs("A"):
        print(vertex, end=", ")
    print("\n")
    # print(new_graph.get_neighbor("A"))


main()
