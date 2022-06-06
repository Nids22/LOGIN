from mydb2 import Db
from reg import Reg
class User:


    def __init__(self):
       
        newClass=None
        self.newClass = Db()
        
        
                 
    def check_username(self,username):

       return self.newClass.check_user1(username) 

            
    def check_pass(self,username,password): 
         
         return self.newClass.check_pass(username,password) 
         

    def change_pass(self,username,email,new_pass):

        return self.newClass.update_pass(username,email,new_pass)     

    def check_email(self,username,email):
          return self.newClass.valid_user(username,email)    