# Implement a problem of number of zeroes.
# Statement: Given an array of 1s and 0s which has all
# 1s first followed by all 0s? Find the number of 0s.
# Count the number of zeroes in the given array.
# Input: arr[] = {1, 1, 1, 1, 0, 0} Output: 2
# Input: arr[] = {1, 0, 0, 0, 0} Output: 4


"""
    Given array input
"""
arr1 = [1, 1, 1, 1, 0, 0, 0, 0]

'''
    Finding the given array is valid or not
'''


def loc(arr):
    global l
    for i in range(len(arr) - 1):

        if arr[i] == 1 and arr[i + 1] == 1:
            pass

        elif arr[i] == 1 and arr[i + 1] == 0:
            l = arr[i + 1]

        elif arr[i] == 0 and arr[i + 1] == 1:
            return 'Invalid input format!!'

    return l


'''
    Function parameter
'''
location_data = loc(arr1)
val = 0
if type(location_data) == int:
    val = True
    # print(f'Location of 1st 0: {arr1.index(location_data)}')
else:
    print(location_data)
    print('Cannot be Executed.')

if val:
    '''
        Using binary Search to find no of zeros
    '''

    '''
        Assigning values to low, mid and high
    '''
    low = 0
    high = len(arr1) - 1
    mid = (low + high) // 2

    while low <= high:
        mid = (low + high) // 2
        if arr1[mid] == 1:
            low = mid + 1
        else:
            high = mid - 1

    print(f'The number of zeros are : {len(arr1) - low}')
