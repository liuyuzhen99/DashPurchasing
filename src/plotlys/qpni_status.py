import plotly.graph_objs as go
from dash import dcc, html
from datas.excel_reader import Excel_Reader
from datas.tevon_reader import Tevon_Reader

class Qpni_Status_Painter:
    def __init__(self, excel_reader=Excel_Reader(), tevon_reader=Tevon_Reader()) -> None:
        self.excel_reader = excel_reader
        self.tevon_reader = tevon_reader

    def create_ml_sum_cluster_barplot(self):
        # file_path_start = r"C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\Shared Documents - NEV Co. QPNi\A6L e-tron (AU511_4CE_BL)"
        ml_list = self.excel_reader.ml_sum_status()
        # print(ml_list)
        # ml3_list = self.excel_reader.ml_sum_status('ml3')
        # ml4_list = self.excel_reader.ml_sum_status('ml4')
        # ml5_list = self.excel_reader.ml_sum_status('ml5')
        # ml6_list = self.excel_reader.ml_sum_status('ml6')
        # ml7_list = self.excel_reader.ml_sum_status('ml7')
        categories = ['ML2', 'ML3', 'ML4', 'ML5', 'ML6', 'ML7']
        data1 = [ml_list[0][0], ml_list[1][0], ml_list[2][0], ml_list[3][0], ml_list[4][0], ml_list[5][0]]
        data2 = [ml_list[0][1], ml_list[1][1], ml_list[2][1], ml_list[3][1], ml_list[4][1], ml_list[5][1]]
        data3 = [ml_list[0][2], ml_list[1][2], ml_list[2][2], ml_list[3][2], ml_list[4][2], ml_list[5][2]]
        data4 = [ml_list[0][3], ml_list[1][3], ml_list[2][3], ml_list[3][3], ml_list[4][3], ml_list[5][3]]
        trace1 = go.Bar(x=categories, y=data1, marker=dict(color='rgb(255,0,0)'))
        trace2 = go.Bar(x=categories, y=data2, marker=dict(color='rgb(255,255,0)'))
        trace3 = go.Bar(x=categories, y=data3, marker=dict(color='rgb(0,255,0)'))
        trace4 = go.Bar(x=categories, y=data4, marker=dict(color='rgb(128,128,128)'))
        fig = go.Figure(data=[trace1, trace2, trace3, trace4])
        fig.update_layout(barmode='relative', title='QPNI-Status', showlegend=False)
        return dcc.Graph(figure=fig)