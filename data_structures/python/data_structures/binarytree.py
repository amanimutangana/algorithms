class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current_node, value):
        # Prevent duplicate values
        if value == current_node.value:
            return
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:  # value > current_node.value
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def dfs_preorder(self, node=None):
        result = []
        # Helper function for the recursive traversal
        def traverse(node):
            # Base case: if the node is None, return
            if node is None:
                return
            
            # Visit the current node and append the value to result
            result.append(node.value)
            
            # Recur on the left subtree
            traverse(node.left)
            
            # Recur on the right subtree
            traverse(node.right)
        
        # Start the traversal from the root
        traverse(self.root)
        return result

    def dfs_postorder(self, node=None):
        result = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
        traverse(self.root)
        return result

    def dfs_inorder(self):
        result = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
        traverse(self.root)
        return result

    def bfs(self):

        if self.root is None:
            return []
        
        queue = [self.root]
        traversal_result = []

        while queue:
            current_node = queue.pop(0)
            traversal_result.append(current_node.value)

            # Add left and right children to the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        return traversal_result
