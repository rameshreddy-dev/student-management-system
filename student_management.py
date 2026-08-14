students = []


def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll_no = line.strip().split(",")

                student = {
                    "name": name,
                    "roll_no": roll_no
                }

                students.append(student)

    except FileNotFoundError:
        pass


def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(
                student["name"]
                + ","
                + student["roll_no"]
                + "\n"
            )


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    student = {
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)

    save_students()

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print(student["name"], "-", student["roll_no"])


def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student found:")
            print(student["name"], "-", student["roll_no"])
            return

    print("Student not found.")


def update_student():
    roll_no = input("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            new_name = input("Enter the new student name: ")

            student["name"] = new_name

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)

            save_students()

            print("Student deleted successfully!")
            return

    print("Student not found.")


load_students()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using the Student Management System.")
        break

    else:
        print("Invalid choice.")