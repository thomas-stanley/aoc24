total = 0
with open("input2.txt", "r") as f:
    for line in f:
        ok = True
        numbers = line.strip().split(" ")
        numbers = [int(x) for x in numbers]
        difference = numbers[1] - numbers[0]
        if difference == 0:
            continue
        elif difference < 0:
            ascending = True
        elif difference > 0:
            ascending = False
        for i in range(1, len(numbers)):
            separation = numbers[i - 1] - numbers[i]
            if separation == 0:
                ok = False
                break
            if ascending:
                if separation < -3:
                    ok = False
                    break
            else:
                if separation > 3:
                    ok = False
                    break
        if ok:
            total += 1
print(total)

        