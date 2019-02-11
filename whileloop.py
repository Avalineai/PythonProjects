num1= [8, 19, 148, 4]
num2= [9, 1, 33, 83]
list3 = []
for i in num1:
    for j in num2:
        mult = i*j
        list3.append(i*j)
        
print(list3)


num4= [8, 19, 148, 4]
num5= [9, 1, 33, 83]
mult2 = []
for i in num4:
    for j in num5:
        mult2.append(i*j)
        
print(mult2)


numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed inccorrectly!")
