import random

comparisons = 0
swaps = 0


def comb_sort(array):
    ''' Comb sort uses gap > 1, where bubble sort fixes gap size = 1.
        Start with gap size = len(array) // 1.3,
        then keep shrinking by 1.3 until gap size reaches 1.

        Once gap size 1 is reached, continue using gap size 1 until the list is completely sorted.

        @array: the python list being sorted

        Make sure to calculate total number of swaps / comparisons!
    '''
    global comparisons
    global swaps

    gap = int(len(array) // 1.3)
    while gap > 1:
        for i in range(len(array)):
            try:
                comparisons += 1
                if array[i + gap] < len(array):
                    swaps += 1
                    array[i], array[i + gap] = array[i + gap], array[i]
            except IndexError:
                break
        gap = int(gap // 1.3)

    print("comparisons:", comparisons, "swaps:", swaps)

    for i in range(len(array)):
        for j in range(i):
            comparisons += 1
            if array[i] < array[j]:
                swaps += 1
                array[i], array[j] = array[j], array[i]


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    comb_sort(array)
    print("After sorting:")
    print(array)
    print("comparisons:", comparisons, "swaps:", swaps)


main()
