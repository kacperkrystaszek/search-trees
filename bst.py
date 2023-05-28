from bst.BST import BST
from utility.SearchTreeUtils import SearchTreeUtils as stu

bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print(stu.in_order(bst))

print(bst.search(40))
print(bst.search(90))
stu.visualize(bst)

bst.delete(30)
print(stu.in_order(bst))
stu.visualize(bst)
