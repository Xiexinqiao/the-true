import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  # 将父级目录加入执行目录列表


import pandas as pd
from part1.toolbox.property import Property
from part1.toolbox.client import Client
from part1.toolbox.queue import Queue
from toolbox.dynamic_pricing import DynamicPricingModel
from toolbox.property_matcher import PropertyMatcher

# 读取数据集文件
properties_df = pd.read_csv('data/real_estate_properties_dataset.csv')
clients_df = pd.read_csv('data/client_requests_dataset.csv')

# 初始化队列
client_queue = Queue()

# 从数据集中加载客户信息
for index, row in clients_df.iterrows():
    client = Client(row['client_ID'], row['name'], row['contact_info'], row['budget'])
    client_queue.enqueue(client)

# 初始化动态定价模型
pricing_model = DynamicPricingModel()
property = Property(1, "123 Main St", 250000, "HOUSE")

# 模拟房产浏览
for _ in range(15):
    pricing_model.track_view(property.property_id)

# 调整房产价格
pricing_model.adjust_price(property, 250000)
print("Adjusted Price:", property.price)  # 应该调整后的价格

# 测试房产匹配
matcher = PropertyMatcher()
matched = matcher.match_properties(client_queue.queue[0], properties_df.to_dict(orient='records'))
print("Matched Properties:", matched)  # 应该匹配的房产列表
