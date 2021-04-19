# Program to
numbers = {"0":"Zero", "1":"One", "2":"Two", "3":"Three", "4":"Four",
"5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"}

userInput = input("Number: ")
print(numbers[1])
length = len(userInput)
concatenator = ''
iterator=0

while length>0:
    var=userInput[iterator]
    concatenator += numbers.get(var) + " "
    length-=1
    iterator+=1
print(concatenator)

# Priyal's code

# phone=763278
# number={
#         "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": "zero"
# }
# words= " "

# while(phone>0):
#         a= str(phone%10)
        
#         b= number[a]
#         words+= b + " "
#         phone= int(phone/10)
       
# print(words)