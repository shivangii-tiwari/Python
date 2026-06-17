class Student:
    def __init__(self,student_ID,student_name,age,marks):
        self.student_ID = student_ID
        self.student_name=student_name
        self.age=age
        self.marks=marks
class Student_mangment_system:
    def __init__(self):
        self.students = []   #this empty list for storing the number of student
    def add_student(self):   #we are adding the student here
        sid = int(input("enter the ID: "))
        name = input("enter name: ")
        age = int(input("enter the age: "))
        marks = float(input("enter the marks: "))
        student = student(sid,name,age,marks)
        self.student.append(student)
        print("stud added sucessfully")
    def view_student(self):   #we are viewing the student here
        for student in self.students:
            print(student.student_id,student.student_name,student.age,student.marks)
    def search_student(self):  #here we are searching for student
        sid = int(input("enter the student ID: "))
        for student in self.students:
            if student.student_ID == sid:
                print("student found")
                print(student.name)
                return
            print("student not found")
    def update_marks(self):  #here we are updating the marks of student
        sid = int(input("enter the ID: "))
        for student in self.students:
            if student.student_ID == sid:
                student.marks = float(input("enter the new marks: "))
                print("marks updated")
                return
            print("student not found")
    def delete_student(self):   #here we are deleting the student
        sid = int(input("enter the ID: "))
        for student in self.students:
            if student.student_ID == sid:
                self.students.remove(student)
                print("removed sucessfully")
                return
            print("student not found")
    def highest_marks(self):  # here we are showing waaaooo student
        if not self.students:
            print("students not avilable")
            return
        waaaooo_student = self.students[0]
        for student in self.students:
            if student.marks > waaaooo_student.marks:
                waaaooo_student = student
        print("waaaoo student: ")
        print(waaaooo_student.name,waaaooo_student.marks)
sms = Student_mangment_system()
while True:
    print("\n  student Management System")
    print("1. add student")
    print("2.view all student")
    print("3.search student")
    print("4.update marks")
    print("5.delete student")
    print("6.show highest marks student")
    print("7.Exit")
    choice = input("enter your choice: ")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.view_students()

    elif choice == "3":
        sms.search_student()

    elif choice == "4":
        sms.update_marks()

    elif choice == "5":
        sms.delete_student()

    elif choice == "6":
        sms.highest_marks_student()

    elif choice == "7":
        print("Thank you for using Student Management System")
        break

    else:
        print(" Invalid Choice! Please try again.")

        









