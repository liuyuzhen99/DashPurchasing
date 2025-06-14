import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import os

class Upload_Filepath_Painter:
    def __init__(self, app=dash.Dash(__name__)) -> None:
        self.file_path = ['','','']
        self.app = app
        self.type = ''

    def upload_filepath_btn(self):
        return html.Div([
            # dcc.Upload(id='upload-data', children=html.Div(['将文件拖放到此处或选择文件']), multiple=False),
            html.Div([
                dcc.RadioItems(
                    id='radioitems',
                    options=[
                        {'label': 'A6L e-tron', 'value': 'A6L e-tron (AU511_4CE_BL)'},
                        {'label': 'Q6L e-tron', 'value': 'Q6L e-tron (AU416_2CE_BL)'}
                    ],
                    value='',
                    style={'display': 'inline-block'}
                ),
                html.Div(id='output-radioitems')
            ]),
            html.Div([
                dcc.Upload(id='upload-tevon-data', children=html.Button('TEVON EXCEL UPLOAD', style={
                    'backgroundColor': '#4CAF50',
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
                }), multiple=False),
                html.Div(id='output-tevon-upload', style={
                            'color': '#333',
                            'fontSize': '20px',
                            'fontFamily': 'Arial',
                            'margin': '0px',
                        })
            ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),
            html.Div([
                dcc.Upload(id='upload-part-description-data', children=html.Button('PART DESCRIPTION UPLOAD', style={
                    'backgroundColor': '#4CAF50',
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
                }), multiple=False),
                html.Div(id='output-part-description-upload', style={
                            'color': '#333',
                            'fontSize': '20px',
                            'fontFamily': 'Arial',
                            'margin': '0px',
                        })
            ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),
            html.Div([
                dcc.Upload(id='upload-mileston-json-data', children=html.Button('MILESTON JSON UPLOAD', style={
                    'backgroundColor': '#4CAF50',
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
                }), multiple=False),
                html.Div(id='output-mileston-json-upload', style={
                            'color': '#333',
                            'fontSize': '20px',
                            'fontFamily': 'Arial',
                            'margin': '0px',
                        })
            ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'})
        ], style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'space-around', 'height': 'auto'})
    
    # def filepath_callback(self):
    #     @self.app.callback([Output('output-tevon-upload', 'children'),
    #            Output('output-part-description-upload', 'children'),
    #            Output('output-mileston-json-upload', 'children'),
    #            ],
    #           [Input('upload-tevon-data', 'contents'),
    #            Input('upload-part-description-data', 'contents'),
    #            Input('upload-mileston-json-data', 'contents'),
    #            ],
    #           [State('upload-tevon-data', 'filename'),
    #            State('upload-part-description-data', 'filename'),
    #            State('upload-mileston-json-data', 'filename'),
    #            State('upload-tevon-data', 'last_modified'),
    #            State('upload-part-description-data', 'last_modified'),
    #            State('upload-mileston-json-data', 'last_modified'),
    #            ])
    #     def update_output(content1, content2, content3,  
    #                     filename1, filename2, filename3, 
    #                     last_modified1, last_modified2, last_modified3):
    #         outputs = []
    #         for content, filename in [(content1, filename1), (content2, filename2), (content3, filename3)]:
    #             if content is not None:
    #                 outputs.append(html.Div([
    #                     html.H5(f'selected file: {filename}')
    #                 ]))
    #             else:
    #                 outputs.append(html.Div([
    #                     html.H5('file not uploaded')
    #                 ]))
    #         if content1 is not None:
    #             self.file_path[0] = os.path.abspath(filename1)
    #         if content2 is not None:
    #             self.file_path[1] = os.path.abspath(filename2)
    #         if content3 is not None:
    #             self.file_path[2] = os.path.abspath(filename3)
    #         print(self.file_path)
    #         return outputs