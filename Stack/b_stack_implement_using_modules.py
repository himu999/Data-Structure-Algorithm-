import collections

stack = collections.deque()


def push():
    if len(stack) == n:
        print('Stack is full!')
    else:
        stack.append(input('Enter the element:'))
        print(stack)


def pop():
    if not stack:
        print('Stack is empty!')
    else:
        e = stack.pop()
        print('Remove element:', e)


n = int(input('Limit of stack: '))

while True:
    print('Select the operation 1.push 2.pop 3.quit')
    choice = int(input())

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print('Enter the correct operation')
