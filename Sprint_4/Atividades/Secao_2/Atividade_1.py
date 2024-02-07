with open('number.txt', 'r') as f:
    number = [int(line.strip()) for line in f]

    even_number = list(map(lambda n: n if n % 2 == 0 else None, number))
    even_number = list(filter(lambda n: n is not None, even_number))

    sorted_even_number = sorted(even_number, reverse=True)

    sum_of_top_5_even_number = sum(sorted_even_number[:5])

    print(sorted_even_number[:5])
    print(sum_of_top_5_even_number)
