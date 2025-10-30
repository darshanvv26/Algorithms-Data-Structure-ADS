from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # a. Check BST is empty
    def is_empty(self):
        return self.root is None

    # b. Get count of nodes in BST
    def count_nodes(self):
        def count(node):
            if not node:
                return 0
            return 1 + count(node.left) + count(node.right)
        return count(self.root)

    # c. Add node to BST
    def insert(self, key):
        def _insert(node, key):
            if not node:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    # d. Search node in BST
    def search(self, key):
        def _search(node, key):
            if not node:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        return _search(self.root, key)

    # e. Tree Traversals
    def inorder(self):
        def _inorder(node):
            if node:
                yield from _inorder(node.left)
                yield node.key
                yield from _inorder(node.right)
        return list(_inorder(self.root))

    def preorder(self):
        def _preorder(node):
            if node:
                yield node.key
                yield from _preorder(node.left)
                yield from _preorder(node.right)
        return list(_preorder(self.root))

    def postorder(self):
        def _postorder(node):
            if node:
                yield from _postorder(node.left)
                yield from _postorder(node.right)
                yield node.key
        return list(_postorder(self.root))

    def level_order(self):
        if not self.root:
            return []
        queue = deque([self.root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    # f. Delete specified node
    def delete(self, key):
        def _delete(node, key):
            if not node:
                return node
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            return node
        self.root = _delete(self.root, key)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # g. Find height of BST
    def height(self):
        def _height(node):
            if not node:
                return -1
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    # h. Count number of terminal (leaf) nodes
    def count_leaves(self):
        def _count_leaves(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return _count_leaves(node.left) + _count_leaves(node.right)
        return _count_leaves(self.root)


if __name__ == "__main__":
    bst = BST()
    print("BST empty?", bst.is_empty())  
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    print("BST empty?", bst.is_empty())  
    print("Count nodes:", bst.count_nodes())  
    print("Search 40:", bst.search(40))  
    print("Search 100:", bst.search(100))
    print("In-order traversal:", bst.inorder())  
    print("Pre-order traversal:", bst.preorder())
    print("Post-order traversal:", bst.postorder())
    print("Level-order traversal:", bst.level_order())
    bst.delete(30)
    print("After deleting 30, In-order:", bst.inorder())
    print("Height of BST:", bst.height())
    print("Number of leaves:", bst.count_leaves())
