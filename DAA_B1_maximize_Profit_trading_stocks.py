# Statement: Given an array arr[] of N positive integers
# which denotes the cost of selling and buying a stock on
# each of the N days. The task is to find the maximum
# profit that can be earned by buying a stock on or selling
# all previously bought stocks on a particular day.
# Input: arr[] = {2, 3, 5} Output: 5
# Input: arr[] = {8, 5, 1} Output: 0

arr = [1, 3, 4, 7, 5, 6]
# arr = [2, 3, 5]
# arr = [8, 5, 1]

num = [n for n in arr if n > arr[0]]
if num:
    print(max(num))
else:
    print(0)
