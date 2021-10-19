'''

Problem:    find a number in an array binary search.
Input:      sorted array of numbers and searched number.
Output:     index of the array containing the searched number or None if the number is not found.

'''


def binary_search(arr, searched_number):
    start = 0
    end = len(arr) - 1

    while end > start:
        mid = (start + end) // 2

        if arr[mid] == searched_number:
            return mid
        elif searched_number > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return None