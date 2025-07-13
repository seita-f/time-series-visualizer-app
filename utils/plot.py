# import plotly.express as px
import plotly.graph_objects as go

def plot_time_series(df, columns, file_name):
    fig = go.Figure()
    for col in columns:
        fig.add_trace(go.Scatter(y=df[col], name=col, mode='lines'))
    fig.update_layout(title=file_name, xaxis_title="Index", yaxis_title="Value")
    return fig