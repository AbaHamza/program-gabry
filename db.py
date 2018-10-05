import mysql.connector

class con_db():
    def __init__(self):
        self.mydb= mysql.connector.connect(
             host="localhost",
             user="root",
             passwd="123qaz123",
             database= "sohep"
              )
        self.mycursor = self.mydb.cursor()
    def query(self, x):
        self.mycursor.execute(x)
        return list(self.mycursor)


'''

con=con_db()
x= con.query("select * from users")
print(x[0])

'''



