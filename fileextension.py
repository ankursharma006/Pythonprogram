filename=input("Input the Filename : ")
extension=filename.split(".")
if extension[-1] =="py":
    print("The extension of the file is : 'Python' ")
elif extension[-1]=="jv":
    print("The extension of the file is : 'Java'")
elif extension[-1] =="txt":
    print("The extension of the file is : 'Text'")
elif extension[-1]=="cpp":
    print("The extension of the file is : 'C++")