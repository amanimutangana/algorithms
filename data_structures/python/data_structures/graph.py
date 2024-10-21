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
        visited = set()
        queue = [start_vertex]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([v for v in self.graph[vertex] if v not in visited])
        
        return result
    
    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        result = [start_vertex]
        
        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                result += self.dfs(neighbor, visited)
        
        return result
