import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import os
import pandas as pd
import base64
import io
import json

app = dash.Dash(__name__)

filepath = ['', '', '']

# 布局
app.layout = html.Div([
    # dcc.Upload(id='upload-data', children=html.Div(['将文件拖放到此处或选择文件']), multiple=False),
    html.Div([
        dcc.Upload(id='upload-tevon-data', children=html.Button('TEVON EXCEL UPLOAD'), multiple=False),
        html.Div(id='output-tevon-upload')
    ], style={'display': 'flex', 'flex-direction': 'column'}),
    html.Div([
        dcc.Upload(id='upload-part-description-data', children=html.Button('PART DESCRIPTION UPLOAD'), multiple=False),
        html.Div(id='output-part-description-upload')
    ], style={'display': 'flex', 'flex-direction': 'column'}),
    html.Div([
        dcc.Upload(id='upload-mileston-json-data', children=html.Button('MILESTON JSON UPLOAD'), multiple=False),
        html.Div(id='output-mileston-json-upload')
    ], style={'display': 'flex', 'flex-direction': 'column'})
], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-around'})

@app.callback([Output('output-tevon-upload', 'children'),
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
            # file_path = os.path.abspath(filename)
            outputs.append(html.Div([
                html.H5(f'selected file: {filename}')
            ]))
        else:
            outputs.append(html.Div([
                html.H5('file not uploaded')
            ]))
    if content1 is not None:
        content_type, content_string = content1.split(',')
        decoded = base64.b64decode(content_string)
        # filepath[0] = os.path.abspath(filename1)
        df = pd.read_excel(io.BytesIO(decoded),skiprows=6)
        print(df)
    if content2 is not None:
        content_type, content_string = content2.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_excel(io.BytesIO(decoded), sheet_name="Q6L e-tron")
        print(df)
    if content3 is not None:
        content_type, content_string = content3.split(',')
        decoded = base64.b64decode(content_string)
        filepath[2] = os.path.abspath(filename3)
        df1 = json.loads(decoded)
        print(df1)
    # print(filepath)
    return outputs
        
if __name__ == '__main__':
    app.run(debug=True)