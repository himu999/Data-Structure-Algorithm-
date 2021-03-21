def selection_sort(list):
    length = len(list)

    for i in range(length-1):
        min_index = i

        for j in range(i, length):

            if a[min_index] >= a[j]:
                min_index = j
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp

        print(list)

    return list


if __name__ == "__main__":
    a = map(int, input().split())
    a = list(a)
    print(selection_sort(a))
