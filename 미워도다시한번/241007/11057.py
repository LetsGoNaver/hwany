n = int(input())
dp = [[1] * 10 for _ in range(n+1)]

for i in range(2, n+1):
  for j in range(10):
    dp[i][j] = sum(dp[i-1][j:])

print(sum(dp[n]) % 10007)
