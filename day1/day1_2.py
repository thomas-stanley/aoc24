list_1 = []
list_2 = []
total = 0
with open("puzzle1input.txt", "r") as f:
    for line in f:
        num_1, num_2 = line.strip().split("   ")
        list_1.append(int(num_1))
        list_2.append(int(num_2))
for value in list_1:
    to_add = value * list_2.count(value)
    total += to_add
print(total)