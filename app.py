import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load datasets
austin_intakes = pd.read_csv('Austin Animal Center Intakes.csv')
austin_outcomes = pd.read_csv('Austin Animal Center Outcomes.csv')

# Merge Intakes and Outcomes on 'Animal ID'
df = pd.merge(austin_intakes, austin_outcomes, on='Animal ID')

# Data cleaning and feature engineering
df['Intake Date'] = pd.to_datetime(df['DateTime_x'])  # Use 'DateTime_x' for Intake Date
df['Outcome Date'] = pd.to_datetime(df['DateTime_y'])  # Use 'DateTime_y' for Outcome Date
df['Intake Year'] = df['Intake Date'].dt.year
df['Outcome Year'] = df['Outcome Date'].dt.year

# Initialize Dash app
app = dash.Dash(__name__)

# Graph 1: Scatter plot of intake condition by year
scatter_fig = px.scatter(df, x='Intake Year', y='Intake Condition', color='Animal Type_x', title="Intake Condition by Year")

# Graph 2: Bar chart of adoptions by year
bar_fig = px.bar(df[df['Outcome Type'] == 'Adoption'], x='Outcome Year', y='Animal ID', title="Adoptions by Year", color='Animal Type_y')

# Graph 3: Pie chart showing outcomes in 2020
pie_fig = px.pie(df[df['Outcome Year'] == 2020], names='Outcome Type', title="Animal Outcomes in 2020")

# Define the layout of the app
app.layout = html.Div([
    html.H1("Austin Animal Shelter Dashboard"),

    html.H2("Intake Condition by Year"),
    dcc.Graph(
        id='intake-condition-scatter',
        figure=scatter_fig
    ),

    html.H2("Adoptions by Year"),
    dcc.Graph(
        id='adoptions-bar',
        figure=bar_fig
    ),

    html.H2("Animal Outcomes in 2020"),
    dcc.Graph(
        id='outcomes-pie',
        figure=pie_fig
    ),

    html.H3("Summary"),
    html.P("This dashboard provides insights into animal intakes and outcomes in Austin Animal Shelter."),
    
    html.Div([
        html.H4("Student Name: MD ASHIKUZZAMAN"),
        html.H4("Student ID: 1231400017")
    ])
])

# Expose the Flask server for deployment
server = app.server

# Run the app locally for development
if __name__ == "__main__":
    app.run_server(debug=True)
