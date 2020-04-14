import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pickle
import plotly.express as px
from dash.dependencies import Input, Output

file = open('viz_df.p', 'rb')
viz_df = pickle.load(file)
file.close()

comps = ['pc1', 'pc2', 'pc3', 'pc4', 'pc5', 'pc6']
text_data = ['sample', 'url', 'date']
col_options = [dict(label=x, value=x) for x in comps]
sentiment = ['w_protest', 'w_econ', 'w_gov', 'w_poli', 'protest_ratio', 'econ_ratio', 'gov_ratio', 'poli_ratio']
sent_options = [dict(label=x, value=x) for x in sentiment]
dimensions = ["x", "y", "z"]
models = ['Hierarchical', 'K-Means', 'Mean Shift', 'Spectral']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]),
    html.H1('Language in News', style={'textAlign': 'center'}),
    html.Br([]), html.Br([]), html.Br([]),
    html.Div('Wayne Lam', style={'textAlign': 'center'}),
    html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]),
    html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]),
    dcc.Link('Next Page', href='/page-1', style={'textAlign': 'center', 'color': 'black'}),
    # dcc.Link('Go to Page 2', href='/page-2'),
])

page_1_layout = html.Div(id='page-1-content', children=[
        html.H1('Reduced Dimensions of News Articles', style={'textAlign': 'center'}),
        html.P('Dimensionality reduction (PCA) of 17 features to 6 dimensions', style={'textAlign': 'center'}),
        html.Br(),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ]
                + [html.P(dcc.RadioItems(
                    id='color',
                    options=[{'label': i, 'value': i} for i in models],
                    value='K-Means',
        ))]),
        dcc.Graph(id="graph", style={"width": "80%", "display": "inline-block"}),
        dcc.Link('Next Page', href='/page-2', style={'textAlign': 'center', 'color': 'black'}),
    ]
)

page_2_layout = html.Div(id='page-2-content', children=[
        html.H1('Topic/Sentiment of News Articles', style={'textAlign': 'center'}),
        html.P('Dimensions ', style={'textAlign': 'center'}),
        html.Br(),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=sent_options)])
                for d in dimensions
            ]
                + [html.P(dcc.RadioItems(
                    id='color',
                    options=[{'label': i, 'value': i} for i in models],
                    value='K-Means',
        ))]),
        dcc.Graph(id="graph", style={"width": "80%", "display": "inline-block"}),
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
        height=500,
        hover_name='headline',
        hover_data=text_data,
    )

# page_2_layout = html.Div([
#     html.H1('Page 2'),
#     dcc.RadioItems(
#         id='page-2-radios',
#         options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
#         value='Orange'
#     ),
#     html.Div(id='page-2-content'),
#     html.Br(),
#     dcc.Link('Go to Page 1', href='/page-1'),
#     html.Br(),
#     dcc.Link('Go back to home', href='/')
# ])

# @app.callback(dash.dependencies.Output('page-2-content', 'children'),
#               [dash.dependencies.Input('page-2-radios', 'value')])
# def page_2_radios(value):
#     return 'You have selected "{}"'.format(value)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page

if __name__ == '__main__':
    app.run_server(debug=True)