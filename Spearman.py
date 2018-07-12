# Calculate Spearman's rank correlation coefficient

import scipy
import numpy as np

a = np.random.randn(100)
b = np.random.randn(100)

# Number of values
N = len(a)

# Rank lists of a and b
a_rank = scipy.stats.rankdata(a)
b_rank = scipy.stats.rankdata(b)

s = 0

for k,v in zip(a_rank,b_rank):
    s += (k - v) ** 2

ρ = 1 - ((6 * s) / (N * (N ** 2 - 1)))

print("The Spearman's rank correlation coefficient is", str(ρ) + ".")

# Standard error of Spearman's coefficient

σ = .6325 / (np.sqrt(N - 1))

print("The standard error of the coefficient is", str(σ) + ".")