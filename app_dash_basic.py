import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('iris.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


app.layout = html.Div([
    html.H2('Filtering Iris Table Example'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in df['class'].unique()],
        value='LA'
    ),
    html.Div(id='display-table')

])

@app.callback(dash.dependencies.Output('display-table', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_table(value):
    if value is None:
        return generate_table(df)

    dff = df[df['class']==value]
    return generate_table(dff)
    

if __name__ == '__main__':
    app.run_server(debug=True)
