ten_items = []
cube_items = []
for i in range(1, 11):
    ten_items.append(i)

print(ten_items)

# for j in ten_items:
#     cube_items.append(j**3)

cube_items = list(map(lambda x: x ** 3, ten_items))

print(cube_items)