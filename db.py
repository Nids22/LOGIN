from sqlite3 import connect
from this import d
import mysql.connector


class Db:
    local_host="localhost"
    user_name="root"
    pass_word="Neelesh220303"
    database="mydbs"


    def __init__(self):
        self.connect = self.db_connect()
       
    insert = {
        "email":"ni@ex.com",
        "username":"user1",
        "password":"fghyuyuy"
    }
    
    def db_connect(self,insert={},update={},select={}):
        mydb = mysql.connector.connect(
        host=self.local_host,
        user=self.user_name,
        password=self.pass_word,
        database = self.database
        )
        db = mydb.cursor()
        sql = "INSERT INTO login (email,username,password)  VALUES"+self.vals(insert,{})
        print(sql)
        # db = self.db_connect()
        # print(['hh',db])

        records=()
        y=list(records)

        for i in insert:
            

        
        
        records=tuple(y)
        
        db.execute(sql, ('nidhibhatia03@hotmail.com','Bhatia','password'))

        mydb.commit()

        print(db.rowcount, "record inserted.")

        # if insert:


        # return mydb.cursor()
        
        # self.connect.execute("CREATE DATABASE mydatabase")

        
#         mycursor = mydb.cursor()

# sql = "INSERT INTO mydbs (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

    def vals(self,field=(),values=()):
        len_field=(len(field)-1)

        new_val_string ="("
        for i,val in enumerate(field):
           
            if i==len_field:
        
                new_val_string+="%s)"
            else:
               new_val_string+="%s,"

            
        return str(new_val_string)    

    
    def insert_data(self,field,values):

        

        # get the number of fields that will be present in the fields list then represent them in the values section
        #make sure the number of values received match the number of field received

        sql = "INSERT INTO login (email,username,password)  VALUES (%s,%s,%s)"
        print(sql)
        db = self.db_connect()
        print(['hh',db])
       
        db.execute(sql, values)

        # db.commit()

        print(self.connect.rowcount, "record inserted.")



    
        
    

db = Db()
# db.insert_data(("email","username","password"),('nidhibhatia03@hotmail.com','Bhatia','password'))
db.db_connect()
