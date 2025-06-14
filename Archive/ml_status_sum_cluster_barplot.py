import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash import dash_table
import webbrowser
import threading
import time
from config_handler import Config
from cluster_bar_plot import create_ml_sum_cluster_barplot


def open_browser():
    time.sleep(1)
    webbrowser.open_new('http://127.0.0.1:8050/')


def run_dash_server():
    app.run_server(debug=False)


app = dash.Dash(__name__)


def create_layout():
    return html.Div([
        html.Div(create_ml_sum_cluster_barplot(), style={
            'width': '50%',
            'display': 'inline-block'
        }),
    ])


app.layout = create_layout()

if __name__ == '__main__':
    # app_thread = threading.Thread(target=run_dash_server)
    # app_thread.daemon = True
    # app_thread.start()
    #
    # open_browser()
    #
    # app_thread.join()
    app.run_server(debug=True)
