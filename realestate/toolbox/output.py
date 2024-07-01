import csv
from AVLTree import AVLTree
from Queue import Queue
from Client import Client
from Property import Property
# 初始化AVL树和队列
property_tree = AVLTree()
client_queue = Queue()
root = None # 初始化根节点为None

# 从CSV文件加载房产信息
filename = 'THETRUE\data\real_estate_properties_dataset.csv'
with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # 跳过标题行
        for row in csv_reader:
            prop = Property(*row) # 假设Property构造函数接受多个参数
            root = property_tree.insert(root, prop.property_id, prop) # 假设insert方法可以将Property实例添加到树中

# 从CSV文件加载客户信息
filename = 'data\client_requests_dataset.csv'
with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # 跳过标题行
    for row in csv_reader:
         client = Client(*row) # 假设Client构造函数接受多个参数
         client_queue.enqueue(client) # 假设enqueue方法可以将Client实例添加到队列中

# 打印加载结果
print("AVL Tree Root:", root.value) # 假设AVL树的节点有一个value属性
print("Client Queue:", client_queue)
