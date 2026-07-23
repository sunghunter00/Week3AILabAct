def check_borrowing(overdue, accountStatus):
    if overdue == "yes":
        return "Not allowed: overdue books"
    elif accountStatus == "suspended":
        return "Not allowed: suspended account"
    else:
        return "Borrowing allowed"


approvedCount = 0

while True:
    print("\n===== Library Kiosk =====")

    studentName = input("Enter student name (type 'exit' to quit): ")

    if studentName.lower() == "exit":
        break

    overdue = input("Do you have overdue books? (yes/no): ").lower()
    accountStatus = input("Enter account status (active/suspended): ").lower()
    bookCount = int(input("How many books do you want to borrow? "))

    borrowResult = check_borrowing(overdue, accountStatus)

    print("\nResult:", borrowResult)

    if borrowResult == "Borrowing allowed":
        if bookCount <= 0:
            print("Please enter at least 1 book.")
        elif bookCount > 3:
            print("You can only borrow up to 3 books.")
            print("Approved books: 3")
            approvedCount += 1
        else:
            print(f"You may borrow {bookCount} book(s).")
            approvedCount += 1

print("\nLibrary session ended.")
print("Total approved students:", approvedCount)