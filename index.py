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
                print("Create account ? ")
                account=input("Please type Y or N : ")

                if account=="Y" or account=="y":
                    new_user.create_user()
                # password = input("Please provide a password : ")
                else:
                    password=maskpass.askpass(prompt="Please provide a password : ")

            print("Log in successful!")    

    else:
        new_user.create_user()          