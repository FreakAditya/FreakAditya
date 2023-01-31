grades = {'A+': 10, 'A': 10, 'A-': 9, 'B+': 8,
          'B-': 7, 'C+': 6, 'C-': 5, 'D': 4, 'F': 2}

list = []
while True:
    try:
        # Get input from user
        course_name, credit, grade = input(
            "Enter sub name, credit, and grade: ").split()
        # Convert credit to int
        credit = int(credit)
        # Append the input to the list list
        if ((course_name.isupper()) == True and (course_name.isalnum()) == True) and (credit == 1 or credit == 2 or credit == 4) and (
                grade == 'A+' or grade == 'A' or grade == 'A-' or grade == 'B+' or grade == 'B' or grade == 'B-' or grade == 'C+'or grade == 'C' or grade == 'C-' or grade == 'D' or grade == 'F'):

            list.append((course_name, credit, grade))
        elif ((course_name.isupper()) != True or (course_name.isalnum()) != True):
            print("Incorrect Course Name ")
        elif (credit != 1 and credit != 2 and credit != 4):
            print("Incorrect Credit input")
        elif (grade != 'A+' and grade != 'A' and grade != 'A-' and grade != 'B+' and grade != 'B' and grade != 'B-' and grade != 'C+' and grade != 'C' and grade != 'C-' and grade != 'D' and grade != 'F'):
            print("Incorrect Grade Input")
    except:
        break
list = sorted(list)
for sub in list:
    course_name, credit, grade = sub
    print(f"{course_name}: {grade}")

# calculate the SGPA
cred_sum = 0
grade_sum = 0
for sub in list:
    course_name, credit, grade = sub
    grade_sum += credit * grades[grade]
    cred_sum += credit
SGPA = grade_sum / cred_sum

# Print the SGPA
print("SGPA: ", SGPA)
