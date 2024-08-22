import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Data setup
trans = [
    {"src": "start", "dst": "Acct1", "amt": 50.00, "date": '2024-01-01'}, 
    {"src": "start", "dst": "Acct2", "amt": 0.00, "date": '2024-01-01'},  
    {"src": "start", "dst": "Acct3", "amt": 50.00, "date": '2024-01-01'}, 
    {"src": "start", "dst": "Acct4", "amt": 0.00, "date": '2024-01-01'},
    {"src": "start", "dst": "Acct5", "amt": 100.00, "date": '2024-01-01'},
     
    {"src": "Acct1", "dst": "Acct2", "amt": 25.00, "date": '2024-01-02'},
    {"src": "Acct1", "dst": "Acct3", "amt": 25.00, "date": '2024-01-02'},

    {"src": "Acct3", "dst": "Acct4", "amt": 75.00, "date": '2024-01-03'},

    {"src": "Acct2", "dst": "Acct4", "amt": 25.00, "date": '2024-01-04'},

    {"src": "Acct5", "dst": "Acct4", "amt": 100.00, "date": '2024-01-05'}
]

# Convert to DataFrame and ensure dates are datetime objects
trans_df = pd.DataFrame(trans)
trans_df['date'] = pd.to_datetime(trans_df['date'])

# Calculate account totals
accounts = trans_df['dst'].unique()
totals = {account: 0 for account in accounts}

# DataFrame to store bubbles data
bubbles = []

# Process each transaction
for _, row in trans_df.iterrows():
    if row['src'] != 'start':
        totals[row['src']] -= row['amt']
    totals[row['dst']] += row['amt']
    
    # Add bubble for destination account total
    bubbles.append({
        'date': row['date'],
        'account': row['dst'],
        'amount': totals[row['dst']],
        'type': 'total'
    })
    
    if row['src'] != 'start':
        # Add bubbles for transfers
        for alpha in np.linspace(0.1, 0.9, num=5):  # create intermediate points between src and dst
            bubbles.append({
                'date': row['date'],
                'account': row['dst'],  # place between accounts
                'amount': row['amt'] * (1 - alpha),  # scale amount by distance
                'type': 'transfer'
            })

# Create a DataFrame from the bubble data
bubble_df = pd.DataFrame(bubbles)

# Scaling factors
max_total = bubble_df[bubble_df['type'] == 'total']['amount'].max()
max_transfer = bubble_df[bubble_df['type'] == 'transfer']['amount'].max()

# Create the bubble chart
fig = go.Figure()

# Add total account bubbles
fig.add_trace(go.Scatter(
    x=bubble_df[bubble_df['type'] == 'total']['date'],
    y=bubble_df[bubble_df['type'] == 'total']['account'],
    mode='markers',
    marker=dict(
        size=bubble_df[bubble_df['type'] == 'total']['amount'] / max_total * 100,  # scale size
        sizemode='area',
        color='blue',
        opacity=0.7
    ),
    text=bubble_df[bubble_df['type'] == 'total']['amount'],
    hoverinfo='text+x+y'
))

# Add transfer bubbles
fig.add_trace(go.Scatter(
    x=bubble_df[bubble_df['type'] == 'transfer']['date'],
    y=bubble_df[bubble_df['type'] == 'transfer']['account'],
    mode='markers',
    marker=dict(
        size=bubble_df[bubble_df['type'] == 'transfer']['amount'] / max_transfer * 50,  # scale size smaller
        sizemode='area',
        color='red',
        opacity=0.6
    ),
    text=bubble_df[bubble_df['type'] == 'transfer']['amount'],
    hoverinfo='text+x+y'
))

# Customize layout
fig.update_layout(
    title="Account Totals and Transfers Over Time",
    xaxis_title="Date",
    yaxis_title="Account",
    yaxis=dict(
        tickvals=list(range(len(accounts))),
        ticktext=accounts
    ),
    height=600,
    width=900,
)

# Show plot
fig.show()
