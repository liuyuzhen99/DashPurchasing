import dash
import pandas as pd
from dash import dcc, html, dash_table, callback
from dash.dependencies import Input, Output, State


from datas.excel_reader import Excel_Reader
from datas.ms_reader import Ms_Reader
from datas.tevon_reader import Tevon_Reader
from datas.detail_df_creator import Detail_df_Creator
from plotlys.ms_sum import Ms_Painter
from plotlys.ms_table import Ms_table_Painter
from plotlys.qpni_status import Qpni_Status_Painter
from plotlys.detail_excel import Detail_Excel_Painter
from plotlys.upload_filepath import Upload_Filepath_Painter

# dash.register_page(__name__)
app = dash.Dash(__name__)

config = Ms_Reader()


data = pd.DataFrame({
    'Delivery Assembly/directed parts': [config.get_VFF_milestone1(), config.get_PVS_milestone1(), config.get_0Serie_milestone1()],
    'ZP8 Ramp up 1': [config.get_VFF_milestone2(), config.get_PVS_milestone2(), config.get_0Serie_milestone2()]
},
index=['VFF', 'PVS', '0-Serie'])

excel_reader = Excel_Reader()
tevon_reader = Tevon_Reader()
detail_df_creator = Detail_df_Creator()
detail_df_creator.set_df()

ms_painter = Ms_Painter()
ms_table_painter = Ms_table_Painter(data)
qpni_status_painter = Qpni_Status_Painter()
detail_excel_painter = Detail_Excel_Painter(detail_df_creator.df)
upload_filepath_painter = Upload_Filepath_Painter()

green_VFF, yellow_VFF, red_VFF, green_PVS, yellow_PVS, red_PVS, green_0Serie, yellow_0Serie, red_0Serie = tevon_reader.get_milestone_summary()

app.layout = html.Div([
    html.Div([
        html.Div(upload_filepath_painter.upload_filepath_btn()),
        # html.Div generate report
        html.Button('Generate', id='generate-btn')
    ], style={'display': 'flex', 'justify-content': 'space-around'}),
    html.Div(id='dashboard')
    # html.Div([
    #     html.Div(ms_painter.create_milestone_sum(green_VFF, yellow_VFF, red_VFF, 'VFF'), style={'width': '15%'}),
    #     html.Div(ms_painter.create_milestone_sum(green_PVS, yellow_PVS, red_PVS, 'PVS'), style={'width': '15%'}),
    #     html.Div(ms_painter.create_milestone_sum(green_0Serie, yellow_0Serie, red_0Serie, '0-Serie'), style={'width': '15%'}),
    #     html.Div(qpni_status_painter.create_ml_sum_cluster_barplot(), style={'width': '25%'}),
    #     html.Div(ms_table_painter.table_n_btn(), style={'width': '25%', 'display': 'flex', 'justify-content': 'center', 'flex-direction': 'column'})
    # ], style={'display': 'flex'}),
    # html.Div(detail_excel_painter.detail_excel())
], style={'display': 'flex', 'flex-direction': 'column'})


@app.callback(Output('dashboard', 'children'),
          Input('generate-btn', 'n_clicks'), prevent_initial_call=True)
def generate_dashboard(generate_clicks):
    ctx = dash.callback_context
    if ctx.triggered:
        return html.Div([
            html.Div([
                html.Div(ms_painter.create_milestone_sum(green_VFF, yellow_VFF, red_VFF, 'VFF'), style={'width': '15%'}),
                html.Div(ms_painter.create_milestone_sum(green_PVS, yellow_PVS, red_PVS, 'PVS'), style={'width': '15%'}),
                html.Div(ms_painter.create_milestone_sum(green_0Serie, yellow_0Serie, red_0Serie, '0-Serie'), style={'width': '15%'}),
                html.Div(qpni_status_painter.create_ml_sum_cluster_barplot(), style={'width': '25%'}),
                html.Div(ms_table_painter.table_n_btn(), style={'width': '25%', 'display': 'flex', 'justify-content': 'center', 'flex-direction': 'column'})
            ], style={'display': 'flex'}),
            html.Div(detail_excel_painter.detail_excel())
        ])
    else:
        return None
    
if __name__ == '__main__':
    app.run(debug=True)