list_1 = []
list_2 = []
total = 0
with open("puzzle1input.txt", "r") as f:
    for line in f:
        num_1, num_2 = line.strip().split("   ")
        list_1.append(int(num_1))
        list_2.append(int(num_2))
list_1.sort()
list_2.sort()
for i in range(len(list_1)):
    total += abs(list_1[i] - list_2[i])
print(total)