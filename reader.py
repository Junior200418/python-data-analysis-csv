import os

print(f"\n{" " * 15}WELCOME")
print(f"This is a python CSV analysis tool\n")
print("Note: Pls keep file in same folder with the tool or use full path eg C:/.. when entering file name")
file_Name = str(input("What is the name of the file: "))
can_Read = ""
is_Empty = ""


if not os.path.exists(file_Name):
    print("File does not exist. Pls try again")
else:
    print("Processing......\n")

if os.path.getsize(file_Name) == 0:
    is_Empty = "YES"
else:
    is_Empty = "NO"

try:
    with open(file_Name, "r") as f:
        data = f.read()
    can_Read = "YES"
except:
    can_Read = "No"
    

print(f"[File Name: {file_Name}] {" "*5} [Can be read: {can_Read}]{" "*5} [Is Empty: {is_Empty}]\n")

lines = 0

while True:
    menu = str(input(f"What would you like to do: Get Started (Y) Quit (Q): ")).lower()
    if menu == "q":
        print("GoodBye!!")
        break
    elif menu == "y":
        while menu == "y":
            with open(file_Name) as file:
                print("\n1. Print out the text file to screen")
                print("2. Number of Lines")
                print("3. Back\n")
                menu_2 = int(input("Select: "))
                if menu_2 == 1:
                    for z in file:
                        print(z)
                elif menu_2 == 2:
                    lines = 0
                    for i in file:
                        lines += 1
                    print(f"There are {lines} lines of text in the file")
                elif menu_2 == 3:
                    break
                else:
                    try:
                        if menu_2 != 1 or menu_2 != 2 or menu_2 != 3:
                            print("Error in numbering. Try Again")
                    except:
                        print("ok")