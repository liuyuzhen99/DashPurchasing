import dash
import pandas as pd
from dash import dcc, html, dash_table, callback
from dash.dependencies import Input, Output, State
from Archive.a6_painter import A6_Painter

# dash.register_page(__name__)

a6_painter = A6_Painter()

layout = a6_painter.page_init_A6()