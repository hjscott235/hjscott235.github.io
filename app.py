# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import datetime
import process
import statsmodels.api as sm
import plotly.graph_objects as go
import dash_daq as daq

process

app = dash.Dash(__name__)

## build graphs
trend = px.scatter(process.grouped, x="day", y="objects detected", trendline='lowess')
count = go.Figure()
count.add_trace(go.Indicator(
    mode = "number+delta",
    value = 23,
    title = {"text": "Latest Counts"},
    delta = {'reference': 170, 'relative': True},
    domain = {'row': 0, 'column': 0}))
count.update_layout(paper_bgcolor="#252629")
count.show()
latest = px.bar(process.latest, x="month", y="objects detected")
latest.update_layout(paper_bgcolor="#252629")

## build page
app.layout = html.Div([
    html.Div(
        className="header",
        children=[
            html.Div('Supply Chain Manager')
        ]),
    html.Div(
        className="subheader",
        children=[
            html.Div('Orbital Insight for Triumph Group International')
        ]),
    html.Div(
        className="parent",
        children=[
            html.Div(
                className="summary",
                children=[
                    dcc.Graph(
                        id='count',
                        figure=count)
                    ]),
            html.Div(
                className="summary",
                children=[
                        dcc.Graph(
                            id='latest-data',
                            figure=latest)
                ]),
            html.Div(
                className="summary",
                children=[
                    html.Div(
                        <img src "images/status-yellow.png">
                        )
                ]),
            html.Div(
                className="summary",
                children=[
                    html.Div('test')
                ])
        ]),
    dcc.Graph(
        id='objects-trend',
        figure=trend
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)