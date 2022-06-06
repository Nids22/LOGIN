import base64
from login import User
from reg import Reg
from mydb2 import Db
import pyautogui
import bcrypt
import maskpass


class NewUser:
   

    def create_user(self):
                user_acc = User()
                user_reg=Reg()
                user_data=Db()

                # new username input
                username = input("Please provide a username : ") 
                
                # used username
                NewUser.user_check(self,username)
                

                # new email input
                email= input("Please provide an email : ")  

                # used email
                NewUser.email_check(self,email)

                # password input and check
                NewUser.pass_check(self,username,email)
              

    # user-check func
    def user_check(self,username):
         user_reg=Reg()

         while user_reg.user_check(username) or len(username)>20 :
                    if(len(username)>20):
                        print("Username too long, has to be less than 20 characters")
                        username=input("Please provide a username : ") 
                    else:    
                        print("Username not available")
                        username = input("Please provide a username : ") 

    # email-check func
    def email_check(self,email):
         user_reg=Reg()   
         substr="@"
         substr2=".com"  

         while user_reg.email_check(email) or (not (substr) in email)  or not (substr2) in email:

                    if(user_reg.email_check(email)):
                
                        print("Email already in use")
                        email= input("Please provide an email : ") 
                    else:

                        print("This is not an email")
                        email= input("Please provide an email : ") 
                              
    # pass_check func                
    def pass_check(self,username,email):
            user_reg=Reg()   

            re_pass=""
            password="Prox" # placeholder

            # checking if both passwords are the same
            while(not re_pass==password):    

                        # new password
                        password=maskpass.askpass(prompt="Please provide a password : ")
                        # password= input("Please provide a password : ")

                        # re-enter password 
                        re_pass=maskpass.askpass(prompt="Please re-enter the passsword : ")
                        # re_pass = input("Please re-enter the passsword : ") 

                        while(len(password)<5):
                            print("Password must be atleast 5 characters long")
                            
                            # new password
                            password=maskpass.askpass(prompt="Please provide a password : ")
                            # password= input("Please provide a password : ")

                            # re-enter password 
                            re_pass=maskpass.askpass(prompt="Please re-enter the passsword : ")
                            # re_pass = input("Please re-enter the passsword : ") 

        

            passw = password.encode("utf-8")

            encoded = base64.b64encode(passw)
            
          
            user_reg.e_insert(email,username,encoded)
            print("Sign in succesful!")             