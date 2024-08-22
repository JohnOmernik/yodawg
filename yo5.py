import plotly.graph_objects as go

# Example data
accounts = ['Account 1', 'Account 2', 'Account 3', 'Account 4']
dates = ['2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
amounts = [1000, 2000, 1500, 500]  # The size of the bubbles
y_positions = [1, 2, 1, 3]  # Manual y-axis positions for different accounts

# Convert dates to datetime objects
dates = pd.to_datetime(dates)

# Create the bubble chart
fig = go.Figure()

# Add bubbles
fig.add_trace(go.Scatter(
    x=dates,
    y=y_positions,
    mode='markers',
    marker=dict(
        size=amounts,  # Size of the bubbles
        sizemode='area',
        sizeref=2.*max(amounts)/(100.**2),  # Controls the scaling of bubble sizes
        sizemin=4,  # Minimum size of bubbles
        color=amounts,  # You can also map color to amounts or another variable
        colorscale='Viridis',  # Color scale for bubbles
        showscale=True  # Show the color scale legend
    ),
    text=accounts,  # Labels for hover
    hoverinfo='text+x+y+size'
))

# Customize the layout
fig.update_layout(
    title="Manual Bubble Chart",
    xaxis_title="Date",
    yaxis_title="Account Category",
    yaxis=dict(
        tickvals=[1, 2, 3],
        ticktext=['Category 1', 'Category 2', 'Category 3'],
    ),
    height=600,
    width=900,
)

# Show plot
fig.show()
