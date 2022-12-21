import pyodbc

connection = pyodbc.connect('Driver={SQL SERVER};'
                            'Server=LAPTOP-VUTUC4CP;'
                            'Database = TRIVIA;'
                            'Trusted_Connection=yes;')


cursor = connection.cursor()



def filled():
    StudentId = int(input("Enter your id number: "))
    Firstname = input("Enter your firstname: ")
    Lastname = input("Enter your lastname: ")
    City = input("Enter your city: ")
    cursor.execute("INSERT INTO TRIVIA.dbo.tblTrivia(StudentId,Firstname,Lastname,City) VALUES (?,?,?,?)",
                   (StudentId, Firstname, Lastname, City))
    connection.commit()





filled()
cursor.close()
connection.close()
