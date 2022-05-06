print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):
    # Copy input list to result list
    arr_result = arr.copy()
    integer_checker = all([isinstance(item, int) for item in arr_result])
    # Get number of elements in the list
    n = len(arr_result)
    if integer_checker:
        if n == 10:
            for i in range(n - 1):
                # range(n) also work but outer loop will
                # repeat one time more than needed.

                # Last i elements are already in place
                for j in range(0, n - i - 1):

                    if sorting_order == SORT_ASCENDING:
                        if arr_result[j] > arr_result[j + 1]:
                            arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                    elif sorting_order == SORT_DESCENDING:
                        if arr_result[j] < arr_result[j + 1]:
                            arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                    else:
                        # Return an empty array
                        arr_result = []

        elif n > 10:
            arr_result = 1

        elif 0 < n < 10:
            arr_result = 2

        elif n == 0:
            arr_result = 0
    elif not integer_checker:
        arr_result = 3

    return arr_result


def main():
    # Driver code to test above
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0.9]

    print("Sorted array in ascending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)


if __name__ == "__main__":
    main()
