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

app = dash.Dash(__name__)

def create_pie_graph1():
    colors = ['green', 'yellow', 'red']
    figure1 = go.Figure(go.Pie(labels=['Green', 'Yellow', 'Red'], values=[40, 30, 30]))
    figure1.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    showlegend=False,
    domain=dict(x=[0, 1], y=[0, 1]),
    marker=dict(colors=colors))
    return dcc.Graph(figure=figure1)

app.layout = create_pie_graph1()

if __name__ == '__main__':
    app.run_server(debug=True)