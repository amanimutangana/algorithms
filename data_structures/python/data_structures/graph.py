class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
    def get_neighbors(self, vertex):
        return self.graph[vertex] if vertex in self.graph else []

    def has_edge(self, vertex1, vertex2):
        return vertex1 in self.graph and vertex2 in self.graph[vertex1]
    
    def bfs(self, start_vertex):
        # Initialize the visited set, queue, and result list
        visited = set()
        queue = [start_vertex]
        result = []
        
        # Process the queue until it's empty
        while queue:
            # Remove the first vertex from the queue
            vertex = queue.pop(0)
            
            # If the vertex hasn't been visited yet
            if vertex not in visited:
                # Mark the vertex as visited
                visited.add(vertex)
                
                # Add the vertex to the result list
                result.append(vertex)
                
                # Get the neighbors of the current vertex
                neighbors = self.graph[vertex]
                
                # Add unvisited neighbors to the queue
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        # Return the list of visited vertices in BFS order
        return result

    
    def dfs(self, start_vertex, visited=None):
        # Initialize the visited set if it's not provided
        if visited is None:
            visited = set()
        
        # Mark the current vertex as visited
        visited.add(start_vertex)
        
        # Start the result list with the current vertex
        result = [start_vertex]
        
        # Explore each neighbor of the current vertex
        neighbors = self.graph[start_vertex]
        for neighbor in neighbors:
            # If the neighbor hasn't been visited yet, perform DFS on it
            if neighbor not in visited:
                result += self.dfs(neighbor, visited)
        
        # Return the result list containing the visited vertices in DFS order
        return result

