# 1. Create a Name Generator App
# 2. Create 3 lists for first name, middle name, and last name with 10 items per list
# 3. The application will ask the user to generate a new name.
# 4. If yes, use a random number between 0 - 9 to randomly select items in the lists
# 5. Display the generated name
# “Congratulations! Your new name is ________
# 6. If No, display the word “Thank
# you! ” and display all the names that user generated.




import random





first = ["Kai", "Hunter", "Luca", "Quinn", "River", "Skylar", "Hayden", "Riley", "Reese", "Jude"]
middle = ["Abbot", "Griffith", "Maxfield", "Rufus", "Eva", "Emma", "Olivia", "Sims", "Tan", "Ovilda"]
last = ["James", "Doha", "Harden", "Jordan", "Bryant", "Williams", "Simmons", "Imbid", "George", "Leonard"]
namebank = []
while True:
    name = input("Do you want to generate a new name? [y/n]: ")
    if name.upper() == "Y":
        rand = random.randint(0, 4)
        randname = first[rand] + " " + middle[rand] + " " + last[rand]
        namebank.append(randname)
        print(f"Your new name is {randname}\n")
        continue
    elif name.upper() == "N":
        print("Thank you!")
        print("List of generated names:")
        for x in namebank:
            print(f"{x}")
        break
