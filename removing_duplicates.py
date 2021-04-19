numbers = [2,2,4,6,3,4,6,1]
print(numbers.count(6))

for num in numbers:
    while numbers.count(num)>1:
        numbers.remove(num)
print(numbers)

