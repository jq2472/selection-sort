"""
Jolin Qiu

1. Insertion_sort performs better than selection_sort when the test case
is an already sorted, or substantially partially sorted array / anything
where the elements in the list are not in complete reverse order.

2. The time complexity of selection_sort is always quadratic / O(n^2)
no matter what. However, O(n^2) is only the worst-case time complexity
for insertion_sort. So insertion_sort will typically have lesser than or
at worst, equal-to time complexities than O(n^2).
"""


def read_file():
    """ reads a file consisting of integer values, one per line,
    and returns a list.
    """
    filename = input("Input file name: ")
    with open(filename) as f:
        file_list = []
        for line in f:
            file_list.append(int(line.strip()))
    print("Unsorted: " + str(file_list))
    return file_list


def selection_sort(file_list):
    """ sorts the numbers from the file list in ascending order.
    """
    for mark in range(0, len(file_list)):
        swap(file_list, mark, find_min_from(file_list, mark))
    return file_list


def find_min_from(file_list, mark):
    """ returns the index of the smallest value in the list
    for a specified range.
    :param file_list: list of numbers being sorted
    :param mark: the start index to sort from
    """
    min_index = mark
    for i in range(mark, len(file_list)):
        if file_list[i] < file_list[min_index]:  # only *want to* "update" index when it's less than
            min_index = i
    return min_index  # 'i' would only return the last index


def swap(file_list, x, y):
    """ swap the contents of the list at position x with position y.
    :param file_list: list of numbers being sorted
    :param x: the index of one datum
    :param y: the index of the other datum
    """
    place_holder = file_list[x]
    file_list[x] = file_list[y]
    file_list[y] = place_holder


def main():
    """ prompt for an input file name: read, store, sort, and print data
     in the file.
     """
    print("sorted: " + str(selection_sort(read_file())))


main()
