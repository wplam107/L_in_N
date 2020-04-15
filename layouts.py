import dash
import dash_core_components as dcc
import dash_html_components as html
from data.data import *

index_page = html.Div([
    html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]),
    html.H1('Language in News', style={'textAlign': 'center'}),
    html.Br([]), html.Br([]), html.Br([]),
    html.Div('Wayne Lam', style={'textAlign': 'center'}),
    html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]),
    html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]), html.Br([]),
    html.Br([]), html.Br([]), html.Br([]),
    dcc.Link('PCA Scatter Plot', href='/page-1', style={'textAlign': 'center', 'color': 'black'}),
    html.Br([]),
    dcc.Link('Feature Scatter Plot', href='/page-2', style={'textAlign': 'center', 'color': 'black'}),
])

page_1_layout = html.Div(id='page-1-content', children=[
        html.H1('Reduced Dimensions of News Articles', style={'textAlign': 'center'}),
        html.P('Dimensionality reduction (PCA) of 17 features to 6 dimensions', style={'textAlign': 'center'}),
        html.Br(),
        html.P(['This plot allows you to select 3 different principal components as dimensions ',
        'in addition to the different clustering algorithms.  ',
        'The colors are different clusters.']),
        html.Br(),
        dcc.Link('Home', href='/', style={'textAlign': 'center', 'color': 'black'}),
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
        html.Br(),
        dcc.Graph(id='dist', style={"width": "80%", "display": "inline-block"})
    ]
)

page_2_layout = html.Div(id='page-2-content', children=[
        html.H1('Topic/Sentiment of News Articles', style={'textAlign': 'center'}),
        html.P('Dimensions ', style={'textAlign': 'center'}),
        html.Br(),
        html.P(['This plot allows you to select 3 different features as dimensions ',
        'in addition to the different clustering algorithms.  ',
        'The colors are different clusters.']),
        html.Br(),
        dcc.Link('Home', href='/', style={'textAlign': 'center', 'color': 'black'}),
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
        html.Br(),
        dcc.Graph(id='dist', style={"width": "80%", "display": "inline-block"})
    ]
)