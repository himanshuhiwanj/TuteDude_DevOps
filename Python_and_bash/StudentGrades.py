choice = 0

Dictionary = {}
while choice != 4:
    choice = int(input("Enter your choice (1-4):\n 1.Enter New Student\n 2.Update Student Grades\n 3.Print Student Grades\n 4.Exit\n"))

    
    if choice == 1:
        name = input("Enter student name: ").strip()
        score = int(input("Enter student score: "))
        Dictionary[name] = score

    elif choice == 2:
        name = input("Enter student name to update: ").strip()
        if name in Dictionary:
            score = int(input("Enter new score: "))
            Dictionary[name] = score
        else:
            print("Student not found.") 

    elif choice == 3:
        for items in Dictionary:
            print(items + ": " + str(Dictionary[items]))


    