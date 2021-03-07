def insertion_sort(lst):

    for i in range(len(lst)):
        temp = lst[i]

        j = i - 1

        while j >= 0 and lst[j] > temp:
            lst[j+1] = lst[j]
            j = j - 1

        lst[j+1] = temp

    return lst


if __name__ == "__main__":

    a = [12, 25, 98, -10, 4, 0, 0.2, 78]
    print(insertion_sort(a))
