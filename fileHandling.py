with open("testFile.txt","r") as file:
    content = file.read()
    print(content)

with open("testFile.txt","w") as file:
    file.write("New Text written sucessfully. Thankyou!")
    
with open("testFile.txt","a") as file:
    file.write("This text is appended")

with open("testFile.txt","r") as file:
    content = file.read()
    print(content)

with open("testFileW.txt","w+") as file:
    file.write("YOu have successfully used w+ mode in you file")
    file.seek(0)
    content = file.read()
    print(content)