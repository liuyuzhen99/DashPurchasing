import dash
import pandas as pd
from dash import dcc, html, dash_table, callback
from dash.dependencies import Input, Output, State
import os
import base64
import io
import json


from datas.excel_reader import Excel_Reader
from datas.ms_reader import Ms_Reader
from datas.tevon_reader import Tevon_Reader
from datas.detail_df_creator import Detail_df_Creator
from plotlys.ms_sum import Ms_Painter
from plotlys.ms_table import Ms_table_Painter
from plotlys.qpni_status import Qpni_Status_Painter
from plotlys.detail_excel import Detail_Excel_Painter
from plotlys.upload_filepath import Upload_Filepath_Painter

class Q6_Painter:
    def __init__(self, ms_reader=Ms_Reader(), excel_reader = Excel_Reader(),
                tevon_reader = Tevon_Reader(),detail_df_creator = Detail_df_Creator(),
                ms_painter = Ms_Painter(), ms_table_painter = Ms_table_Painter(),
                qpni_status_painter = Qpni_Status_Painter(),detail_excel_painter = Detail_Excel_Painter(),
                upload_filepath_painter = Upload_Filepath_Painter(), app = dash.Dash(__name__) ) -> None:
        self.upload_filepath_painter = upload_filepath_painter
        self.ms_reader = ms_reader
        self.excel_reader = excel_reader
        self.tevon_reader = tevon_reader
        self.detail_df_creator = detail_df_creator
        self.ms_painter = ms_painter
        self.ms_table_painter = ms_table_painter
        self.qpni_status_painter = qpni_status_painter
        self.detail_excel_painter = detail_excel_painter
        self.data = ''
        self.app = app

    def page_init_Q6(self):
        return html.Div([
                    html.Div([
                        html.Div(self.upload_filepath_painter.upload_filepath_btn()),
                        # html.Div generate report
                        html.Button('Generate', id='generate-btn', style={
                    'backgroundColor': '#007BFF',
                    'color': 'white',
                    'padding': '10px 20px',
                    'border': 'none',
                    'cursor': 'pointer',
                    'fontSize': '16px',
                    'borderRadius': '4px',
                    'textAlign': 'center',
                    'textDecoration': 'none',
                    'display': 'inline-block',
                    'transitionDuration': '0.4s',
                    'transitionProperty': 'background-color, color, border',
                    'margin': '0px 10px',
                })
                    ], style={
                                'display': 'flex',
                                'justify-content': 'space-around',
                                'border': '2px solid #007BFF',
                                'padding': '20px',
                                'borderRadius': '8px',
                            }),
                    html.Div(id='output-dashboard')], 
                    style={'display': 'flex', 'flex-direction': 'column', 'alignItem': 'center', 'margin': '2px 0px'})
    
    def model_callback(self):
        @self.app.callback(
            Output('output-radioitems', 'children'),
            [Input('radioitems', 'value')]
        )
        def choose_model(selected_value):
            if selected_value:
                self.upload_filepath_painter.type = selected_value
                return ''
            else:
                return ''
            
    def filepath_callback(self):
        @self.app.callback([Output('output-tevon-upload', 'children'),
               Output('output-part-description-upload', 'children'),
               Output('output-mileston-json-upload', 'children'),
               ],
              [Input('upload-tevon-data', 'contents'),
               Input('upload-part-description-data', 'contents'),
               Input('upload-mileston-json-data', 'contents'),
               ],
              [State('upload-tevon-data', 'filename'),
               State('upload-part-description-data', 'filename'),
               State('upload-mileston-json-data', 'filename'),
               State('upload-tevon-data', 'last_modified'),
               State('upload-part-description-data', 'last_modified'),
               State('upload-mileston-json-data', 'last_modified'),
               ])
        def update_output(content1, content2, content3,  
                        filename1, filename2, filename3, 
                        last_modified1, last_modified2, last_modified3):
            outputs = []
            for content, filename in [(content1, filename1), (content2, filename2), (content3, filename3)]:
                if content is not None:
                    outputs.append(html.Div([
                        html.H5(f'{filename}', style={'margin': '0px'})
                    ]))
                else:
                    outputs.append(html.Div([
                        html.H5('file not uploaded', style={'margin': '0px'})
                    ]))
            if content1 is not None:
                self.upload_filepath_painter.file_path[0] = os.path.abspath(filename1)
                content_type, content_string = content1.split(',')
                decoded = base64.b64decode(content_string)
                df_tevon = pd.read_excel(io.BytesIO(decoded), skiprows=6)
                # 将tevon dataframe传到对应的类
                self.detail_df_creator.tevon_df = df_tevon
                self.tevon_reader.df = df_tevon
            if content2 is not None:
                self.upload_filepath_painter.file_path[1] = os.path.abspath(filename2)
                content_type, content_string = content2.split(',')
                decoded = base64.b64decode(content_string)
                if self.upload_filepath_painter.type == 'A6L e-tron (AU511_4CE_BL)':
                    df_part = pd.read_excel(io.BytesIO(decoded), sheet_name="A6L e-tron")
                elif self.upload_filepath_painter.type == 'Q6L e-tron (AU416_2CE_BL)':
                    df_part = pd.read_excel(io.BytesIO(decoded), sheet_name="Q6L e-tron")
                # 将part description传到对应的类
                self.excel_reader.part_description_df = df_part
                self.detail_df_creator.part_description_df = df_part
            if content3 is not None:
                self.upload_filepath_painter.file_path[2] = os.path.abspath(filename3)
                content_type, content_string = content3.split(',')
                decoded = base64.b64decode(content_string)
                js_ms = json.loads(decoded)
                # 将json传到对应的类
                self.ms_reader.config_data = js_ms
            return outputs
    
    def upload_filepath_callback(self):
        @self.app.callback(
            Output('output-dashboard', 'children'),
            Input('generate-btn', 'n_clicks')
        )
        def generate_dashboard(n_clicks):
            # print(self.upload_filepath_painter.file_path)
            if n_clicks and len(self.upload_filepath_painter.file_path) == 3:
                if self.upload_filepath_painter.file_path[0] != '' and self.upload_filepath_painter.file_path[1] != '' and self.upload_filepath_painter.file_path[2] != '':
                    self.data = pd.DataFrame({
                        'Delivery Assembly/directed parts': [self.ms_reader.get_VFF_milestone1(), self.ms_reader.get_PVS_milestone1(), self.ms_reader.get_0Serie_milestone1()],
                        'ZP8 Ramp up 1': [self.ms_reader.get_VFF_milestone2(), self.ms_reader.get_PVS_milestone2(), self.ms_reader.get_0Serie_milestone2()]
                    },
                    index=['VFF', 'PVS', '0-Serie'])
        
                    if self.upload_filepath_painter.type == 'A6L e-tron (AU511_4CE_BL)':
                        self.detail_df_creator.file_path_start = r"C:\****\Shared Documents - NEV Co. QPNi\03_A6L e-tron (AU511_4CE_BL)"
                        # self.detail_df_creator.file_path_start = r"C:\****\03_A6L e-tron (AU511_4CE_BL)"
                    elif self.upload_filepath_painter.type == 'Q6L e-tron (AU416_2CE_BL)':
                        self.detail_df_creator.file_path_start = r"C:\****\Shared Documents - NEV Co. QPNi\02_Q6L e-tron (AU416_2CE_BL)"
                        # self.detail_df_creator.file_path_start = r"C:\****\02_Q6L e-tron (AU416_2CE_BL)"
                    self.excel_reader.path_start = self.detail_df_creator.file_path_start
                    self.detail_df_creator.excel_reader = self.excel_reader
                    self.detail_df_creator.ms_reader = self.ms_reader
                    self.detail_df_creator.set_df()
                    self.ms_table_painter.data = self.data
                    self.tevon_reader.ms_reader = self.ms_reader
                    self.detail_excel_painter.df = self.detail_df_creator.df
                    self.qpni_status_painter.excel_reader = self.excel_reader
                    self.qpni_status_painter.tevon_reader = self.tevon_reader

                    green_VFF, yellow_VFF, red_VFF, green_PVS, yellow_PVS, red_PVS, green_0Serie, yellow_0Serie, red_0Serie = self.tevon_reader.get_milestone_summary()
                    return html.Div([
                        html.Div([
                            html.Div(self.ms_painter.create_milestone_sum(green_VFF, yellow_VFF, red_VFF, self.ms_reader.get_VFF_milestone1(), self.ms_reader.get_VFF_milestone2(), 'VFF'), style={'width': '20%'}),
                            html.Div(self.ms_painter.create_milestone_sum(green_PVS, yellow_PVS, red_PVS, self.ms_reader.get_PVS_milestone1(), self.ms_reader.get_PVS_milestone2(), 'PVS'), style={'width': '20%'}),
                            html.Div(self.ms_painter.create_milestone_sum(green_0Serie, yellow_0Serie, red_0Serie, self.ms_reader.get_0Serie_milestone1(), self.ms_reader.get_0Serie_milestone2(), '0-Serie'), style={'width': '20%'}),
                            html.Div(self.qpni_status_painter.create_ml_sum_cluster_barplot(), style={'width': '25%'}),
                            # html.Div(self.ms_table_painter.table_n_btn(), style={'width': '25%', 'display': 'flex', 'justify-content': 'center', 'flex-direction': 'column'})
                        ], style={'display': 'flex', 'width': '100%', 'justifyContent': 'space-around'}),
                        html.Div(self.detail_excel_painter.detail_excel(), style={'height': '50vh'})
                    ])
                else:
                    return "<script>alert('Pls select all the files!);</script>"
            else:
                return None
            
    
