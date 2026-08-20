#1
number = -5

if number < 0:
    print("Number is Negative")
elif number == 0:
    print("ZERO")
else:
    print("Number is Positive")
    

#2
number = 7

if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


#3
age = 120

if age < 13:
    print("CHILD")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")


#4
for i in range(1,11):
    print(i)

#5
numbers = [2, 4, 3, 7, 9, 1, 8]

for i in numbers:
    if i >=5:
        print("Greater Number:",i)
        break

        
#6

numbers_1 = [3, 8, 11, 14, 20, 7, 9, 12]

for i in numbers_1:
    if i % 2 == 0:
        print("Even Number:",i)


#7

numbers_3 = [10, -5, 8, -2, 15, -7, 20]

for i in numbers_3:
    if i <=0:
        continue
    print("Positive Number:",i)


#8

numbers = input("Enter numbers separated by space: ").split()
for i in numbers:
    if i == 16:
        print("Found 16!")
        break
    else:
        print("Not Found:",i)



#9
correct_password = "python123"

attempts = 3
while True:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access Granted!")
        break
    else:
        print("Incorrect Password. Try Again.")
    