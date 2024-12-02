safe = 0
with open("input_2.txt", "r") as f:
    for line in f:
        numbers = line.strip().split(" ")
        numbers = [int(x) for x in numbers]
        copied_numbers = numbers.copy()
        for remove_index in range(len(copied_numbers)):
            ok = True
            numbers = [x for i, x in enumerate(copied_numbers) if i != remove_index]
            if len(set(numbers)) == len(numbers):
                sorted_numbers = sorted(numbers)
                print(numbers)
                print(sorted_numbers)
                ascending = sorted_numbers == numbers
                print(ascending)
                sorted_numbers.reverse()
                descending = sorted_numbers == numbers
                print(descending)
                print("-----")
                if ascending:
                    for i in range(1, len(numbers)):
                        difference = numbers[i] - numbers[i-1]
                        if difference > 3:
                            ok = False
                            break
                elif descending:
                    for i in range(1, len(numbers)):
                        difference = numbers[i-1] - numbers[i]
                        if difference > 3:
                            ok = False
                            break
                else:
                    ok = False
                if ok:
                    safe += 1
                    break
print(safe)

        