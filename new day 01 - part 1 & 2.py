with open("2019 day1.txt", 'r') as file:
    data = [int(x) for x in file.read().splitlines()]
    print(sum(x // 3 - 2 for x in data))
    total = 0
    for x in data:
        current = max(x // 3 - 2, 0)
        while current:
            total += current
            current = max(current // 3 - 2, 0)
    print(total)
