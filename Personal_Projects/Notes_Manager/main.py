while True:
    print("\n1. Add new Notes.")
    print("2. Open existing Notes.")
    print("3. Delete Notes.")
    print("4. Exit.\n")


    choice = input("Enter choice: ")

    if choice == "1":
        note = input("Enter your Notes: ")
        with open("hw.txt", "a") as f:
            f.write(note + "\n")

    elif choice =="2":
        try:
            with open("hw.txt", "r") as f:
                print("Your notes: ")
                for i, line in enumerate(f,start =1):
                    print(f"{i}. {line.strip()}")

        except FileNotFoundError:
            print("No notes found yet!")

    elif choice == "3":
        try:
            with open("hw.txt", "r") as f:
                notes = f.readlines()
            if not notes:
                print("No notes to delete")
            else:
                for i, line in enumerate(notes,start=1):
                    print(f"{i}. {line.strip()}")
                del_num = int(input("Enter note number to delete: "))
                if 1 <= del_num <= len(notes):
                    notes.pop(del_num - 1)

                    with open("hw.txt", "w") as f:
                        f.writelines(notes)

                    print("Note deleted")
                else:
                    print("Invalid number")
        except FileNotFoundError:
            print("No notes found")

        except ValueError:
            print("Enter a valid number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

