f = open("python1.txt" , "w")
strWrite = input("Enter the characters: ")
f.write(strWrite)
f.close()

f = open("python1.txt" , "r")
strRead = f.read()
print("The characters you entered are:", strRead)
f.close()