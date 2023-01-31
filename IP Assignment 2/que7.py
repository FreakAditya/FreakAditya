address_book = {}

with open("file.txt", 'r+') as f:
    for line in f:
        name, address, phone, email = line.strip().split()

        if name in address_book:

            address_book[name].append(
                {'address': address, 'phone': phone, 'email': email})
        else:

            address_book[name] = [
                {'address': address, 'phone': phone, 'email': email}]
# print(address_book)
# with open("file.txt",'w') as f:
#     f.write('\n')
loop = 1
while(loop != 5):
    print("(1) insert a new entry")
    print("(2) delete an entry")
    print("(3) find all matching entries given a partial name")
    print("(4) find the entry with a phone number or email")
    print("(5) exit")
    inp = (int(input("Choose one option: ")))
    if inp == 1:
        name = input("Enter the name of the person: ")
        address = input("Enter the address: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")

        if name in address_book:
            address_book[name].append(
                {'address': address, 'phone': phone, 'email': email})
        else:

            address_book[name] = [
                {'address': address, 'phone': phone, 'email': email}]

        with open("file.txt", "a") as f:
            f.write("\n")
            f.write(f"{name} {address} {phone} {email}\n")

    elif inp == 2:
        name = input("Enter the name of the person to delete: ")

        if name in address_book:

            del address_book[name]

            with open("file.txt", "r") as f:
                lines = f.readlines()
            with open("file.txt", "w") as f:
                for line in lines:
                    if name not in line:
                        f.write(line)
        else:
            print(f"{name} not found in the address book.")

    elif inp == 3:
        partial_name = input("Enter the partial name: ")

        results = {k: v for k, v in address_book.items(
        ) if partial_name.lower() in k.lower()}
        if len(results) > 0:
            print("Results in address_book:")
            for k, v in results.items():
                print(k, v)
        else:
            print(
                f"No entries found in address_book with partial name {partial_name}.")

        results = []
        with open("file.txt", "r") as f:
            for line in f:
                if partial_name.lower() in line.lower():
                    results.append(line)
        if len(results) > 0:
            print("Results in file:")
            for r in results:
                print(r)
        else:
            print(
                f"No entries found in file with partial name {partial_name}.")

    elif inp == 4:
        search_term = input("Enter the phone number or email: ")

        results = []
        with open("file.txt", "r") as f:
            for line in f:
                if search_term in line:
                    results.append(line)
        if len(results) > 0:
            print("Results in file:")
            for r in results:
                print(r)
        else:
            print(f"No entries found in file with {search_term}.")

    else:
        print("Wrong input ")

    loop = inp
# print(list_of_address_book)
f.close()
