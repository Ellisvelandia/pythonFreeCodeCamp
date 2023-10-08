# A function is some store code that we use , A function takes some input and produces an output.
# When you put an integer and floating point in a expression , the integer is implicity converted to a floar
# you can control this with the bult-in functions int() and float()
# You can also use int() and float() to convert between strings and integers
# Y ou will get an error if the string does not contain numeric characters


#####
# overall it ndicates the start of a function, and the following indented section of code is to be stored for later.
#####

# Building oir Own Functions
# We create a new function using the def keyword followed by optional parameters in parentheses
"we idented the body of the function"
"this defines the function but does not execute the body of the fucntion"


def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print("I sleep all night and i wortk all day")


print(print_lyrics())

# Arguments

# "An argument is a value we pass into the function as its input when we call the function"
# "we use arguments so we can direct the function to do different kinds of works we call it at diffetent times"
# "we put the arguments in the parentheses after the name of the function"

big = max("Hello world")  # argument

# Parameters

# "A paramerer  is a variable which we use in the function definition. it is a 'handle'
# that allows the code in the function to access the arguments for a particular function invocation"


def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")


greet("en")  # parameter
greet("es")  # parameter
greet("fr")  # parameter

# Return values
# "often a function will takes its argumnets , do some computation , and return a value
# to be used as the value of the function call in the calling expression.
# The return Keyword is used for this"


def greet():
    return "Hello"


print(greet(), "Ellis")
print(greet(), "Crisanto")

# "we can define more than one parsmeters in the function definition
# we simply add more arguments when we call the function
# we match the number ad order or argument and paramenters
# "


def addtwo(a, b):
    added = a + b
    return added


x = addtwo(3, 5)
print(x)


# - Exercise

# What will the following Python program print out?:


def fred():
    print("Zap")


def jane():
    print("ABC")


jane()
fred()
jane()
