import dash
import pandas as pd
from dash import dcc, html, dash_table, callback
from dash.dependencies import Input, Output, State
from plotlys.q6_painter import Q6_Painter

dash.register_page(__name__)

q6_painter = Q6_Painter()

layout = q6_painter.page_init_Q6()

