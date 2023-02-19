class Course:
    def __init__(self, cname, credits, assessments, policy):
        self.cname = cname
        self.credits = credits
        self.assessments = assessments
        self.policy = policy
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def do_grading(self):
        for student in self.students:
            student.calculate_grade(self.policy)

    def get_cutoff(self,file_name):
        A = []
        B = []
        C = []
        D = []
        with open(file_name, 'r') as f:
            lines_data = f.readlines()
        for k in lines_data:
            l = k.strip().split(', ')
            grade = l[2]
            score = float(l[1])
            if grade == "A":
                A.append(score)
            elif grade == "B":
                B.append(score)
            elif grade == "C":
                C.append(score)
            elif grade == "D":
                D.append(score)
        
        if len(A) == 0:
            print("No Cutoff")
        elif len(A) == 1:
            print("A cutoff ", A[0])
        else:
            max_diff = float('-inf')
            max_index = None
            for i in range(len(A) - 1):
                diff = A[i + 1] - A[i]
                if diff > max_diff:
                    max_diff = diff
                    max_index = i
            if max_index is not None:
                print("A cutoff ", (A[max_index] + A[max_index + 1]) / 2)
            
        if len(B) == 0:
            print("No Cutoff")
        elif len(B) == 1:
            print("B cutoff ", B[0])
        else:
            max_diff = float('-inf')
            max_index = None
            for i in range(len(B) - 1):
                diff = B[i + 1] - B[i]
                if diff > max_diff:
                    max_diff = diff
                    max_index = i
            if max_index is not None:
                print("B cutoff ", (B[max_index] + B[max_index + 1]) / 2)
            
        if len(C) == 0:
            print("No Cutoff")
        elif len(C) == 1:
            print("C cutoff ", C[0])
        else:
            max_diff = float('-inf')
            max_index = None
            for i in range(len(C) - 1):
                diff = C[i + 1] - C[i]
                if diff > max_diff:
                    max_diff = diff
                    max_index = i
            if max_index is not None:
                print("C cutoff ", (C[max_index] + C[max_index + 1]) / 2)
            
        if len(D) == 0:
            print("No Cutoff")
        elif len(D) == 1:
            print("D cutoff ", D[0])
        else:
            max_diff = float('-inf')
            max_index = None
            for i in range(len(D) - 1):
                diff = D[i + 1] - D[i]
                if diff > max_diff:
                    max_diff = diff
                    max_index = i
            if max_index is not None:
                print("D cutoff ", (D[max_index] + D[max_index + 1]) / 2)

    def get_summary(self):
        summary = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'F': 0
        }
        for student in self.students:
            summary[student.grade] += 1

        return summary

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
        marks = {assessment[0]: float(mark) for assessment, mark in zip(course.assessments, items[1:])}
        student = Student(rollno, marks)
        course.add_student(student)


cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
policy = [80, 65, 50, 40, 0]
ip_course = Course(cname, credits, assessments, policy)

upload_marks(ip_course, 'marks.txt')

ip_course.do_grading()

while True:
    inp = input("(1: Generate summary, 2: Print grades, 3: Search for student, 0: Exit): ")
    if inp == '0':
        break
    elif inp == '1':
        print("Course:- ",cname,",","Credit:- ",credits)
        print(assessments)
        summary = ip_course.get_summary()
        print("Grading summary:")
        for grade, count in summary.items():
            print(f"{grade}: {count}")
        ip_course.get_cutoff("grades.txt")

        
    elif inp == '2':
        with open('grades.txt', 'w') as f:
            for student in ip_course.students:
                f.write(f"{student.rollno}, {sum(student.marks.values())}, {student.grade}\n")
        print("Grades written to grades.txt")
    elif inp == '3':
        rollno = input("Enter the roll number of the student: ")
        for st in ip_course.students:
            if st.rollno == rollno:
                print("Roll number: ", st.rollno)
                print("Marks: ", st.marks)
                print("Total marks: ", sum(st.marks.values()))
                print("Grade: ", st.grade)
                break
        else:
            print("Student not found.")


