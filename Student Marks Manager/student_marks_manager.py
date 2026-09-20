print("===========Student Marks Manager===========")
choice = 0
Student_Record = []

while choice != 7:

    print("1.Add Student\n2.Show Students\n3.Search Student\n4.Update Marks\n5.Calculate Result\n6.Find Highest Marks\n7.Exit")
    choice = int(input("Enter your choice: "))

    # Add Student
    if choice == 1:

        Student_Name = input("Enter the Student name: ")
        Student_Class = input("Enter the Student class: ")
        Student_Roll_no = int(input("Enter the Student Roll Number: "))
        Student_Age = int(input("Enter the Age of the Student: "))

        Student = [Student_Name, Student_Class, Student_Roll_no, Student_Age]

        print("Enter the marks of the Student (5 Subjects)")
        marks = []
        Total_Marks = 0

        for i in range(5):
            Subject_marks = int(input(f"Enter the marks of {i+1} Subject (out of 100): "))
            Total_Marks += Subject_marks
            marks.append(Subject_marks)

        Student.append(marks)
        Student.append(Total_Marks)

        Student_Record.append(Student)

        print("Student Added Successfully!")
        print("==============================================")


    # Show Students
    elif choice == 2:

        if len(Student_Record) == 0:
            print("No Student Record Found.")

        else:
            for i in range(len(Student_Record)):

                print("Student Name:", Student_Record[i][0])
                print("Class:", Student_Record[i][1])
                print("Student Roll Number:", Student_Record[i][2])
                print("Age:", Student_Record[i][3])
                print("Marks:", Student_Record[i][4])
                print("Total Marks:", Student_Record[i][5])
                print("----------------------------------------------")


    # Search Student
    elif choice == 3:

        Student_Name = input("Enter the Student Name: ")

        for i in range(len(Student_Record)):

            if Student_Record[i][0] == Student_Name:

                print("Record Found!")
                print("Student Name:", Student_Record[i][0])
                print("Class:", Student_Record[i][1])
                print("Student Roll Number:", Student_Record[i][2])
                print("Age:", Student_Record[i][3])
                print("Marks:", Student_Record[i][4])
                print("Total Marks:", Student_Record[i][5])

                break

        else:
            print("Student Record Not Found.")

        print("==============================================")


    # Update Marks
    elif choice == 4:

        Student_Name = input("Enter the name of the Student: ")
        Student_Class = input("Enter the Class of the Student: ")
        Student_Roll_no = int(input("Enter the Roll no of student: "))

        for i in range(len(Student_Record)):

            if (Student_Name == Student_Record[i][0] and
                Student_Class == Student_Record[i][1] and
                Student_Roll_no == Student_Record[i][2]):

                print("Enter the Updated marks of all subjects of the student.")

                marks = []
                Total_Marks = 0

                for j in range(5):

                    Subject_marks = int(input(f"Enter the marks of the {j+1} subject: "))

                    marks.append(Subject_marks)
                    Total_Marks += Subject_marks

                Student_Record[i][4] = marks
                Student_Record[i][5] = Total_Marks

                print("The marks of the Student are Successfully Updated.")

                break

        else:
            print("Student Record Not Found.")

        print("================================================")


    # Calculate Result
    elif choice == 5:

        Obtain_Marks = 0

        Student_Name = input("Enter the name of the student: ")
        Student_Class = input("Enter the class of the student: ")
        Student_Roll_no = int(input("Enter the Roll no of the student: "))

        for i in range(len(Student_Record)):

            if (Student_Record[i][0] == Student_Name and
                Student_Record[i][1] == Student_Class and
                Student_Record[i][2] == Student_Roll_no):

                Obtain_Marks = Student_Record[i][5]

                break

        Percentage = (Obtain_Marks * 100) / 500

        print("Obtain Marks (out of 500):", Obtain_Marks)
        print("Percentage:", Percentage)

        if Percentage >= 33:
            print("Pass")
        else:
            print("Fail")

        print("==================================================")


    # Find Highest Marks
    elif choice == 6:

        Highest_marks = 0

        Student_Class = input("Enter the class: ")

        for i in range(len(Student_Record)):

            if Student_Record[i][1] == Student_Class:

                if Highest_marks < Student_Record[i][5]:

                    Highest_marks = Student_Record[i][5]

        print("Highest Marks:", Highest_marks)
        print("==================================================")

    # Exit
    elif choice == 7:
        break
    else:
        print("Enter Wrong choice.")
