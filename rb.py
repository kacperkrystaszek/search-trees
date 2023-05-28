from rb.RB import RB
from utility.SearchTreeUtils import SearchTreeUtils as stu

rb = RB()
rb.insert(50)
rb.insert(30)
rb.insert(20)
rb.insert(40)
rb.insert(70)
rb.insert(60)
rb.insert(80)

print(stu.in_order(rb))

print(rb.search(40))
print(rb.search(90))
stu.visualize(rb)

print("-"*30)

rb.delete(30)
# print(stu.in_order(rb))
stu.visualize(rb)
