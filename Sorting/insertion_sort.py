def insertion_sort(lst):

    for i in range(1, len(lst)):
        anchor = lst[i]

        j = i - 1

        while j >= 0 and anchor < lst[j]:

            lst[j+1] = lst[j]
            j = j - 1

        lst[j+1] = anchor


if __name__ == "__main__":

    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    insertion_sort(elements)
    print(elements)
