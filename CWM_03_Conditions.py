
# if statements
hungry = True

if hungry:
    print("Eat food")

# if else statements
rain = False

if rain:
    print("Take Umbrella")
else:
    print("No need of Umbrella")

# if elif else statements
light = "red"

if light == "red":
    print("STOP")
elif light == "Yellow":
    print("wait")
else:
    print("GO")


#for loop
for i in range(5):
    print("clap")

# while loop
# hungry =True

# while hungry:
#     print("Eat food")  #it will keep doing as long as condition is True


# while loop with break and continue
count =1

while count <=5:
    print(count)
    count = count +2

#break
print()

for i in range(10):
    if i == 5:
        break

    print(i)

#continue
print()

for i in range(10):
    if i == 5:
        continue
    print(i)




