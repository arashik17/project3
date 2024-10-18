import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load datasets
austin_intakes = pd.read_csv('Austin Animal Center Intakes.csv')
austin_outcomes = pd.read_csv('Austin Animal Center Outcomes.csv')

# Merge Intakes and Outcomes on 'Animal ID'
df = pd.merge(austin_intakes, austin_outcomes, on='Animal ID')

# Data cleaning and feature engineering (adapted from 'austin-animal-shelter-eda.py')
df['Intake Date'] = pd.to_datetime(df['DateTime_x'])
df['Outcome Date'] = pd.to_datetime(df['DateTime_y'])
df['Stay_Duration'] = df['Outcome Date'] - df['Intake Date']
df['Intake Year'] = df['Intake Date'].dt.year
df['Outcome Year'] = df['Outcome Date'].dt.year

# Filter data only for adoptions and group by year for optimization
adoption_df = df[df['Outcome Type'] == 'Adoption'].groupby('Outcome Year').size().reset_index(name='Adoptions')

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Austin Animal Shelter Dashboard"),

    # Dropdown for selecting which graph to show
    html.Label("Select Graph:"),
    dcc.Dropdown(
        id='graph-selector',
        options=[
            {'label': 'Scatter Plot: Intake Condition by Year', 'value': 'scatter'},
            {'label': 'Bar Chart: Adoptions by Year', 'value': 'bar'},
            {'label': 'Pie Chart: Animal Outcomes in 2020', 'value': 'pie'},
            {'label': 'Stay Duration for Dogs', 'value': 'dog-duration'}
        ],
        value='scatter'  # Default selection
    ),

    # Graph placeholder for interactive updates
    dcc.Graph(id='main-graph'),

    html.H3("Summary"),
    html.P("This dashboard provides insights into animal intakes and outcomes in Austin Animal Shelter."),
    
    html.Div([
        html.H4("Student Name: MD ASHIKUZZAMAN"),
        html.H4("Student ID: 1231400017")
    ])
])

# Callback to update the graph based on dropdown selection
@app.callback(
    dash.dependencies.Output('main-graph', 'figure'),
    [dash.dependencies.Input('graph-selector', 'value')]
)
def update_graph(selected_graph):
    if selected_graph == 'scatter':
        # Scatter plot of intake condition by year
        scatter_fig = px.scatter(df, x='Intake Year', y='Intake Condition', color='Animal Type_x',
                                 title="Intake Condition by Year")
        return scatter_fig

    elif selected_graph == 'bar':
        # Bar chart of adoptions by year (optimized)
        bar_fig = px.bar(adoption_df, x='Outcome Year', y='Adoptions',
                         title="Adoptions by Year", labels={'Outcome Year': 'Year', 'Adoptions': 'Number of Adoptions'},
                         hover_data={'Adoptions': True}, color_discrete_sequence=['#636EFA'])
        return bar_fig

    elif selected_graph == 'pie':
        # Pie chart showing outcomes in 2020
        pie_fig = px.pie(df[df['Outcome Year'] == 2020], names='Outcome Type',
                         title="Animal Outcomes in 2020")
        return pie_fig

    elif selected_graph == 'dog-duration':
        # Bar chart showing stay duration for dogs
        Dog = df[df['Animal Type_x'] == 'Dog'].copy()
        Dog['Stay_Duration'] = Dog['Outcome Date'] - Dog['Intake Date']
        dog_duration_fig = px.bar(Dog, x='Intake Year', y='Stay_Duration',
                                  title="Stay Duration for Dogs", color='Breed')
        return dog_duration_fig

# Expose the Flask server for deployment
server = app.server

# Run the app locally for development
if __name__ == "__main__":
    app.run_server(debug=True)
