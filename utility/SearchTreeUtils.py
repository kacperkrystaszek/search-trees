class SearchTreeUtils:
    @classmethod        
    def in_order(cls, search_tree):
        elements = []
        cls._in_order(search_tree.root, elements)
        return elements
    
    @classmethod
    def _in_order(cls, node, elements):
        if node is not None:
            cls._in_order(node.left, elements)
            elements.append(node.data)
            cls._in_order(node.right, elements)
    
    @classmethod        
    def visualize(cls, search_tree):
        tree_dict = cls._build_tree_dict(search_tree.root)
        cls._print_tree_dict(tree_dict)

    @classmethod
    def _build_tree_dict(cls, node):
        if node is None:
            return {}
        if hasattr(node, "color"):
            tree_dict = {
                "data": node.data,
                "color": node.color,
                "left": cls._build_tree_dict(node.left),
                "right": cls._build_tree_dict(node.right)
            }
        else:
            tree_dict = {
                "data": node.data,
                "left": cls._build_tree_dict(node.left),
                "right": cls._build_tree_dict(node.right)
            }
        return tree_dict
    
    @classmethod
    def _print_tree_dict(cls, node, level=0):
        if node:
            cls._print_tree_dict(node["left"], level+1)
            if node.get("color"):
                print(' ' * 4 * level + str(node["data"]) + str(node['color']))
            else:
                print(' ' * 4 * level + str(node["data"]))            
            cls._print_tree_dict(node["right"], level+1)
        else:
            print(' ' * 4 * level + "--")
