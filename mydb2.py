from pickle import TRUE
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

    def db_connect(self,insert={},update={},select={}):
    
        connection = None

        try:
            connection = mysql.connector.connect(
            host=self.local_host,
            user=self.user_name,
            password=self.pass_word,
            database = self.database
            )
        except error as error:
            print("No connection established")


        return connection
        

    def vals(self,field=(),values=()):
        len_field=(len(field)-1)
        new_field_string = "("
        new_val_string ="("
        for i,val in enumerate(field):
           
            if i==len_field:
                new_field_string+=field[i]+")"
                new_val_string+="%s)"
            else:
               new_field_string+=field[i]+","
               new_val_string+="%s,"

            
        return [str(new_field_string),str(new_val_string)]    

    
    def insert_data(self,field,values):

        db = self.db_connect()
        connection = db.cursor()
        # "(email,username,password)"

        sql = "INSERT INTO login "+self.vals(field,values)[0]+" VALUES" + self.vals(field,values)[1]
        
       
       
        connection.execute(sql, values)

        db.commit()
        print("done")


        # print(self.connect.rowcount, "record inserted.")

    def check_user1(self,username):
        
        db = self.db_connect()
        connection = db.cursor()

        the_in="SELECT * FROM login WHERE username = "+"'"+str(username)+"'"

        t_uple=[username]

        connection.execute(the_in)

        result = connection.fetchall()

        # db.commit()
        if result:
            return True
        else:
            return False  

    def check_user2(self,address):

        db = self.db_connect()
        connection = db.cursor()

        the_in="SELECT * FROM login WHERE username = "+"'"+str(address)+"'"

        connection.execute(the_in)

        result = connection.fetchall()

        if result:
            return True
        else:
            return False  

    def check_pass(self,username,password):

        db = self.db_connect()
        connection = db.cursor()

        the_in="SELECT * FROM login WHERE username = "+"'"+str(username)+"'" +"AND password = "+"'"+str(password)+"'"
        
        connection.execute(the_in)

        result=connection.fetchall()
  

        if result:
            return True
        else:
            return False

    def update_pass(self,username,email,up_pass):
    
        db = self.db_connect()
        connection = db.cursor()

        # the_in="UPDATE login SET password="+"'"+str(up_pass)+"'"+ "WHERE username = "+"'"+str(username)+"'" +"AND email= "+"'"+str(email)+"'"
        the_in="UPDATE login SET password="+"'"+up_pass+"'"+ "WHERE username="+"'"+username+"'" +"AND email ="+"'"+email+"'"
        connection.execute(the_in)
       
       
        db.commit() 

    def valid_user(self,username,email) :

        db = self.db_connect()
        connection = db.cursor()

        the_in="SELECT * FROM login WHERE username = "+"'"+str(username)+"'" +"AND email = "+"'"+str(email)+"'"
        
        connection.execute(the_in)

        result=connection.fetchall()

        #print (result)

        if result:
            return True
        else:
            return False 

db = Db()
# db.insert_data(("email","username","password"),('nid03@hotmail.com','Bia','passrd'))
# db.insert_data()
db.update_pass("sun","s@s.com","newpass")
