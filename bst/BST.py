from bst.BSTNode import BSTNode as Node

class BST:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
            
    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
                
    def search(self, data):
        return self._search(data, self.root)
    
    def _search(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search(data, node.left)
        return self._search(data, node.right)
    
    def delete(self, data):
        self.root = self._delete(self.root, data)
        
    def _delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self.find_min_node(node.right)
            node.data = min_node.data
            node.right = self._delete(node.right, min_node.data)
        return node
    
    def find_min_node(self, node=None):
        if node is None:
            current = self.root
        else:
            current = node
        while current.left:
            current = current.left
        return current
    
    def find_max_node(self, node=None):
        if node is None:
            current = self.root
        else:
            current = node
        while current.right:
            current = current.right
        return current
    
