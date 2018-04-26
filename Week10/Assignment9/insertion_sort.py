import random

comparisons = 0
swaps = 0


def insertion_sort(array):
    ''' Insertion sort iterates, consuming one input element each repetition,
        and growing a sorted output list.
        @array: the python list being sorted

        Make sure to calculate total number of swaps / comparisons!
    '''
    global comparisons
    global swaps

    for i in range(1, len(array)):
        currentVal = array[i]
        pos = i
        while pos > 0 and currentVal < array[pos - 1]:
            comparisons += 1
            array[pos] = array[pos - 1]
            pos -= 1
        swaps += 1
        array[pos] = currentVal


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    insertion_sort(array)
    print("After sorting:")
    print(array)
    print("comparisons:", comparisons, "swaps:", swaps)


main()
