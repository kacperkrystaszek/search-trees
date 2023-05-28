from avl.AVL import AVLTree as AVL
from utility.SearchTreeUtils import SearchTreeUtils as stu

avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(25)
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(25)

# print(stu.in_order(avl))

print(avl.search(40))
print(avl.search(90))
stu.visualize(avl)

print("-"*30)

avl.delete(50)
# print(stu.in_order(avl))
stu.visualize(avl)
