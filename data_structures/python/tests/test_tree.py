from data_structures.tree import BinaryTree

def test_tree_insert():
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(8)
    
    assert bt.root.value == 5
    assert bt.root.left.value == 3
    assert bt.root.right.value == 8

def test_tree_search():
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(8)
    
    assert bt.search(5) is True
    assert bt.search(3) is True
    assert bt.search(8) is True
    assert bt.search(10) is False
