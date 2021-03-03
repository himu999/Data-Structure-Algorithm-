def bubble_sort(lst):
    size = len(lst)

    for h in range(size-1):

        for i in range(size-1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    bubble_sort(elements)

    print(elements)
