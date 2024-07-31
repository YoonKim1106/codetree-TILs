def count_even_numbers():
    even_count = 0

    for _ in range(5):
        number = int(input().strip())
        if number % 2 == 0:
            even_count += 1
    
    print(even_count)

count_even_numbers()