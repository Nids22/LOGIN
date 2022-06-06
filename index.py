from login import User
from reg import Reg
from mydb2 import Db
from new_user import NewUser
import bcrypt
import maskpass

if __name__ == '__main__':
    user_acc = User()
    user_reg=Reg()
    user_data=Db()
    new_user=NewUser()

    print("Do you have an account ?")

    exists = input("Answer Y or N : ")

    if exists=="Y" or exists=="y":
        username = input("Please provide a username : ") 

        account="N"

        # wrong username
        while ((not user_acc.check_username(username)) and account=="N"):
        # while account=="N":
            # print(user_acc.check_username(username))
            print("Username does not exist")
            print("Create account ? ")
            account=input("Please type Y or N : ")

            if account=="N":
                # try username again
             username = input("Please provide a username : ") 
             
            else:
                # new user registration
                # user_reg
                
                account="Z"

                new_user.create_user()

        if account=="N": 
            # check old password
            # password = input("Please provide a password : ") 
            password=maskpass.askpass(prompt="Please provide a password : ")
            
            # To check whether the password is correct or whether another account needs to be created
            while not user_acc.check_pass(username,password) and account=="N":

                print("Incorrect Password...")
                print("Change Password ? ")
                pass_account=input("Please type Y or N : ")


                # User wants to change the password
                if pass_account=="Y" or pass_account=="y":

                    # input email used with the account
                    email= input("Please provide the email that this account is registered with : ")

                    while(not user_acc.check_email(username,email)):
                        print("Incorrect email registered with account")
                        print("Create new account ? ")
                        account=input("Please type Y or N : ")

                        if(account=="Y" or account=="y"):
                            new_user.create_user()
                        else:    
                         email= input("Please provide the email that this account is registered with : ")


                    new_pass=""
                    con_pass="placeholder"

                    #input new password
                    while(not new_pass==con_pass):
                        new_pass=maskpass.askpass(prompt="Please provide a new password : ")
                        con_pass=maskpass.askpass(prompt="Please re-enter your new password : ")

                        while(len(new_pass)<5):
                            print("Password must be atleast 5 characters long")
                            
                            # new password
                            new_pass=maskpass.askpass(prompt="Please provide a new password : ")
                            # password= input("Please provide a password : ")

                            # re-enter password 
                            con_pass=maskpass.askpass(prompt="Please re-enter the new passsword : ")
                            # re_pass = input("Please re-enter the passsword : ") 

                    user_acc.change_pass(username,email,new_pass)
                    password=new_pass
                    
                # password = input("Please provide a password : ")
                else:
                    password=maskpass.askpass(prompt="Please provide a password : ")

            print("Log in successful!")    

    else:
        new_user.create_user()          