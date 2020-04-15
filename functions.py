import numpy as np
import pandas as pd
import pickle
import plotly.graph_objects as go


# Function to group sources by model cluster
def source_group(mod):
    labels = sorted(viz_df[mod].unique())
    a = pd.DataFrame(viz_df.groupby('source')[mod].value_counts(normalize=True, sort=False))
    a = round(a.unstack() * 100, 1)
    a = np.where(a.isna(), 0, a)
    return labels, a

# Function to plot horizontal bars (stacked)
def h_bar(mod):
    sources = ['ABC (Australia)', 'CCTV', 'CNN', 'Reuters', 'SCMP']
    labels, ls = source_group(mod)
    x_data = ls
    y_data = sources
    top_labels = labels
    colors = ['rgba(38, 24, 74, 0.8)', 'rgba(71, 58, 131, 0.8)',
              'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)']

    fig = go.Figure()

    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            fig.add_trace(go.Bar(
                x=[xd[i]], y=[yd],
                orientation='h',
                hovertemplate='Source: %{yd}, '
                marker=dict(
                    color=colors[i],
                    line=dict(color='rgb(248, 248, 249)', width=1)
                )
            ))

    fig.update_layout(
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
            domain=[0.15, 1]
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        barmode='stack',
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        margin=dict(l=10, r=40, t=140, b=80),
        showlegend=False,
    )

    annotations = []

    for yd, xd in zip(y_data, x_data):
        # labeling the y-axis
        annotations.append(dict(xref='paper', yref='y',
                                x=0.14, y=yd,
                                xanchor='right',
                                text=str(yd),
                                font=dict(family='Arial', size=10,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False, align='right'))
        # labeling the first percentage of each bar (x_axis)
        annotations.append(dict(xref='x', yref='y',
                                x=xd[0] / 2, y=yd,
                                text=str(xd[0]) + '%',
                                font=dict(family='Arial', size=10,
                                          color='rgb(248, 248, 255)'),
                                showarrow=False))
        # labeling the first cluster of a model (on the top)
        if yd == y_data[-1]:
            annotations.append(dict(xref='x', yref='paper',
                                    x=xd[0] / 2, y=1.1,
                                    text=top_labels[0],
                                    font=dict(family='Arial', size=10,
                                              color='rgb(67, 67, 67)'),
                                    showarrow=False))
        space = xd[0]
        for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=10,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # Labeling clusters of model
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=10,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]

    fig.update_layout(annotations=annotations)
    fig.update_layout(
        title={'text': f'{mod} Cluster Groups by Source',
               'y':0.9,
               'x':0.5,
               'xanchor': 'center',
               'yanchor': 'top'},
               font=dict(
                   family='Arial',
                   size=18,
                   color='#7f7f7f'))
    fig.show()