from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

def analyze_data(root, properties_df):
    # 数据分析
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # 房产价格分布
    properties_df['price'].plot(kind='hist', bins=20, ax=ax, title='Property Price Distribution')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
