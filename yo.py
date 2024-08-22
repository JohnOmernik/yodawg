import matplotlib.pyplot as plt
import numpy as np

# Example data
accounts = ['Account 1', 'Account 2', 'Account 3', 'Account 4']
times = np.arange(0, 10)
transactions = [
    {'source': 'Account 1', 'destination': 'Account 2', 'amount': 10, 'time': 1},
    {'source': 'Account 2', 'destination': 'Account 3', 'amount': 20, 'time': 2},
    {'source': 'Account 3', 'destination': 'Account 4', 'amount': 15, 'time': 3},
    {'source': 'Account 1', 'destination': 'Account 3', 'amount': 5, 'time': 4},
    # Add more transactions as needed
]

# Mapping accounts to y-axis positions
account_positions = {account: i for i, account in enumerate(accounts)}

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot swimlanes
for account, pos in account_positions.items():
    ax.hlines(y=pos, xmin=times.min(), xmax=times.max(), color='gray', linestyle='--')

# Plot transactions
for tx in transactions:
    source_pos = account_positions[tx['source']]
    dest_pos = account_positions[tx['destination']]
    ax.plot([tx['time'], tx['time']], [source_pos, dest_pos], color='blue', 
            linewidth=tx['amount']/5,  # Thickness proportional to amount
            alpha=0.7)

# Add labels
ax.set_yticks(range(len(accounts)))
ax.set_yticklabels(accounts)
ax.set_xlabel('Time')
ax.set_title('Money Flow Between Accounts')

plt.show()
