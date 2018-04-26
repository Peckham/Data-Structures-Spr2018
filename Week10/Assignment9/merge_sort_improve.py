import random


def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]      # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i + j] = S2[j]      # copy jth element of S2 as next item of S
            j += 1


def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return                # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]           # copy of first half
    S2 = S[mid:n]           # copy of second half
    # conquer (with recursion)
    merge_sort(S1)          # sort copy of first half
    merge_sort(S2)          # sort copy of second half
    # merge results

    # ---------------------------------------------------------------
    # Add your merge sort modification here ........................
    # To do
    if S1[-1] < S2[0]:
        for i in range(len(S1)):
            S[i] = S1[i]
        for j in range(len(S2)):
            S[j + len(S1)] = S2[j]
    elif S2[-1] < S1[0]:
        for i in range(len(S2)):
            S[i] = S2[i]
        for j in range(len(S1)):
            S[j + len(S2)] = S1[j]
    else:
        merge(S1, S2, S)  # merge sorted halves back into S
    # ---------------------------------------------------------------


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    merge_sort(array)
    print("After sorting:")
    print(array)


main()
