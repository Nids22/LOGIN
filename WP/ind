from login import User
from reg import Reg
from mydb2 import Db

if __name__ == '__main__':
    user_acc = User()
    user_reg=Reg()
    user_data=Db()

    print("Do you have an account  ?")

    exists = input("Answer Y or N...")

    if exists=="Y":
        username = input("Please provide a username : ") 

        account="N"

        #wrong username
        while ((not user_acc.check_username(username)) and account=="N"):
        # while account=="N":
            # print(user_acc.check_username(username))
            print("Username does not exist")
            print("Create account ? ")
            account=input("Please type Y or N : ")

            if account=="N":
                #try username again
             username = input(" Please provide a username : ") 
            else:
                #new user registration
                # user_reg
                print(1234)
                account="Z"

                #new username input
                username = input(" Please provide a username : ") 
                
                #used username
                while user_reg.user_check(username) :
                    print("Username not available")
                    username = input(" Please provide a username : ") 

                #new email input
                email= input("Please provide an email : ")  

                #used email
                while user_reg.email_check(email):
                    print("Email already in use")
                    email= input("Please provide an email : ")  
                      
                #new password
                password = input("Please provide a password : ")
                #re-enter password 
                re_pass = input("Please re-enter the passsword : ") 

                if(re_pass==password):
                 user_reg.e_insert(email,username,password)
                 print("Sign in succesful!")  

        if account=="N": 
            #check old password
            password = input("Please provide a password : ") 
            
            while not user_acc.check_pass(username,password):

                password = input("Please provide a password : ")

            print("Log in successful!")    

    else:
        #new username input
                username = input(" Please provide a username : ") 
                
                #used username
                while user_reg.user_check(username) :
                    print("Username not available")
                    username = input(" Please provide a username : ") 

                #new email input
                email= input("Please provide an email : ")  

                #used email
                while user_reg.email_check(email):
                    print("Email already in use")
                    email= input("Please provide an email : ")  
                      
                #new password
                password = input("Please provide a password : ")
                #re-enter password 
                re_pass = input("Please re-enter the passsword : ") 

                if(re_pass==password):
                 user_reg.e_insert(email,username,password)
                 print("Sign in succesful!")          


        







    



