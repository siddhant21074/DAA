# Statement: Given an array of 1s and 0s which has all
# 1s first followed by all 0s? Find the number of 0s.
# Count the number of zeroes in the given array.
# Input: arr[] = {1, 1, 1, 1, 0, 0} Output: 2
# Input: arr[] = {1, 0, 0, 0, 0} Output:


# arr = [1, 1, 1, 1, 0, 0]
arr = [1, 0, 0, 0, 0]
print(arr.count(0))

# print(len(arr))
# num = [n for n in arr if n == 1 and arr[n + 1] == 0]
for i in range(0, len(arr)):
    if arr[i] == 1:
        if arr[i + 1] == 0:
            print(arr[i+1])
    # else:
    #      print('Invalid input')
