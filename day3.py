course = "python for beginners"
print(len(course))
print(course.lower())

print(course.find("O"))
print(course.replace("python", "C++"))

y = 10
y -= 3
print(y)

x = 10 + 3 * 2
print(x)

# order of operation 
# exponentiation then multiplication and then addition

import math

print(math.floor(2.9))

weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")


i = 1    
while i <= 5:
    print("*" * i)
    i += 1
print("Done")

secret_number = 9
number_of_gusses = 0
maximum_limit = 3
while number_of_gusses < maximum_limit:
    guess = int(input("Guess"))
    number_of_gusses += 1
    if guess == secret_number:
        print("You Win!")
        break
else:
    print("you are out of moves")