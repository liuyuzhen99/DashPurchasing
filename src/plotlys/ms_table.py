import datetime
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd

class Ms_table_Painter:
    def __init__(self, data = pd.DataFrame(), app = dash.Dash(__name__)) -> None:
        self.app = app
        self.data = data

    def data_2_dict(self):
        data_dict = self.data.to_dict('index') 
        for key, value in data_dict.items(): value[' '] = key
        return data_dict

    def table_n_btn(self):
        edit_button  = html.Button('编辑', id='edit-button', n_clicks=0)
        confrim_button = html.Button('确认', id='confirm-button', n_clicks=0, style={'display': 'none'})
        table = dash_table.DataTable(id='editable-table', columns=[{'name': ' ', 'id': ' ', 'editable': False}] +
                                                           [{'name': col, 'id': col} for col in self.data.columns], 
                                                           data=[value for value in self.data_2_dict().values()], 
                                                           editable=False, 
                                                           merge_duplicate_headers=True)
        return html.Div([
        html.Div([edit_button, confrim_button]),
        table
        ])

    def table_callback1(self):
        @self.app.callback(
            [Output('editable-table', 'editable'),
            Output('edit-button', 'style'),
            Output('confirm-button', 'style')],
            [Input('edit-button', 'n_clicks'),
            Input('confirm-button', 'n_clicks')],
            [State('editable-table', 'editable')],
            prevent_initial_call=True
        )
        def toggle_editable_mode(edit_clicks, confirm_clicks, current_editable):
            ctx = dash.callback_context
            if not ctx.triggered:
                return False, {'display': 'inline-block'}, {'display': 'none'}
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            if button_id == 'edit-button':
                return True, {'display': 'none'}, {'display': 'inline-block'}
            elif button_id == 'confirm-button':
                return False, {'display': 'inline-block'}, {'display': 'none'}
            
    def table_callback2(self):
        @self.app.callback(
            Output('editable-table', 'data'),
            [Input('confirm-button', 'n_clicks')],
            [State('editable-table', 'data')],
            prevent_initial_call=True
        )
        def update_data(confirm_clicks, table_data):
            ctx = dash.callback_context
            if not ctx.triggered:
                return dash.no_update
            # new_data = pd.DataFrame(table_data)
            # 将更改后的milestone数据保存到文件中
                # config.set_VFF_milestone1(new_data.loc[0, 'Delivery Assembly/directed parts'])
                # config.set_VFF_milestone2(new_data.loc[0, 'ZP8 Ramp up 1'])
                # config.set_PVS_milestone1(new_data.loc[1, 'Delivery Assembly/directed parts'])
                # config.set_PVS_milestone2(new_data.loc[1, 'ZP8 Ramp up 1'])
                # config.set_0Serie_milestone1(new_data.loc[2, 'Delivery Assembly/directed parts'])
                # config.set_0Serie_milestone2(new_data.loc[2, 'ZP8 Ramp up 1'])
            return table_data
    