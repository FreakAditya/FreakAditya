def process_data(data):
    data = sorted(data, key=lambda x: x[3])
    students = {}
    for entry in data:
        name, crossing, gate, time = entry
        if name not in students:
            students[name] = []
        if crossing == "ENTER":
            if students[name] and students[name][-1][1] == "ENTER":
                continue
            students[name].append((gate, crossing, time))
        elif crossing == "EXIT":
            if students[name] and students[name][-1][1] == "EXIT":
                students[name].pop()
            students[name].append((gate, crossing, time))
    return students


def save_student_record(student, students, current_time):
    with open(f"{student}.txt", "w") as file:
        if student not in students:
            file.write(f"{student} not found in records.\n")
        else:
            record = students[student]
            file.write(f"Record of {student}:\n")
            for entry in record:
                file.write(f"Gate {entry[0]}, {entry[1]} at {entry[2]}\n")
            if record[-1][1] == "ENTER":
                file.write(f"{student} is currently present in the campus.\n")
            else:
                file.write(
                    f"{student} is not currently present in the campus.\n")


data = []
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        items = line.strip().split(", ")
        data.append((items[0], items[1], int(items[2]), items[3]))
students = process_data(data)


while True:
    inp = input("1.Check if student in/out status and their presence.\n2.Students moved in and out in given time interval.\n3.No of times students enter exited from perticular gate.\n")
    if inp == "0":
        break
    elif inp == "1":
        student = input("Enter the name of the student: ")
        current_time = input("Enter the current time: ")
        save_student_record(student, students, current_time)
    elif inp == "2":
        start_time = input("Enter the start time: ")
        end_time = input("Enter the end time: ")
        with open("output.txt", "w") as file:
            file.write("Records during the specified time period:\n")
            for student, record in students.items():
                for entry in record:
                    if start_time <= entry[2] <= end_time:
                        file.write(
                            f"{student}, {entry[1]}, {entry[0]}, {entry[2]}\n")

    elif inp == "3":
        gate_number = int(input("Enter the gate number: "))
        enter_count = 0
        exit_count = 0
        for record in students.values():
            for entry in record:
                if entry[0] == gate_number:
                    if entry[1] == "ENTER":
                        enter_count += 1
                    else:
                        exit_count += 1
        print(
            f"Number of times students have entered the campus through gate {gate_number}: {enter_count}")
        print(
            f"Number of times students have exited the campus from gate {gate_number}: {exit_count}")
    
    else:
        print("Wrong input")
