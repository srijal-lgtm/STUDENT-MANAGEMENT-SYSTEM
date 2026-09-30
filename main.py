students = []

def add_student():
    print("\n--- Add Student ---")

    sid = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    marks = input("Enter student marks: ")

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("\nStudent added successfully!")


def view_students():
    print("\n--- All Student Records ---")

    if students == []:
        print("No student records available.")
    else:
        for student in students:
            print("----------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])


def search_student():
    print("\n--- Search Student ---")

    sid = input("Enter student ID: ")

    for student in students:
        if student["id"] == sid:
            print("\nStudent found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            return

    print("Sorry, student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    sid = input("Enter student ID: ")

    for student in students:
        if student["id"] == sid:
            print("Student:", student["name"])
            confirm = input("Do you want to delete? (yes/no): ")

            if confirm == "yes":
                students.remove(student)
                print("Record deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print("Student not found.")


while True:
    print("\n===== STUDENT RECORD MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nExiting Student Record Management System.")
        break

    else:
        print("\nInvalid choice. Please try again.")
