# Build a gradebook that calculates student averages and determines letter grades.

# ### 📋 Requirements
# 1. Store student data in a dictionary format: `{"name": [list_of_grades]}`
# 2. Create a menu system with options:
#    - Add new student
#    - Add grade to existing student
#    - View student average and letter grade
#    - Display class statistics
#    - Exit
# 3. Calculate letter grades: A(90+), B(80-89), C(70-79), D(60-69), F(<60)
# 4. Show class average and highest/lowest performing student
Student={}
def add_student():
    name=input("Enter student name: ")
    if name in Student:
        print("student already exist")
    else:
        Student[name]=[]
        print(f"{name} added succesfully")
def add_grade():
    name=input("Enter student name: ")
    if name not in Student:
        print("Student not found.")
        return
    try:
        grade=float(input("Enter grade(0-100):"))
        if 0<=grade<=100:
            Student[name].append(grade)
            print("grade added.")
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input. please enter a number.")
def calculate_letter_grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    else:
        return "F"
def view_student():
    name= input("Enter student name: ")
    if name not in Student:
        print("Student not found")
        return
    grades = Student[name]
    if not grades:
        print("No grades available.")
        return
    avg=sum(grades)/len(grades)
    letter = calculate_letter_grade(avg)
    print(f"{name}'s average: {avg: 1f} - letter grade: {letter}")
def class_stats():
    if not Student:
        print("No students in the system")
        return
    total_grades=[]
    for grade in Student.values():
        total_grades.extend(grades)
    if not total_grades:
        print("No grades available for statistics.")
        return
    avg_class=sum(total_grades)/len(total_grades)
    highest=max(total_grades)
    lowest=min(total_grades)
    print(f"class average: {avg_class:1f}")
    print(f"Highest grade: {highest}")
    print(f"Lowest Grade: {lowest}")
def menu():
    while True:
        print("\n--- Student Grade system---")
        print("1. add new student")
        print("2. Add grade to existing student")
        print("3. View student average and letter grade")
        print("4. Print class statistic")
        print("5. exit")
        choice=input("choose an option(1-5):")
        if choice == '1':
            add_student()
        elif choice == '2':
            add_grade()
        elif choice == '3':
            view_student()
        elif choice == '4':
            class_stats()
        elif choice == '5':
            print("Exiting the system. Goodbye")
            break
        else:
            print("invalid option. try again")
menu()