import plotly.graph_objects as go
import pandas as pd

# Example data with two dates
transactions = [
    {'source': 'Account 1', 'destination': 'Account 2', 'amount': 10, 'date': '2024-01-02'},
    {'source': 'Account 2', 'destination': 'Account 3', 'amount': 20, 'date': '2024-01-02'},
    {'source': 'Account 3', 'destination': 'Account 4', 'amount': 15, 'date': '2024-01-03'},
    {'source': 'Account 1', 'destination': 'Account 3', 'amount': 5, 'date': '2024-01-03'},
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

# Initialize the main figure
fig = go.Figure()

# Add a Sankey diagram for each date
for i, (date, group) in enumerate(df_grouped):
    source_indices = [account_indices[tx['source']] for _, tx in group.iterrows()]
    destination_indices = [account_indices[tx['destination']] for _, tx in group.iterrows()]
    amounts = group['amount'].tolist()

    fig.add_trace(go.Sankey(
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
        ),
        domain=dict(
            x=[i / len(df_grouped), (i + 1) / len(df_grouped)],
            y=[0, 1]
        )
    ))

# Update layout
fig.update_layout(
    title_text="Money Flow Between Accounts Over Time",
    font_size=10,
    height=600,  # Adjust height to fit multiple Sankey diagrams
)

# Show plot
fig.show()
