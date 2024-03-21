def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


n = int(input('Enter the number of items: '))
print('Enter the values')
items = []
for i in range(n):
    items.append(int(input()))

print('Before sorting', items)
bubble_sort(items)
print('After sorting', items)
