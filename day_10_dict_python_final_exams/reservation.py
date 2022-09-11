import os

import sys

from pathlib import Path



class menu:
    def __init__(self, choice):
        self.choice = choice
        if choice == "A":
            count = 0
            file = open("reservation.txt")
            lines = file.readlines()[1:]
            file.close()
            for line in lines:
                count += 1

            if count == 0:
                print("There are no reservations!!")
                print()
            else:
                file = open("reservation.txt", "r")
                print(file.read())
                file.close()

        elif choice == "B":
    
            with open("reservation.txt", "r") as file:
                for last_line in file:
                    pass 
                
                    if last_line[0] == "#":
                        num = 1
                    else:
                        num = int(last_line[0]) + 1

                name = (input("Enter Name: "))
                date = (input("Enter Date: "))
                time = (input("Enter Time: "))
                adults = int(input("No. of Adult(s): "))
                children = int(input("No. of Children(s): "))
                file = open("reservation.txt", "a")
                file.write(f"{num}\t\t\t{name}\t\t\t{date}\t\t\t{time}\t\t\t{adults}\t\t\t{children}\n")
                file.close()
                print()


        elif choice == "C":
            resnum = input("Enter Reservation number: ")
            file1 = open("reservation.txt", "r")
            lines = file1.readlines()
            file1.close()
            file2 = open("reservation.txt", "w")

            for line in lines:
                if not line.startswith(resnum):
                    file2.write(line)
            file2.close()

        elif choice == "D":
            adults, children, total_adults, total_children, total = 0, 0, 0, 0, 0
            file = open("reservation.txt", "r")
            list_of_lists=[]
            report = ""
            i = 0

            for line in file:
                i += 1
                if i > 1:

                    stripped_line = line.strip()
                    line_list = stripped_line.split("\t\t\t")
                    adults += int(line_list[4])
                    children += int(line_list[5])
                    subtotal = (int(line_list[4]) * 500) + (int(line_list[5]) * 300)
                    total += subtotal
                    line_list.append(str(subtotal))
                    report += f"{line_list[0]}\t\t\t{line_list[2]}\t\t\t{line_list[3]}\t\t\t" \
                              f"{line_list[1]}\t\t\t{line_list[4]}\t\t\t{line_list[5]}\t\t\t{line_list[6]}\n"
            file.close()

            print()
            print()
            print("                                                                       REPORT")
            print()
            print("#\t\t\tDate\t\t\t\tTime\t\t\t\tName\t\t\t\tAdults\t\t\tChildren\t\tSubtotal")
            print(report)
            print("Total Number of Adults: ", adults)
            print("Total Number of Children: ", children)
            print("Grand Total: PHP ", total)
            print("---------------------------------------------------------------- nothing follows "
                  "----------------------------------------------------------------")
            print()
            print()

        elif choice == "E":
            import sys
            sys.exit("Thank you!")

        else:
            print("Invalid response. Please try again.")


while True:
    try:
        file = open("reservation.txt", "r")
    except FileNotFoundError:
        file = open("reservation.txt", "w+")
        file.write("#\t\t\tName\t\t\t        Date\t\t\t        Time\t\t\t    Adults\t\t\tChildren\n")
    file.close()

    print("RESTAURANT RESERVATION SYSTEM")
    print("System Menu:")
    print("A. View all Reservations\tB. Make Reservation")
    print("C. Delete Reservation\t\tD. Generate Report")
    print("E. Exit\n")

    selection_menu = input('Enter selection: ').upper()
    menu(selection_menu)