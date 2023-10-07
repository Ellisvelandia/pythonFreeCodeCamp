# a variable is a named place in the memory where a programmer can store data and later retrieve the data using the variable "name"

# programmers get to choose the names of the variables

width = 15
height = 12.0
print(height / 3)

# + Addition
# - Substaction
# * Multiplication
# / Division
# ** Power
# % Remainder

# Paranthesis
# power
# Multiplicatiion
# Addtion
# left to right

inp = input("Europe floor?")
usf = int(inp) + 1
print("US floor", usf)

# Conditionals
x = 5

if x < 1:
    print("Smaller")
elif x > 20:
    print("Bigger")
else:
    print("Blank")

# Identation
# Increase indent after an if statement or for stattement(after:)

x = 5
if x > 2:
    print("Bigger than 2")
    print("Still bigger")
print("Done with 2")

for i in range(5):
    print(i)
    if i > 2:
        print("Bigger than 2")
    print("Done with i", i)
print("All Done")

# Two way Desicions
# sometimes we want to do one thing if a logical expression is true and something else if the expression is false
# it is like a fork in the road - we must because choose one or the other path but not both

x = 4

if x == 2:
    print("Bigger")
else:
    print("Smaller")

print("All Done")
