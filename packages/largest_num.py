def max_finder():
    numbers = []

    try:
        while True:
            numbers.append(int(input("Enter the number: ")))
    except:
        print(numbers)


    var = numbers[0]
    for num in numbers:
        if num > var:
            var = num
    print(var)