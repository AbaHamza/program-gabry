from db import con_db

con = con_db()
x=con.query("select * from users")

