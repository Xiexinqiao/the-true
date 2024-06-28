# 加载CSV数据集并初始化AVL树和队列
import pandas as pd
from Property import Property
from Client import Client
from AVLTree import AVLTree
from Queue import Queue
# 读取数据集文件
properties_df = pd.read_csv(r'C:\Users\lenovo\Desktop\the true\realestate\toolbox\real_estate_properties_dataset.csv')
clients_df = pd.read_csv(r'C:\Users\lenovo\Desktop\the true\realestate\toolbox\client_requests_dataset.csv')

# 初始化AVL树和队列
property_tree = AVLTree()
root = None
client_queue = Queue()

# 从数据集中加载房产信息
for index, row in properties_df.iterrows():
    prop = Property(row['property_ID'], row['address'], row['price'], row['property_type'], row['status'], row['owner'])
    root = property_tree.insert(root, prop.property_id, prop)

# 从数据集中加载客户信息
for index, row in clients_df.iterrows():
    client = Client(row['client_ID'], row['name'], row['contact_info'], row['budget'],row['price'])
    client_queue.enqueue(client)

# 打印加载结果
print("AVL Tree Root:", root.value)
print("Client Queue:", client_queue)
