#Building Graph from scratch as part of boot.dev course work

class Graph:

    def __init__(self, num_vertices):
        self.graph = []

        for i in range(num_vertices):
            self.graph.append([])
            for j in range(num_vertices):
                self.graph[i].append(False)

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
    
    #Function to build graph using adjacency list and not matrix
    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])
    
    #helper function to retrive all the adjacent nodes
    def adjacent_nodes(self, node):

        return self.graph[node]
    
    #Fucntion to find unconnected_vertices
    def unconnected_vertices(self):

        keys = self.graph.keys()
        no_connections = []
        
        for key in keys:
            if self.graph[key] == set():
                no_connections.append(key)

        return no_connections
    
    #BFS Algorithm
    def breadth_first_search(self, v):

        v_visited = []
        v_queue = []

        v_queue.append(v)

        while v_queue != []:

            popped_v = v_queue.pop(0)
            v_visited.append(popped_v)

            sorted_neighbors = sorted(self.graph[popped_v])

            for neighbor in sorted_neighbors:

                if neighbor not in v_visited and neighbor not in v_queue:

                    v_queue.append(neighbor)

        return v_visited