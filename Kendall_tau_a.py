# Kendall's Tau-a (Kendall Rank Correlation Coefficient)

import scipy.stats
import numpy as np

# Replace a and b with your own data.
a = np.random.randn(100)
b = np.random.randn(100)

# a = [1, 5, 2, 7, 44, 20]
# b = [4, 6 , 1, 77, 14, 30]

# Number of values
N = len(a)

# Rank lists of a and b
a_rank = list(scipy.stats.rankdata(a))
b_rank = list(scipy.stats.rankdata(b))

# Sort a_rank from least to greatest, keeping b_rank associated with same values
# Combine a_rank and b_rank into tuples list
a_b_comb = list(zip(a_rank,b_rank))

# Sort tuples list by a_rank 
sort_a_b = sorted(a_b_comb)

# Split tuples list back into individual lists of values
a_rank, b_rank = zip(*sort_a_b)

# Number of concordant pairs
P = 0

# Number of discordant pairs
Q = 0

for idx_y, y in enumerate(b_rank):
    f = idx_y + 1
    while f < len(b_rank):
        if b_rank[f] > b_rank[idx_y]:
            P += 1
        elif b_rank[f] < b_rank[idx_y]:
            Q += 1
        f += 1

τa = (P - Q) / (Q + P)
print("Kendall's Tau-a (τ-A) for this data is", str(τa) + ". Please note that Tau-a does not account for ties in ranked data.")