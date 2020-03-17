"""
Find k-th number of two sorted arrays with different sizes in O(log(min(n, m)))
"""

from time import perf_counter

list_a = [1, 3, 5, 6, 9, 10, 11, 100]
list_b = [2, 4, 7, 8, 723]


# sorting takes at least O(n) time here
def find_kth_1(a: list, b: list, k: int):
    return sorted(a + b)[k - 1]


# binary search takes O(log(n)) time
# can be further optimised with non-recursive function
def find_kth_2(a: list, b: list, k: int):
    if len(a) < len(b):
        return find_kth_2(b, a, k)

    if k > len(b):
        return a[k - len(b) - 1]
    if k == 1:
        return min(a[0], b[0])
    if k == 2:
        return max(a[0], b[0])

    c = int(k / 2)
    # print(f"{k=}")
    # print(f"{c=}")
    if a[c] > b[c]:
        b = b[c:]
        return find_kth_2(a, b, k - c)
    else:
        a = a[c:]
        return find_kth_2(a, b, k - c)


start = perf_counter()
print(find_kth_1(list_a, list_b, 35))
print(perf_counter() - start)

start = perf_counter()
print(find_kth_2(list_a, list_b, 35))
print(perf_counter() - start)
