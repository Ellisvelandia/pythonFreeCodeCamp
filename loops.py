# # Repeated steps

# # "Loops have iteration variables that change each time through a loop .
# # Often these iteration variables go through a sequence of number."

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print("Blastoff")
# print(n)

# # An infinite loop
# # while n > 0:
# #     print('Lather')  #True
# #     print('Rinse') #True
# #     print('Dry off') #True

# # what wrong with this loop , always is True

# # Breaking Out of a loop
# #
# # "The break statement ends the current loop and jumps to the statement immediately followings the loop
# # its like a loop test that can happen anywhere in the body of the loop"

# while True:
#     line = input("> ")
#     if line == "done":
#         break
#     print(line)
# print("Done!!!")

# # Finishing an iteration with continue

# # "the continue statement ends the current iteration and jumps
# # to the top of the loop and starts the next iteration"

# while True:
#     if line[0] == "#":
#         continue
#     if line == "done":
#         break
#     print(line)
# print("Done!!")

# Exercises
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1

# Define loops
# "quite often we have a lsit of items of the lines in a file effectively a finite set of things"
# "we can write a loop to run once for each of items in a set using the python for construc"
# "These loops are called definite loops because they execute an exact nuber of times"
# "we say that define loops iterate through the members of a set"

# A simple definite loop

for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!!!")

# Definite loop with strings

friends = ["Ellis", "Glen", "Sally"]
for friend in friends:
    print("Happy new year:", friend)
print("Done!")

# Looking at in

# "The iteration variable 'Iterates' through the sequence(ordered set)"
# "The block (body) of code is executed once for each value in the sequence"
# "the iteration variable moves through all of the values in the sequence"

# Making smart loops
