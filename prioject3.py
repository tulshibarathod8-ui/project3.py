
all_students =[]

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("\nEnter student details:")

            student_id = int(input("Student ID: "))

            if student_id in [student["student_info"][0] for student in all_students]:
                print("Student ID already exists!")

            else:
                student_name = input("Name: ")
                student_age = int(input("Age: "))
                student_grade = input("Grade: ")
                student_info = (
                    student_id,
                    input("Date of Birth (YYYY-MM-DD): ")
                )
                
                all_students.append({
                                "student_info" : student_info,
                                "student_name" : student_name,
                                "student_age" : student_age,
                                "student_grade" : student_grade,
                                "student_subjects": {
                                    subject.strip()
                                    for subject in input("Subjects (comma-separated): ").split(",")
                                }            
                     })
                print("\nStudent added successfully!")

        case 2:
            print("\n--- Display All Students ---")
            if all_students:
                for student in all_students:
                    print(
                        f"Student ID: {student['student_info'][0]} | "
                        f"Name: {student['student_name']} | "
                        f"Age: {student['student_age']} | "
                        f"Grade: {student['student_grade']} | "
                        f"DOB: {student['student_info'][1]} | "
                        f"Subjects: {student['student_subjects']}"
                    )
                
            else:
                print("\nNo student records found!")

        case 3:
            user_data = int(input("Enter Student ID to update: "))

            for student in all_students:
                if user_data == student["student_info"][0]:
                        student["student_name"] = input("Name: ")
                        student["student_age"] = int(input("Age: "))
                        student["student_grade"] = input("Grade: ")
                        student["student_info"] = (
                            student["student_info"][0],
                            input("Date of Birth (YYYY-MM-DD): ")
                        )
                        student["student_subjects"] = {
                            subject.strip()
                            for subject in input("Subjects (comma-separated): ").split(",")
                        }            

                        print("Updated Successfully!")
                        break
            else:
                print("\nStudent ID does not exist!")
                
        case 4:
            user_data = int(input("Enter Student ID: "))

            for student in all_students:
                 if user_data == student["student_info"][0]:
                      del all_students[all_students.index(student)]
                      print("Student deleted successfully!\n")
                      break
            else:
                print("\nStudent ID does not exist!")
                 
        case 5:
            all_subjects = set()

            for subject in all_students:
                all_subjects.update(subject["student_subjects"])
            if all_subjects:
                print("\nSubjects Offered:",sorted(all_subjects))
            else:
                    print("No subjects found!")

        case 6:
            print("\nProgram terminated!")
            break
        
        case _:
            print("\nPlease enter valid choice!")   