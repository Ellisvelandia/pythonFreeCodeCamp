# the try / except structure
# you sorround  dangerous section of code with try and except
# if the code in the try works - the excepts is skipped
# if the code in the try fails - it jump to the except section

temp = "5 degrees"
cel = 0
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print("A string don't be converted")
