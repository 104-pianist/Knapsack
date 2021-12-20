m = 4 # 物品数量
n = 10 # 背包容量
w = [4, 7, 5, 3] # 物品重量
p = [40, 42, 25, 12] # 物品价值

# 创建一个(n+1)行(w+1)列的二维列表
dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(m):
    for j in range(n+1):
        if j < w[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]] + p[i])
print(dp[m][n])