import plotly.graph_objs as go
from dash import dcc, html
from traversal_file_test import traversalDir_SecDir
from excel_reader_test import ml_sum_status
from tevon_test import get_milestone_summary


def create_ml_sum_cluster_barplot():
    file_path_start = r"C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\Shared Documents - NEV Co. QPNi\A6L e-tron (AU511_4CE_BL)"
    ml2_list = ml_sum_status(file_path_start,'ml2')
    ml3_list = ml_sum_status(file_path_start,'ml3')
    ml4_list = ml_sum_status(file_path_start,'ml4')
    ml5_list = ml_sum_status(file_path_start,'ml5')
    ml6_list = ml_sum_status(file_path_start,'ml6')
    ml7_list = ml_sum_status(file_path_start,'ml7')
    categories = ['ML2', 'ML3', 'ML4', 'ML5', 'ML6', 'ML7']
    data1 = [ml2_list[0], ml3_list[0], ml4_list[0], ml5_list[0], ml6_list[0], ml7_list[0]]
    data2 = [ml2_list[1], ml3_list[1], ml4_list[1], ml5_list[1], ml6_list[1], ml7_list[1]]
    data3 = [ml2_list[2], ml3_list[2], ml4_list[2], ml5_list[2], ml6_list[2], ml7_list[2]]
    trace1 = go.Bar(x=categories, y=data1, marker=dict(color='rgb(255,0,0)'), name='red')
    trace2 = go.Bar(x=categories, y=data2, marker=dict(color='rgb(255,255,0)'), name='yellow')
    trace3 = go.Bar(x=categories, y=data3, marker=dict(color='rgb(0,255,0)'), name='green')
    fig = go.Figure(data=[trace1, trace2, trace3])
    fig.update_layout(barmode='relative', title='QPNI-Status')
    return dcc.Graph(figure=fig)

green_VFF, yellow_VFF, red_VFF, green_PVS, yellow_PVS, red_PVS, green_0Serie, yellow_0Serie, red_0Serie = get_milestone_summary()

def create_VFF_milestone_sum(green_VFF,yellow_VFF,red_VFF):
    data = [
        go.Bar(
            x=['G', 'Y', 'R'],
            y=[green_VFF,yellow_VFF,red_VFF],
            marker=dict(color=['green', 'yellow', 'red'])
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title='VFF milestone summary')
    return dcc.Graph(figure=fig)

def create_PVS_milestone_sum(green_PVS, yellow_PVS, red_PVS):
    data = [
        go.Bar(
            x=['G', 'Y', 'R'],
            y=[green_PVS, yellow_PVS, red_PVS],
            marker=dict(color=['green', 'yellow', 'red'])
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title='PVS milestone summary')
    return dcc.Graph(figure=fig)

def create_0Serie_milestone_sum(green_0Serie, yellow_0Serie, red_0Serie):
    data = [
        go.Bar(
            x=['G', 'Y', 'R'],
            y=[green_0Serie, yellow_0Serie, red_0Serie],
            marker=dict(color=['green', 'yellow', 'red'])
        )
    ]
    fig = go.Figure(data=data)
    fig.update_layout(title='0-Serie milestone summary')
    return dcc.Graph(figure=fig)