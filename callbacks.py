import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

from app import app
from data.data import *

@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions] + [Input('color', 'value')])
def make_figure(x, y, z, color):
    return px.scatter_3d(
        viz_df,
        x=x,
        y=y,
        z=z,
        color=color,
        symbol='source',
        height=500,
        hover_name='headline',
        hover_data=text_data,
    )
