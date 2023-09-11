class TreeNode():
    def __init__(self, value, left=None, right = None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # Traversal
    def pre_order_traversal(self, action, node): # Create copy of tree
        if node is not None:
            action(node)
            self.pre_order_traversal(action, node.left)
            self.pre_order_traversal(action, node.right)

    def in_order_traversal(self, action, node): # Print in Order values
        if node is not None:
            self.in_order_traversal(action, node.left)
            action(node)
            self.in_order_traversal(action, node.right)

    def post_order_traversal(self, action, node): # Delete all nodes
        if node is not None:
            self.post_order_traversal(action, node.left)
            self.post_order_traversal(action, node.right)
            action(node)
            

def get_node_value(node):
    print(node.value)
    return node.value

if __name__ == "__main__":
    # Build simple tree manually
    root = TreeNode(12)
    node14 = TreeNode(14)
    node7 = TreeNode(7)
    node9 = TreeNode(9)
    node18 = TreeNode(18)
    node3 = TreeNode(3)
    root.right = node14
    root.left = node7
    node7.right = node9
    node14.right = node18
    node7.left = node3
    binary_tree = BinaryTree(root)
    print("Pre order traversal")
    binary_tree.pre_order_traversal(get_node_value, binary_tree.root)
    print("----------")
    print("In order traversal")
    binary_tree.in_order_traversal(get_node_value, binary_tree.root)
    print("----------")
    print("Post order traversal")
    binary_tree.post_order_traversal(get_node_value, binary_tree.root)
    print("----------")
    # copy_binary_tree = BinaryTree()
    # binary_tree.pre_order_traversal()
    print()