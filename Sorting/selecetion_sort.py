def merge_sort(lst):

    for i in range(len(lst)):
        min_index = i

        for j in range(min_index + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        lst[min_index], lst[i] = lst[i], lst[min_index]

    return lst


if __name__ == "__main__":
    a = [10, 5, -9, 45, 0, 753, -963]
    print(merge_sort(a))
