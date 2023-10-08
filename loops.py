# Repeated steps

# "Loops have iteration variables that change each time through a loop .
# Often these iteration variables go through a sequence of number."

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff")
print(n)

# An infinite loop
# while n > 0:
#     print('Lather')  #True
#     print('Rinse') #True
#     print('Dry off') #True

# what wrong with this loop , always is True

# Breaking Out of a loop
#
# "The break statement ends the current loop and jumps to the statement immediately followings the loop
# its like a loop test that can happen anywhere in the body of the loop"

while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!!!")

# Finishing an iteration with continue

# "the continue statement ends the current iteration and jumps
# to the top of the loop and starts the next iteration"

while True:
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!!")
