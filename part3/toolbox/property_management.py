import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))  # 将父级目录加入执行目录列表

import tkinter as tk
from tkinter import messagebox
import pandas as pd
from part1.toolbox.property import Property
from part1.toolbox.client import Client
from part1.toolbox.queue import Queue
from part1.toolbox.avl_tree import AVLTree


# 加载数据集
properties_df = pd.read_csv('data/real_estate_properties_dataset.csv')
clients_df = pd.read_csv('data/client_requests_dataset.csv')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def analyze_data(root, properties_df):
    # 数据分析
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # 房产价格分布
    properties_df['price'].plot(kind='hist', bins=20, ax=ax, title='Property Price Distribution')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()



def display_property(root, property, add_to_favorites, request_viewing):
    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text=f"Property ID: {property.property_id}").pack()
    tk.Label(frame, text=f"Address: {property.address}").pack()
    tk.Label(frame, text=f"Price: {property.price}").pack()
    tk.Label(frame, text=f"Type: {property.property_type.value}").pack()
    tk.Label(frame, text=f"Status: {property.status.value}").pack()
    tk.Label(frame, text=f"Owner: {property.owner}").pack()

    tk.Button(frame, text="Add to Favorites", command=lambda p=property: add_to_favorites(p)).pack(side=tk.LEFT)
    tk.Button(frame, text="Request Viewing", command=lambda p=property: request_viewing(p)).pack(side=tk.RIGHT)


class PropertyManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Property Management System")
        self.property_tree = AVLTree()
        self.client_queue = Queue()
        self.favorites = []
        self.load_data()
        self.add_widgets()

    def load_data(self):
        # 从数据集中加载房产信息
        for index, row in properties_df.iterrows():
            prop = Property(row['property_ID'], row['address'], row['price'], row['property_type'], row['status'], row['owner'])
            self.property_tree.root = self.property_tree.insert(self.property_tree.root, prop.property_id, prop)
        
        # 从数据集中加载客户信息
        for index, row in clients_df.iterrows():
            client = Client(row['client_ID'], row['name'], row['contact_info'], row['budget'])
            self.client_queue.enqueue(client)

    def add_widgets(self):
        self.add_property_button = tk.Button(self.root, text="Add Property", command=self.add_property)
        self.add_property_button.pack()

        self.view_properties_button = tk.Button(self.root, text="View Properties", command=self.view_properties)
        self.view_properties_button.pack()

        self.view_favorites_button = tk.Button(self.root, text="View Favorites", command=self.view_favorites)
        self.view_favorites_button.pack()

        self.analyze_data_button = tk.Button(self.root, text="Analyze Data", command=self.analyze_data)
        self.analyze_data_button.pack()
    def analyze_data(self):
        # 在这里定义数据分析的方法
        analyze_data(self.root, properties_df)
        self.analyze_data_button = tk.Button(self.root, text="Analyze Data", command=self.analyze_data)
        self.analyze_data_button.pack()
    
    def add_property(self):
        prop = Property(6, "202 Cedar St", 350000, "HOUSE")
        self.property_tree.root = self.property_tree.insert(self.property_tree.root, prop.property_id, prop)
        messagebox.showinfo("Info", "Property added")

    def view_properties(self):
        properties = self.in_order_traversal(self.property_tree.root)
        for prop in properties:
            display_property(self.root, prop, self.add_to_favorites, self.request_viewing)

    def view_favorites(self):
        for prop in self.favorites:
            print(prop)

    def add_to_favorites(self, property):
        self.favorites.append(property)
        messagebox.showinfo("Info", "Property added to favorites")

    def request_viewing(self, property):
        messagebox.showinfo("Request Viewing", f"Viewing requested for {property.address}")

    def in_order_traversal(self, root):
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.value)
            res = res + self.in_order_traversal(root.right)
        return res
