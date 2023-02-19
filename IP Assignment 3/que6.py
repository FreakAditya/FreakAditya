import time
import random


class Course:
    def __init__(self, assessments, policy):
        self.assessments = assessments
        self.policy = policy
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def do_grading(self):
        for student in self.students:
            student.calculate_grade(self.policy)


class Student:
    def __init__(self, rollno, marks):
        self.rollno = rollno
        self.marks = marks
        self.grade = None

    def calculate_grade(self, policy):
        total_marks = sum(self.marks.values())
        for i in range(len(policy) - 1):
            if total_marks >= policy[i]:
                self.grade = "ABCD"[i]
                break


def upload_marks(course, file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    for line in lines:
        items = line.strip().split(' ')
        rollno = items[0]
        marks = {assessment[0]: float(mark) for assessment, mark in zip(
            course.assessments, items[1:])}
        student = Student(rollno, marks)
        course.add_student(student)


# -------------------------------------WITHOUT OOPS + DICTIONARY--------------------------------------------#


def create_course(assessments, policy):
    course = {
        "assessments": assessments,
        "policy": policy
    }
    return course


def upload_marks_data(file):
    with open(file, "r") as f:
        for line in f:
            line = line.strip().split()
            rollno, marks_data = line[0], line[1:]
            marks[rollno] = {assessments[i][0]: int(mark) for i, mark in enumerate(marks_data)}

def print_grades(marks, file):
    with open(file, "w") as f:
        for rollno, student_marks in marks.items():
            f.write(f"{rollno}, {student_marks['total_marks']}, {student_marks['grade']}\n")


def do_grading(course, marks):
    policy = course["policy"]
    for rollno, student_marks in marks.items():
        total_marks = sum(student_marks.values())
        if total_marks >= policy[0]:
            marks[rollno]["grade"] = "A"
        elif total_marks >= policy[1]:
            marks[rollno]["grade"] = "B"
        elif total_marks >= policy[2]:
            marks[rollno]["grade"] = "C"
        elif total_marks >= policy[3]:
            marks[rollno]["grade"] = "D"
        else:
            marks[rollno]["grade"] = "F"
        marks[rollno]["total_marks"] = total_marks


def search_student_record(rollno, marks):
    if rollno in marks:
        count2 += 1
        print("yes")


# Create the course object and upload student marks
assessments = [("labs", 30), ("midsem", 15),
               ("assignments", 30), ("endsem", 25)]
policy = [80, 65, 50, 40, 0]
cname, credits = "IP", 4
marks = {}
ip_course = Course(assessments, policy)
upload_marks(ip_course, 'marks.txt')
ip_course.do_grading()

course = create_course(assessments, policy)

upload_marks_data('marks.txt')

# do_grading(course,marks)


roll_list = [2021229, 2021302, 2031231, 2032133]
count = 0
# Uploading marks data
upload_marks_data("marks.txt")
for i in range(2):
    if i == 0:
        print("Performance comparison for grading operation")
        # Perform the do_grading operation n number of times and calculate the time taken
        n = int(input("Enter the number of times to run do_grading: "))
        start_time = time.time()
        for i in range(n):
            ip_course = Course(assessments, policy)
            upload_marks(ip_course, 'marks.txt')
            ip_course.do_grading()
            ip_course.do_grading()
        end_time = time.time()

        # Display the time taken in milliseconds
        time_taken = (end_time - start_time) * 1000
        print("Time taken in OO: ", time_taken, "milliseconds")

        start_time2 = time.time()
        for i in range(n):
            course = create_course(assessments, policy)

            # Uploading marks data
            upload_marks_data("marks.txt")
            do_grading(course,marks)
        end_time2 = time.time()

        # Display the time taken in milliseconds
        time_taken2 = (end_time2 - start_time2) * 1000
        print("Time taken without OO: ", time_taken2, "milliseconds")
        if time_taken > time_taken:
            print("Without OOPs was ",time_taken-time_taken2,"milisec faster")
        else:
            print("With OOPs was ",time_taken2-time_taken," milisec faster")
    else:
        print("Performance comparison for search operation")
        n = int(input("Enter the number of times to do SEARCHING: "))
        start_time3 = time.time()
        for i in range(n):
            ip_course = Course(assessments, policy)
            upload_marks(ip_course, 'marks.txt')
            ip_course.do_grading()
            rollno = random.choice(roll_list)
            for st in ip_course.students:
                if st.rollno == rollno:
                    count += 1
        end_time3 = time.time()

        # Display the time taken in milliseconds
        time_taken3 = (end_time3 - start_time3) * 1000
        print("Time taken in OO: ", time_taken3, "milliseconds")

        start_time4 = time.time()
        for i in range(n):
    
            course = create_course(assessments, policy)
            upload_marks_data("marks.txt")
            rollno = random.choice(roll_list)
            search_student_record(rollno, marks)
        end_time4 = time.time()

        # Display the time taken in milliseconds
        time_taken4 = (end_time4 - start_time4) * 1000
        print("Time taken without OO: ", time_taken4, "milliseconds")
        if time_taken3 > time_taken4:
            print("Without OOPs was ",time_taken3-time_taken4,"millisec faster")
        else:
            print("With OOPs was ",time_taken4-time_taken3," millisec faster")

    print("----------------------------------CHANGE---------------------------------------------")
