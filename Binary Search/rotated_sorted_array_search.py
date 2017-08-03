# Rotated Sorted Array Search
# https://www.interviewbit.com/problems/rotated-sorted-array-search/

def find_pivot(lst, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    mid = (low + high) / 2
    if mid < high and lst[mid] > lst[mid + 1]:
        return mid
    if mid > low and lst[mid] < lst[mid - 1]:
        return mid - 1
    if lst[low] >= lst[mid]:
        return find_pivot(lst, low, mid-1)
    return find_pivot(lst, mid + 1, high)


def binary_search(lst, key, low, high):
    if high < low:
        return -1
    mid = (low + high) / 2
    if key == lst[mid]:
        return mid
    if key > lst[mid]:
        return binary_search(lst, key, mid + 1, high)
    return binary_search(lst, key, low, mid - 1)


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pivot = find_pivot(A, 0, len(A) - 1)
        if pivot == -1:
            return binary_search(A, B, 0, len(A) - 1)
        
        if A[pivot] == B:
            return pivot
        if A[0] < B:
            return binary_search(A, B, 0, pivot - 1)
        return binary_search(A, B, pivot + 1, len(A) - 1)
