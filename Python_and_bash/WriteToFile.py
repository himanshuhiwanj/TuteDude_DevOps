with open("SampleFile",'w') as file:
    text = input("Enter text to input in file : ")
    file.write(text)

    print("File Created")