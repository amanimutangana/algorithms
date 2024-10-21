from data_structures.graph import Graph

def test_graph_add_vertex():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    
    assert 1 in g.graph
    assert 2 in g.graph

def test_graph_add_edge():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_edge(1, 2)
    
    assert 2 in g.graph[1]
    assert 1 in g.graph[2]

def test_graph_get_neighbors():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_edge(1, 2)
    
    assert g.get_neighbors(1) == [2]
    assert g.get_neighbors(2) == [1]

def test_graph_has_edge():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_edge(1, 2)
    
    assert g.has_edge(1, 2) is True
    assert g.has_edge(2, 1) is True
    assert g.has_edge(1, 3) is False

def test_graph_bfs():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    
    assert g.bfs(1) == [1, 2, 3]

def test_graph_dfs():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    
    assert g.dfs(1) == [1, 2, 3]
