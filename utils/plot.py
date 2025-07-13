import plotly.express as px

def plot_time_series(df, column):
    fig = px.line(df, y=column, title=f"Time Series - {column}")
    return fig
