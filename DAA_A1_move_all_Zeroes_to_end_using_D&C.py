#  Given an array of random numbers, Push all the zero’s
# of a given array to the end of the array. For example, if the given
# arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9,
# 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be
# same.
# Input : arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
# Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};

arr = [1, 2, 0, 4, 3, 0, 5, 0]

'''
    Without D&c 
'''

# arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]x
# num1 = [n for n in arr if n == 0]
# num = [n for n in arr if n != 0]
# sample = num + num1
# print(sample)
#

'''
    With D&c
'''

low = 0
high = len(arr)
mid = (low + high) // 2

'''
    Here we divide the arr into two parts 
'''

arr1 = [arr[n] for n in range(0, mid)]
print(f'This is arr1: {arr1}')

arr2 = [arr[n] for n in range(mid, high)]
print(f'This is arr2: {arr2}')


'''
    Using D&C for arr1 and arr2
'''

num1_with_non_zero = [n for n in arr1 if n != 0]
num1_with_zero = [n for n in arr1 if n == 0]

num2_with_non_zero = [n for n in arr2 if n != 0]
num2_with_zero = [n for n in arr2 if n == 0]

new_arr = num1_with_non_zero + num2_with_non_zero
new_arr1 = num1_with_zero + num2_with_zero

'''
    Final output
'''
result = new_arr + new_arr1
print(result)
