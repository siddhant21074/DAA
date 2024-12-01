# Implement Coin Change problem.
# Statement Given an integer array of coins[ ] of
# size N representing different types of currency and an
# integer sum, The task is to find the number of ways to
# make sum by using different combinations
# from coins[].
# Note: Assume that you have an infinite supply of each
# type of coin.
# Input: sum = 4, coins[] = {1,2,3}, Output: 4
# Input: sum = 10, coins[] = {2, 5, 3, 6} Output: 5

# coins = [1, 2, 3]
# coins = [2, 5, 3, 6]


def coin_change(coins, total_sum):
    dp = [0] * (total_sum + 1)
    print(dp)

    dp[0] = 1
    print(dp)

    for coin in coins:
        for i in range(coin, total_sum + 1):
            dp[i] += dp[i - coin]
            print(dp)

    
    return dp[total_sum]



coins1 = [1, 2, 3]
total_sum1 = 4
print(coin_change(coins1, total_sum1))  

