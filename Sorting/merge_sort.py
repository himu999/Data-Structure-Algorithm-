def merge_sort(lst):
    mid = len(lst) // 2

    if len(lst) <= 1:
        return lst

    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_list(left, right)


def merge_two_list(arr1, arr2):
    c = []
    len_a = len(arr1)
    len_b = len(arr2)
    i = j = 0
    while i < len_a and j < len_b:
        if arr1[i] < arr2[j]:
            c.append(arr1[i])
            i = i + 1
        else:
            c.append(arr2[j])
            j = j + 1

    while i < len_a:
        c.append(arr1[i])

        i = i + 1

    while j < len_b:
        c.append(arr2[j])
        j = j + 1

    return c


if __name__ == "__main__":
    z = [10, 3, 15, 7, 8, 23, 98, 29]
    print(merge_sort(z))
