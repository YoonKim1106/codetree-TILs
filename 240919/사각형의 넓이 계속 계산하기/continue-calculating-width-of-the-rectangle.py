while True:
    data = input().split()
    width = int(data[0])
    height = int(data[1])
    char = data[2]

    area = width * height
    print(area)

    if char == 'C':
        break