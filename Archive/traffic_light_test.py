import dash
from dash import html

# 创建一个Dash应用
app = dash.Dash(__name__)

# 定义一个CSS样式，用于显示圆形
circle_style = {
    'height': '50px',
    'width': '50px',
    'background-color': 'red',
    'border-radius': '50%',
}

# 数据
data = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob', 'Age': 30},
    {'Name': 'Charlie', 'Age': 35}
]

# 创建一个布局，显示一个红色圆形在表格中的单元格中
app.layout = html.Table(
    # 创建表格行
    [
        html.Tr(
            # 在表格行中创建两个单元格
            [
                html.Td(
                    # 在单元格中放置数据或红色的圆
                    data[row_idx][col] if col not in data[row_idx] else html.Div(style=circle_style)
                ) for col in ['Name', 'Age']  # 两列：Name 和 Age
            ]
        ) for row_idx in range(len(data))  # 行数等于数据行数
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
