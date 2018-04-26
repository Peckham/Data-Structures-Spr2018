import random

comparisons = 0
swaps = 0


def find_max(array, a, b):
    '''
        Finds the position of the largest element between two indices in the
        array.
        @array: the python list
        @a:     the index of first element to check
        @b:     the index of last element to check

        Add your modification to @comparisons

        return: index of the largest element
    '''
    global comparisons
    maxPos = a
    for i in range(a, b):
        comparisons += 1
        if (array[maxPos] < array[i]):
            maxPos = i
    return maxPos


def reverse(array, a, b):
    '''
        Reverses the elements between two indices in the array.
        @array: the python list
        @a:     the index of first element to reverse
        @b:     the index of "one past" last element to reverse

        Add your modification to @swaps
    '''
    global swaps
    l = a
    r = b
    while (l < r):
        swaps += 1
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1


def summer_sort(array):
    '''
        Sorts the array using find_max(array, a, b) and reverse(array, a, b)
        functions.
        @array: the python list
        1. Find the max of the entire list.
        2. Reverse from the max to the end, placing max at the end.
        3. Decrement position
        4. Repeat 1 - 3 until position is 0.
    '''
    pos = len(array) - 1
    print("Max, ", find_max(array, 0, len(array)))  # This doesn't seem to work
    while pos > 0:
        reverse(array, find_max(array, 0, pos), pos)
        pos -= 1


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))
    # array = [1, 2, 3, 4, 5]
    print("Before sorting:")
    print(array)
    summer_sort(array)
    print("After sorting:")
    print(array)
    print("comparisons:", comparisons, "swaps:", swaps)


main()
