from binary_search_tree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)

    tree.inorder(tree.root)
    print("\n")
    tree.preorder(tree.root)
    print("\n")
    tree.postorder(tree.root)
    print("\n")
    tree.inorder_iterative()

