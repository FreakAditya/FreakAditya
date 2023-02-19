cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
policy = [80, 65, 50, 40, 30]

# Marks data
marks = {}

def create_course(cname, credits, assessments, policy):
    course = {
        "cname": cname,
        "credits": credits,
        "assessments": assessments,
        "policy": policy
    }
    return course

def get_cutoff(file_name):
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


def upload_marks_data(file):
    with open(file, "r") as f:
        for line in f:
            line = line.strip().split()
            rollno, marks_data = line[0], line[1:]
            marks[rollno] = {assessments[i][0]: int(mark) for i, mark in enumerate(marks_data)}

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

def generate_summary(course, marks):
    print("Course:", course["cname"], "Credits:", course["credits"])
    print("Grading policy:", course["policy"])
    print("Assessments and weights:", course["assessments"])
    
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for student_marks in marks.values():
        grades[student_marks["grade"]] += 1
    print("Grading summary:", grades)

def print_grades(marks, file):
    with open(file, "w") as f:
        for rollno, student_marks in marks.items():
            f.write(f"{rollno}, {student_marks['total_marks']}, {student_marks['grade']}\n")

def search_student_record(rollno, marks):
    if rollno in marks:
        student_marks = marks[rollno]
        print("Rollno:", rollno)
        print("Marks in assessments:", student_marks)
        print("Total marks:", student_marks["total_marks"])
        print("Grade:", student_marks["grade"])
    else:
        print("Record not found for rollno:", rollno)

# Creating the course
course = create_course(cname, credits, assessments, policy)

# Uploading marks data
upload_marks_data("marks.txt")

# Do grading
do_grading(course, marks)


while True:
    operation = input("(1: Generate summary, 2: Print grades, 3: Search for student, 0: Exit): ")
    if operation == '0':
        break
    elif operation == '1':
        generate_summary(course, marks)
        get_cutoff("grades.txt")

        
    elif operation == '2':
        print_grades(marks, "grades.txt")
        print("Grades written to grades.txt")

    elif operation == '3':
        rollno = input("Enter the rollno to search:")
        search_student_record(rollno, marks)

