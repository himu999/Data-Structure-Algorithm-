def merge_two_sorted_array(a, b):

    c = []

    len_a = len(a)
    len_b = len(b)

    i = j = 0
    while i < len_a and j < len_b:

        if a[i] <= b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1

    while i < len_a:
        c.append(a[i])
        i = i + 1

    while j < len_b:
        c.append(a[j])
        j = j + 1

    return c


if __name__ == "__main__":

    a = [5, 8, 12, 56]
    b = [7, 9, 45, 51]

    print(merge_two_sorted_array(a, b))