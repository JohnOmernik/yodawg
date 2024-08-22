import plotly.graph_objects as go
import pandas as pd

# Example data
transactions = [
    {'source': 'Account 1', 'destination': 'Account 2', 'amount': 10, 'date': '2024-01-02'},
    {'source': 'Account 2', 'destination': 'Account 3', 'amount': 20, 'date': '2024-01-03'},
    {'source': 'Account 3', 'destination': 'Account 4', 'amount': 15, 'date': '2024-01-04'},
    {'source': 'Account 1', 'destination': 'Account 3', 'amount': 5, 'date': '2024-01-05'},
    # Add more transactions as needed
]

# Convert string dates to datetime objects
for tx in transactions:
    tx['date'] = pd.to_datetime(tx['date'])

# Prepare the data
accounts = list({tx['source'] for tx in transactions}.union({tx['destination'] for tx in transactions}))
account_indices = {account: i for i, account in enumerate(accounts)}

# Group transactions by date
df = pd.DataFrame(transactions)
df_grouped = df.groupby('date')

# Create frames for the animation
frames = []
for date, group in df_grouped:
    source_indices = [account_indices[tx['source']] for _, tx in group.iterrows()]
    destination_indices = [account_indices[tx['destination']] for _, tx in group.iterrows()]
    amounts = group['amount'].tolist()

    frames.append(go.Frame(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=accounts
        ),
        link=dict(
            source=source_indices,
            target=destination_indices,
            value=amounts
        )
    )], name=str(date.date())))

# Create initial Sankey diagram
fig = go.Figure(
    data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=accounts
        ),
        link=dict(
            source=[],
            target=[],
            value=[]
        )
    )],
    layout=go.Layout(
        title_text="Money Flow Between Accounts Over Time",
        font_size=10,
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, dict(frame=dict(duration=1000, redraw=True), fromcurrent=True)])]
        )]
    ),
    frames=frames
)

# Update the initial data with the first frame
fig.update(data=frames[0].data)

# Show plot
fig.show()
