def bubble_sort(lst, text):

    z = len(lst)

    for h in range(z-1):
        swapped = False

        for i in range(z-1-h):

            if lst[i][text] > lst[i+1][text]:
                temp = lst[i][text]
                lst[i][text] = lst[i+1][text]
                lst[i+1][text] = temp
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubble_sort(elements, "transaction_amount")

    print(elements)
