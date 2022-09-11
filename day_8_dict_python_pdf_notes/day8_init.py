class Employee:
    def __init__(self, name, email):
        self.myname = name
        self.myemail = email
charname = input('Enter name:')
charemail = input('Enter email:')
anime = Employee(charname, charemail)
print("Name:", anime.myname, "\nEmail:", anime.myemail)

one_piece = Employee('Luffy', 'luffy@gmail.com')
print("Name:", one_piece.myname, "\nEmail:", one_piece.myemail)