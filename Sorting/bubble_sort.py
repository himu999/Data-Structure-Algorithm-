def bubble_sort(lst):
    size = len(lst)

    for h in range(size-1):
        swapped = False

        for i in range(size-1-h):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    # elements = ["Himel", "Himu", '1', '2', '3']
    # elements = [1, 2, 3, 4, 5]

    bubble_sort(elements)

    print(elements)
