
import mysql.connector as mysql
mydb = mysql.connect(host="localhost", user="root", passwd="kishore",
database='studentdata')
mycursor = mydb.cursor()
mycursor.execute(' select * from std group by rollno having  count(rollno)>1')
#for i in mycursor:
#    print(i)
class Duplicate():

 def __init__(self):
   self.hand = []

 def new_round(self):
   self.hand1 = mycursor.rowcount
   self.hand = [self.hand1]
   print(self.hand)


hand1 = mycursor.fetchall()

kishore= Duplicate()
kishore.new_round()
mydb.commit()