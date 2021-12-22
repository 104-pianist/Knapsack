quantity = 4 # 物品数量
capacity = 10 # 背包容量
weight = [4, 7, 5, 3] # 物品重量
value = [40, 42, 25, 12] # 物品价值

# 创建一个(capacity+1)行(quantity+1)列的二维列表
dp = [[0] * (capacity+1) for _ in range(quantity+1)]

for i in range(quantity):
    for j in range(capacity+1):
        if j < weight[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-weight[i]] + value[i])
print(dp[quantity][capacity])