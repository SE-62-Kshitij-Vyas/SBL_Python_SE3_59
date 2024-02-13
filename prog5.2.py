with open("Python.txt", "a+") as f:
    str = input("Enter: ")
    while str != "@":
        f.write(str)
        str = input("Enter again: ")

f = open("Python.txt", "r")
strRead = f.read()
print("This is ",strRead)
f.close()