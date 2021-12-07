import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Machine Learning End to End!"

app.layout = html.Div([
                       "My First Page"
                       ])
if __name__ == '__main__':
    app.run_server(debug=True)
