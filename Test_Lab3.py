import Lab3

print("Test_Lab3")


def test_req01():
    result = []
    order = Lab3.SORT_DESCENDING
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    test_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10]
    result = Lab3.bubble_sort(input_arr, order)
    result.append(10)

    assert (result == test_arr)


def test_req02():
    result = []
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]
    result = Lab3.bubble_sort(input_arr, 2)

    assert (result == 1)


def test_req03():
    result = []
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = Lab3.bubble_sort(input_arr, 2)

    assert (result == 2)


def test_req04():
    result = []
    input_arr = []
    result = Lab3.bubble_sort(input_arr, 2)

    assert (result == 0)


def test_req05():
    result = []
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0.1]
    result = Lab3.bubble_sort(input_arr, 2)

    assert (result == 3)

