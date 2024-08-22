import plotly.graph_objects as go

# Example data
accounts = ['Account 1', 'Account 2', 'Account 3', 'Account 4']
transactions = [
    {'source': 'Account 1', 'destination': 'Account 2', 'amount': 10},
    {'source': 'Account 2', 'destination': 'Account 3', 'amount': 20},
    {'source': 'Account 3', 'destination': 'Account 4', 'amount': 15},
    {'source': 'Account 1', 'destination': 'Account 3', 'amount': 5},
    # Add more transactions as needed
]

# Mapping accounts to indices
account_indices = {account: i for i, account in enumerate(accounts)}

# Prepare data for Sankey diagram
source_indices = [account_indices[tx['source']] for tx in transactions]
destination_indices = [account_indices[tx['destination']] for tx in transactions]
amounts = [tx['amount'] for tx in transactions]

# Create Sankey diagram
fig = go.Figure(data=[go.Sankey(
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
)])

# Set plot title
fig.update_layout(title_text="Money Flow Between Accounts", font_size=10)

# Show plot
fig.show()
