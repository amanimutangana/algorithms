from data_structures.binarytree import BinaryTree
def test_dfs_preorder():
    bt = BinaryTree()
    values = [5, 3, 8, 1, 4, 7, 9]
    for value in values:
        bt.insert(value)

    expected_preorder = [5, 3, 1, 4, 8, 7, 9]
    assert bt.dfs_preorder() == expected_preorder  # No need to pass the root node explicitly


def test_dfs_inorder():
    bt = BinaryTree()
    values = [5, 3, 8, 1, 4, 7, 9]
    for value in values:
        bt.insert(value)

    expected_inorder = [1, 3, 4, 5, 7, 8, 9]
    assert bt.dfs_inorder() == expected_inorder  # Same here


def test_dfs_postorder():
    bt = BinaryTree()
    values = [5, 3, 8, 1, 4, 7, 9]
    for value in values:
        bt.insert(value)

    expected_postorder = [1, 4, 3, 7, 9, 8, 5]
    assert bt.dfs_postorder() == expected_postorder  # No argument needed


def test_bfs():
    bt = BinaryTree()
    values = [5, 3, 8, 1, 4, 7, 9]
    for value in values:
        bt.insert(value)

    expected_bfs = [5, 3, 8, 1, 4, 7, 9]
    assert bt.bfs() == expected_bfs  # Ensure correct level-order traversal

