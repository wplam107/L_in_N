import dash
import dash_core_components as dcc
import dash_html_components as html
import pickle
import plotly.express as px
from dash.dependencies import Input, Output
from app import app

file = open('apps/pickles/viz_df.p', 'rb')
viz_df = pickle.load(file)
file.close()

comps = ['pc1', 'pc2', 'pc3', 'pc4', 'pc5', 'pc6']
text_data = ['protest', 'gov', 'econ', 'poli', 'date']
col_options = [dict(label=x, value=x) for x in comps]
dimensions = ["x", "y", "z"]
models = ['Hierarchical', 'K-Means', 'Mean Shift', 'Spectral']

layout = html.Div(
    [
        html.H1("Dimensions of News Articles"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ]
                + [html.P(dcc.RadioItems(
                    id='color',
                    options=[{'label': i, 'value': i} for i in models],
                    value='K-Means',
                    # labelStyle={'display': 'inline-block'},
                    # style={"width": "25%", "float": "left"},
        ))]),
        dcc.Graph(id="graph", style={"width": "100%", "display": "inline-block"}),
    ]
)


@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions] + [Input('color', 'value')])
def make_figure(x, y, z, color):
    return px.scatter_3d(
        viz_df,
        x=x,
        y=y,
        z=z,
        color=color,
        symbol='source',
        height=700,
        hover_name='headline',
        hover_data=text_data,
    )
