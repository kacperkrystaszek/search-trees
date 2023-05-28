from avl.AVLNode import AVLNode as Node


class AVLTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def delete(self, data):
        self.root = self._delete(self.root, data)
    
    def search(self, data):
        return self._search(self.root, data)
        
    def _insert(self, node, data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
            
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)
        x = self._make_insert_balance(balance, data, node)
        if x:
            return x
        
        return node
        
    def _delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self._get_min_value(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
            
        if node is None:
            return node
            
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)
        x = self._make_delete_balance(balance, node)
        if x:
            return x
        
        return node
    
    def _search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)        
        
    def _get_min_value(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value(node.left)
    
    def _make_insert_balance(self, balance, data, node):
        if balance > 1 and data < node.left.data:
            return self._right_rotate(node)
        if balance < -1 and data > node.right.data:
            return self._left_rotate(node)
        if balance > 1 and data > node.left.data:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and data < node.right.data:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
    def _make_delete_balance(self, balance, node):
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
            
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y
    
    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y
    