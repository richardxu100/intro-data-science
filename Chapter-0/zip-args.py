list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

for x, y in zip(list1, list2):
    print(x, y)

l1, l2 = zip(*zip(list1, list2))

print(l1)
print(l2)