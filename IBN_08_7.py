from scipy.stats import binom
p = 0.1
N = 10000
M = N + 5
w = 0
for X in range(N, M + 1):
    w += binom.pmf(X, M, p)
print(w)
