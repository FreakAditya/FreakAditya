with open("IPmarks.txt", "r") as marks_file, open("IPgrades.txt", "w") as grades_file:

    wts = [(50,20),(150,40),(100,15),(50,15),(15,10)]

    for i in marks_file:

        LIST = i.strip().split(",")

        roll_no = LIST[0]

        marks = [int(m) for m in LIST[1:]]
 
        norm_marks = [m/wt[0]*wt[1] for m, wt in zip(marks, wts)]

        total = sum(norm_marks)

        if total >= 80:
            grade = "A"
        elif total >= 70:
            grade = "A-"
        elif total >= 60:
            grade = "B"
        elif total >= 50:
            grade = "B-"
        elif total >= 40:
            grade = "C"
        elif total >= 35:
            grade = "C-"
        elif total >= 30:
            grade = "D"
        else:
            grade = "D"

        grades_file.write(f"{roll_no},{total:.2f},{grade}\n")
