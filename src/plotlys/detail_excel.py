from datas.detail_df_creator import Detail_df_Creator
from dash import dcc, html, dash_table
import pandas as pd

class Detail_Excel_Painter:
    def __init__(self, df=pd.DataFrame()) -> None:
        self.df = df

    def detail_excel(self):
        table = dash_table.DataTable(id='detail-table', 
                                     style_data={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                        'fontFamily': 'Arial',
                                        'fontSize':'10px',
                                    },
                                    style_header={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                        'fontFamily': 'Arial',
                                        'fontSize':'10px',
                                        'backgroundColor': '#ccc',
	                                    'color': '#222',
                                        'fontWeight': 'bold',
                                    },
                                    style_filter={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                        'fontFamily': 'Arial',
                                        'fontSize':'10px',
                                        'backgroundColor': '#ccc',
	                                    'color': '#222',
                                        'fontWeight': 'bold',
                                    },
                                    style_cell_conditional=[
                                        {'if': {'column_id': 'Actions'},
                                        'width': '35%'},
                                        {'if': {'column_id': 'Part Description'},
                                        'width': '10%'},
                                        {'if': {'column_id': 'Part Number'},
                                        'width': '7%'},
                                        {'if': {'column_id': 'Status'},
                                        'width': '5%'},
                                        {'if': {'column_id': 'TEVON Status'},
                                        'width': '5%'},
                                        {'if': {'column_id': 'CORE'},
                                        'width': '4%'},
                                        {'if': {'column_id': 'VFF'},
                                        'width': '3%'},
                                        {'if': {'column_id': 'PVS'},
                                        'width': '3%'},
                                        {'if': {'column_id': '0-Serie'},
                                        'width': '5%'},
                                        {'if': {'column_id': 'Responsible'},
                                        'width': '7%'},
                                        {'if': {'column_id': 'Subgroup'},
                                        'width': '6%'},
                                        {'if': {'column_id': 'Supplier'},
                                        'width': '10%'},
                                    ],
                                    columns=[{'name': col, 'id': col, 'hideable': True, 'editable': col == 'Actions'} for col in self.df.columns],
                                    style_data_conditional=[
                                        {
                                            'if': {
                                                'column_id': 'Status',
                                                'filter_query': '{Status} = "yellow"'
                                            },
                                            'backgroundColor': 'yellow'
                                        },
                                        {
                                            'if': {
                                                'column_id': 'Status',
                                                'filter_query': '{Status} = "red"'
                                            },
                                            'backgroundColor': 'red'
                                        },
                                        {
                                            'if': {
                                                'column_id': 'Status',
                                                'filter_query': '{Status} = "green"'
                                            },
                                            'backgroundColor': 'green'
                                        },
                                        {
                                            'if': {
                                                'column_id': 'TEVON Status',
                                                'filter_query': '{TEVON Status} = "yellow"'
                                            },
                                            'backgroundColor': 'yellow'
                                        },
                                        {
                                            'if': {
                                                'column_id': 'TEVON Status',
                                                'filter_query': '{TEVON Status} = "green"'
                                            },
                                            'backgroundColor': 'green'
                                        },
                                        {
                                            'if': {
                                                'column_id': 'TEVON Status',
                                                'filter_query': '{TEVON Status} = "red"'
                                            },
                                            'backgroundColor': 'red'
                                        }
                                    ],
                                    data=self.df.to_dict('records'),
                                    export_format='xlsx',
                                    export_headers='display',
                                    merge_duplicate_headers=True,
                                    page_action="native",
                                    page_current= 0,
                                    page_size= 15,
                                    fixed_rows={'headers': True},
                                    filter_action='native')
        return table
    
    # table = dash_table.DataTable(id='detail-table', 
    #                          style_data={
    #                             'whiteSpace': 'normal',
    #                             'height': 'auto',
    #                         },
    #                         style_header={
    #                             'whiteSpace': 'normal',
    #                             'height': 'auto',
    #                         },
    #                         columns=[{'name': col, 'id': col, 'hideable': True} for col in df.columns],
    #                         style_cell_conditional=[
    #                             {'if': {'column_id': 'Actions'},
    #                             'width': '35%'},
    #                             {'if': {'column_id': 'Part Description'},
    #                             'width': '10%'},
    #                             {'if': {'column_id': 'Part Number'},
    #                             'width': '7%'},
    #                             {'if': {'column_id': 'Status'},
    #                             'width': '5%'},
    #                             {'if': {'column_id': 'TEVON Status'},
    #                             'width': '5%'},
    #                             {'if': {'column_id': 'CORE'},
    #                             'width': '4%'},
    #                             {'if': {'column_id': 'VFF'},
    #                             'width': '3%'},
    #                             {'if': {'column_id': 'PVS'},
    #                             'width': '3%'},
    #                             {'if': {'column_id': '0-Serie'},
    #                             'width': '5%'},
    #                             {'if': {'column_id': 'Responsible'},
    #                             'width': '7%'},
    #                             {'if': {'column_id': 'Subgroup'},
    #                             'width': '6%'},
    #                             {'if': {'column_id': 'Supplier'},
    #                             'width': '10%'},
    #                         ],
    #                         data=df.to_dict('records'),
    #                         fixed_rows={'headers': True},
    #                         filter_action='native')