import random
def binary_search_rec(x, sorted_list, low, high):
    # this function uses binary search to determine whether an ordered array
    # contains a specified value.
    # return True if value x is in the list
    # return False if value x is not in the list
    # TO DO
    mid = sorted_list[high - low]

    if(low > high): return False
    else:
        mid = (low + high) // 2
        if sorted_list[mid] == x:
            return True
        elif sorted_list[mid] > x:
            return binary_search_rec(x, sorted_list, low, mid - 1)
        else:
            return binary_search_rec(x, sorted_list, mid + 1, high)


def binary_search_iter(x, sorted_list, low, high):
    # TO DO
    # return True if value x is in the list
    # return False if value x is not in the list
    while(low < high):
        mid = (low + high)  // 2
        if sorted_list[mid] == x: return True
        elif sorted_list[mid] < x: low = mid + 1
        else: high = mid - 1
    return False


def main():
    sorted_list = []
    for i in range(100):
        sorted_list.append(random.randint(0, 100))
    sorted_list.sort()

    print("Testing recursive binary search ...")
    for i in range(5):
        value = random.randint(0, 100)
        answer = binary_search_rec(value, sorted_list, 0, len(sorted_list) - 1)
        if (answer == True):
            print("List contains value", value)
        else:
            print("List does not contain value", value)

    print("Testing iterative binary search ...")
    for i in range(5):
        value = random.randint(0, 100)
        answer = binary_search_iter(value, sorted_list, 0, len(sorted_list) - 1)
        if (answer == True):
            print("List contains value", value)
        else:
            print("List does not contain value", value)

main()
