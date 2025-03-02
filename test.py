import copy
list1 = [[1, 2], [3, 4]]
shallow = copy.copy(list1)
deep = copy.deepcopy(list1)

list1[0][0] = 99
print(shallow[0][0])  # 99 (Affected)
print(deep[0][0])     # 1 (Unaffected)


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Create a generator
counter = count_up_to(5)

print(counter)

# Iterate using a for loop
for num in counter:
    print(num)

