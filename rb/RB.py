from rb.RBNode import RBNode as Node


class RB:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        self._insert_help(node)
        self._fix_insert(node)

    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, data):
        node = self.search(data)
        if node is not None:
            self._delete(node)

    def _insert_help(self, node):
        if self.root is None:
            self.root = node
        else:
            current = self.root
            parent = None
            while current is not None:
                parent = current
                if node.data < current.data:
                    current = current.left
                else:
                    current = current.right

            node.parent = parent
            if node.data < parent.data:
                parent.left = node
            else:
                parent.right = node

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == Node.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == Node.RED:
                    node.parent.color = Node.BLACK
                    uncle.color = Node.BLACK
                    node.parent.parent.color = Node.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = Node.BLACK
                    node.parent.parent.color = Node.RED
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == Node.RED:
                    node.parent.color = Node.BLACK
                    uncle.color = Node.BLACK
                    node.parent.parent.color = Node.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = Node.BLACK
                    node.parent.parent.color = Node.RED
                    self._left_rotate(node.parent.parent)

        self.root.color = Node.BLACK

    def _fix_delete(self, node, parent):
        while node != self.root and (node is None or node.color == Node.BLACK):
            if node == parent.left:
                node = self._fix_left_child(node, parent)
            else:
                node = self._fix_right_child(node, parent)
        if node is not None:
            node.color = Node.BLACK

    def _fix_left_child(self, node, parent):
        sibling = parent.right
        if sibling.color == Node.RED and sibling is not None:
            sibling.color = Node.BLACK
            parent.color = Node.RED
            self._left_rotate(parent)
            sibling = parent.right

        if (sibling is None or sibling.left is None or sibling.left.color == Node.BLACK) and (
            sibling is None or sibling.right is None or sibling.right.color == Node.BLACK
        ):
            sibling.color = Node.RED
            node = parent
            parent = node.parent
        else:
            if sibling is not None and (sibling.right.color == Node.BLACK or sibling.right is None):
                if sibling.left is not None:
                    sibling.left.color = Node.BLACK
                sibling.color = Node.RED
                self._right_rotate(sibling)
                sibling = parent.right
            if sibling is not None:
                sibling.color = parent.color
            parent.color = Node.BLACK
            if sibling is not None and sibling.right is not None:
                sibling.right.color = Node.BLACK
            self._left_rotate(parent)
            node = self.root
        return node

    def _fix_right_child(self, node, parent):
        sibling = parent.left
        if sibling.color == Node.RED and sibling is not None:
            sibling.color = Node.BLACK
            parent.color = Node.RED
            self._right_rotate(parent)
            sibling = parent.left

        if (sibling is None or sibling.right is None or sibling.right.color == Node.BLACK) and (
            sibling is None or sibling.left is None or sibling.left.color == Node.BLACK
        ):
            sibling.color = Node.RED
            node = parent
            parent = node.parent
        else:
            if (sibling.left.color == Node.BLACK or sibling.left is None) and sibling is not None:
                if sibling.right is not None:
                    sibling.right.color = Node.BLACK
                sibling.color = Node.RED
                self._left_rotate(sibling)
                sibling = parent.left
            if sibling is not None:
                sibling.color = parent.color
            parent.color = Node.BLACK
            if sibling is not None and sibling.left is not None:
                sibling.left.color = Node.BLACK
            self._right_rotate(parent)
            node = self.root
        return node

    def _left_rotate(self, node):
        right = node.right
        node.right = right.left
        if right.left is not None:
            right.left.parent = node
        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    def _right_rotate(self, node):
        left = node.left
        node.left = left.right
        if left.right is not None:
            left.right.parent = node
        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left

    def _successor(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete(self, node):
        if node.left is None or node.right is None:
            deleted = node
        else:
            deleted = self._successor(node)

        if deleted.left is not None:
            child = deleted.left
        else:
            child = deleted.right

        if child is not None:
            child.parent = deleted.parent

        if deleted.parent is None:
            self.root = child
        elif deleted == deleted.parent.left:
            deleted.parent.left = child
        else:
            deleted.parent.right = child

        if deleted != node:
            node.data = deleted.data

        if deleted.color == Node.BLACK:
            self._fix_delete(child, deleted.parent)
