from Property import Property
from PropertyType import PropertyType
from Client import Client
from AVLTree import AVLTree
from Queue import Queue
# 测试代码
property_tree = AVLTree()
root = None
properties = [
    Property(1, "123 Main St", 250000, PropertyType.HOUSE),
    Property(2, "456 Maple Ave", 300000, PropertyType.APARTMENT),
    Property(3, "789 Oak Dr", 150000, PropertyType.APARTMENT),
    Property(4,"101 Pine St",400000,PropertyType.HOUSE),
    Property(5,"202 Maple St",200000,PropertyType.COMMERCIAL),
    Property(6,"303 Cedar St",350000,PropertyType.HOUSE),
    Property(7,"404 Birch St",450000,PropertyType.HOUSE),
    Property(8,"505 Walnut St",180000,PropertyType.LAND),
    Property(9,"606 Chestnut St",230000,PropertyType.LAND),
    Property(10,"707 Spruce St",310000,PropertyType.COMMERCIAL),
]

for prop in properties:
    root = property_tree.insert(root, prop.property_id, prop)

# 打印AVL树根节点
print(root.value)

# 测试队列
client_queue = Queue()
clients = [
    Client(1, "Alice Johnson", "alice@example.com","HOUSE", 350000),
    Client(2, "Bob Miller", "bob@example.com", "APARTMENT",250000),
    Client(3, "Charlie Davis", "charlie@example.com", "COMMERCIAL",400000),
    Client(4, "Diana Wilson", "diana@example.com", "LAND",200000),
    Client(5, "Edward Taylor", "edward@example.com", "HOUSE",300000),
]

for client in clients:
    client_queue.enqueue(client)

# 打印队列
print(client_queue)