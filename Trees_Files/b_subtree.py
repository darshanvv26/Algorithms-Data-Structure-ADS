class SizeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1  

class SizeBST:
    def __init__(self):
        self.root = None

    def _get_size(self, node):
        return node.size if node else 0

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return SizeNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            node.size = 1 + self._get_size(node.left) + self._get_size(node.right)
            return node

        self.root = _insert(self.root, key)

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

    def inorder(self):
        def _inorder(node):
            if node:
                yield from _inorder(node.left)
                yield (node.key, node.size)
                yield from _inorder(node.right)
        return list(_inorder(self.root))

    def _min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, key):
        def _delete(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = self._min_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            node.size = 1 + self._get_size(node.left) + self._get_size(node.right)
            return node

        self.root = _delete(self.root, key)

    def get_total_size(self):
        return self._get_size(self.root)

    def get_subtree_size(self, key):
        def _find(node, key):
            if not node:
                return 0
            if key == node.key:
                return node.size
            elif key < node.key:
                return _find(node.left, key)
            else:
                return _find(node.right, key)
        return _find(self.root, key)

if __name__ == "__main__":
    sbst = SizeBST()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        sbst.insert(val)
    print("Total nodes in tree:", sbst.get_total_size())  
    print("Subtree size rooted at 30:", sbst.get_subtree_size(30))  
    print("Subtree size rooted at 70:", sbst.get_subtree_size(70))  
    sbst.delete(30)
    print("Total nodes after deleting 30:", sbst.get_total_size()) 
    print("Subtree size rooted at 50:", sbst.get_subtree_size(50))  
