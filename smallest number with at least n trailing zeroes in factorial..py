# Implement a problem of smallest number with at
# least n trailing zeroes in factorial.
# Statement: Given a number n. The task is to find the
# smallest number whose factorial contains at least n
# trailing zeroes.
# Input : n = 1 Output : 5
# Input : n = 6 Output : 25

""" Here n is the number of zero at end i.e n trailing """


def factorial(n):
    f = 1
    for j in range(1, n + 1):
        f *= j
    return f


num = 25
result = factorial(num)

string_of_num = str(result)
num_list = [n for n in string_of_num]

ns = [i for i in num_list if i == '0']
print(ns)