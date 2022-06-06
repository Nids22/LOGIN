from pickle import TRUE
from mydb2 import Db

class Reg:
    newClass=None

    def __init__(self):
        self.newClass = Db()
        
        # check=self.checker()
        

        # if check:
        #     print("All done, thank you!") 

        

    def checker(self):
        # username=input("Please input the username :")

        
        # while self.newClass.check_user1(username):
        #   print("This username has already been taken, please select another : ")  
        #   username=input("Please input the username :")


        # email=input("Please input your email : ")

        # while self.newClass.check_user2(email):
        #   print("This email has already been used, please select another : ")  
        #   email=input("Please input the email :")

        # password="try"
        # pass_check="hold"  

        # while not password==pass_check:

        #     password= input("Please input your password : ")  
        #     pass_check=input("Please re-enter your password : ")
            

        # s_tuple=(email,username,password)
            

        # self.newClass.insert_data(("email","username","password"),s_tuple)

        return True
    
    def user_check(self,username):
        return self.newClass.check_user1(username)

    def email_check(self,email):
        return self.newClass.check_user2(email)

    def e_insert(self,email,username,password):
        
         s_tuple=(email,username,password)
            
         self.newClass.insert_data(("email","username","password"),s_tuple)
         
# new_user = Reg()