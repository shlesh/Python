def max_finder():
    numbers = []
    input("Enter the numbers: ")
    try:
        while True:
            numbers.append(int(input()))
    except:
        print(numbers)


    var = numbers[0]
    for num in numbers:
        if num > var:
            var = num
    print(var)
