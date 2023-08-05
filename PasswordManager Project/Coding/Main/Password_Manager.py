"___________________________ Importing ___________________________________"


# Import All neded variable's and exponent's from The Database.
from Database.Data import *


"__________________________________________________________________________"


# Define a function That will make the starting Operation Of the app.
def starting():


    "---------------------------- Loading Look --------------------------------"


    # Call the function Loading Look , One of the Database Made function's that will make The Code Look like a loading screen
    loading()


    "--------------------------------------------------------------------------"


    "---------------------------- welcoming -----------------------------------"


    print(F"Welcome to KhodeDan Password Manager version : \33[31m{version}\33[34m")
    sleep(4)


    "--------------------------- welcoming ------------------------------------"






"------------------------- UserName collecting Function(Start) ----------------------------"


# Define a function Called Welcoming , Which Have the Order Of initializing the start of the code.
def Collect_UserName():


    "--------------- Loop Variables ----------------"
    LOOP1 = True     # Define a variable with the value of True , Which Later act's as a flag variable.
    LOOP2 = True     # Define a variable with the value of True , Which Later act's as a flag variable.
 
    UserName_Yes_No = None   # Define a variable Called UserName_Yes_no with NoneType value , Which later act's as a variable for asking the user If theirre sure about their entry. 
    "-----------------------------------------------"


    clean()  # Clean Is a replacement function for os.system('cls')


    sleep(4)


    # Start a while loop that will be repeted to CONFIRM or DECLINE the user entry.
    while LOOP1:
        

        clean()


        # Make an If statement In order to break the loop and finish the program If needed.
        if LOOP1 == False:
            break

        
        print('')
        print("Note That \33[31mUsername's\33[34m can only contain \33[31mUppercase\33[34m , \33[31mLowerCase Letters\33[34m , \33[31mNumber's \33[34m")
        global Inputted_Username
        Inputted_Username = input("Please Chose a \33[31muserName\33[34m For Your \33[31maccount\33[34m : ")


        
        if isusername(Inputted_Username) and Inputted_Username not in Users_Info["Users"].keys():

            sleep(1)


            clean()


            # Start A while loop In order to repeat the Asking operation.
            while LOOP2:


                clean()


                # Define and if statement to make sure the loop will break Once the Flag variable Is set to False.
                if LOOP2 == False:


                    break


                UserName_Yes_No = input(F"Are You sure you want \33[31m{Inputted_Username}\33[34m As your \33[31maccount userName\33[34m? (Answer With \33[31myes\33[34m or \33[31mno\33[34m only)  : ")
                UserName_Yes_No = UserName_Yes_No.lower() ; UserName_Yes_No = UserName_Yes_No.strip()
                # Turn all the letter's in The user entry to lowerCase and delete all spaces , In order to make the recognizing Easier.


                if UserName_Yes_No == "yes":


                    clean()


                    Users_Info["Users"][Inputted_Username] = {}


                    print(F"\33[31m{Inputted_Username}\33[34m Has been chosen as your \33[31musername\33[34m.")
                    sleep(3)
 


                    # Set All loop variables to false , In order to finish the welcoming Program.
                    LOOP1 = False
                    LOOP2 = False
                    break


                elif UserName_Yes_No == "no":


                    clean()


                    print("\33[31mReturning to the login Panel\33[34m")
                    sleep(3)
                    break


                else:


                    clean()
                    print("That Is not a \33[31myes\33[34m or \33[31mno \33[34m, Please try again.")
                    sleep(3)
        

        elif Inputted_Username in Users_Info["Users"].keys():


            clean()


            print("This \33[31m UserName \33[34m Allready Exist's , Please try another UserName")


            input("\33[31mPress any key to continue.\33[34m")


            continue


        else:


            clean()


            print("\33[31This username does not meet the requirement's to be used.\33[34m \n\
                  Please note that usernames : \n \
                  1. Should Not be less than 3 characters .\n \
                  2. Should Not be more than 13 characters.\n \
                  3. Should Not be number's only.\n \
                  4. Usernames can only contain Uppercase And Lowercase letters , Numbers.  ")         
            input("\33[31mPress any key to try again\33[34m")


"------------------------------ UserName Taking Function(END) -------------------------------"


"-----------------------------  MasterPassword Taking function(Start) ---------------------------"


# Define a function called collect_user_info , Which will collect the BirthTime of the user for the recovery operation and will collect a MasterPassword.
def collect_MasterPassword():
    "--------------------- Needed variables -------------------"
    global Inputted_MasterPassword   # Turn the Inputted_MasterPassword Variable to a global variable.
    Inputted_MasterPassword = None   # define a variable with the value of None which later will be user for collecting the user MasterPassword Entry.
    MasterPassword_Add_Retry = ""  # Define a variable with the value of "" string which Later will be user for asking the user wether they are sure abou their masterpassword entry ot not.
    LOOP1 = True     # Define a variable with the bool (True) Value In order to use as a FLAG variable in the looping Operation.
    LOOP2 = True    # Define a variable with the bool (True) Value In order to use as a flag variable for the loop operation.
    LOOP3 = True     # Define a variable with the bool (True) Value In order to use as a flag variable for the loop operation .
    "--------------------- Needed variables -------------------"


    clean()


    # This Part of the code have been initialized In a while loop In order to avoid Upcoming Errors , DO NOT REMOVE THE WHILE LOOP.
    while LOOP1 == True:


        clean()


        if LOOP1 == False:
            break


        print("This Is the part where you should chose a \33[31mMasterPassword\33[34m.")
        print("This \33[31mMasterPassword\33[34m will be used for accessing your \33[31maccount.\33[34m")
        print("Do not share It with anyone.")
        input("\33[31mPress any key to contoniue.\33[34m")


        LOOP1 = False
        break


    # Define a while loop in Order to loop through the password Choosing Operation.
    while LOOP2 == True:


        clean()  


        # Define the loop breaker if statement of the operation. (Flag Variable)
        if LOOP2 == False:
            break


        print("The \33[31mMasterPassword\33[34m at least Must have \33[31m1 Upper Case letter \33[34m, \33[31m1 LowerCase Lettter \33[34m, And at least \33[31mA number.\33[34m")
        Inputted_MasterPassword = input(F"Please Chose a \33[31mMasterPassword\33[34m for the account \33[31m{Inputted_Username}\33[34m : ")
        Inputted_MasterPassword = Inputted_MasterPassword.strip()  # Delete all spaces from the user inputted masterpassword.


        if ismasterpassword(Inputted_MasterPassword):


            # Start a while loop In order to ask the user if their sure about their Inputted MasterPassword.
            while LOOP3:


                clean()
                

                # Define the loop breaker If statement. (Flag variable)
                if LOOP3 == False:
                    break

                
                print("Answer with \33[31myes\33[34m or \33[31mno\33[34m only.")
                MasterPassword_Add_Retry = input(F"Are You sure you want \33[31m{Inputted_MasterPassword}\33[34m As Your \33[31mMasterPassword \33[34m? : ")
                MasterPassword_Add_Retry = MasterPassword_Add_Retry.lower() ; MasterPassword_Add_Retry = MasterPassword_Add_Retry.strip()
                # Turn the first lettter of the entry to uppercase , And delete all spaces from the left and right side.


                # Define an if statement , If the User Is sure about their decision , The MasterPassword Will be On their Username.
                if MasterPassword_Add_Retry == "yes".lower():


                    clean()


                    Users_Info["Users"][Inputted_Username] = {}
                    Users_Info["Users"][Inputted_Username]["MasterPassword"] = Inputted_MasterPassword
                    Users_Info["Users"][Inputted_Username]["PassWords"] = {}

                    clean()


                    print(F"\33[31m{Inputted_MasterPassword}\33[34m Has Been chosen as your \33[31mMasterPassword\33[34m")
                    sleep(3)
                    clean()
                    LOOP1 = False ; LOOP2 = False ; LOOP3 = False 
                    break


                # Define an if statement , If the user Change their mind about the Passsword , They will be returned to the password Choosing menu.
                elif MasterPassword_Add_Retry == "no".lower():
                    clean()
                    print("\33[31mReturning to the PassWord Choosing Menu...\33[34m")
                    sleep(3)
                    break

        
        else:


            clean()


            print("\33[34m A Master Password should : \33[31m")
            print(F"{TABS} Contain At Least 1 LowerCase Letter")
            print(F"{TABS} Contain At Least 1 UpperCase Letter")
            print(F"{TABS} Contain At Least 1 Number")
            print(F"{TABS} Contain At Least 5 characters")
            print(F"{TABS} Should Not be longer than 20 characters")
            print("")


            sleep(3)


            input("\33[34mPress any key to continue.")                


            



"---------------------------- MasterPassword Taking Function(End) -----------------------"


"---------------------------- BirthDate taking Function(Start) --------------------------"


# Define a Function that will ask the user if they want to add their birthday or not , And Will append the birthdate to the account Information If added.
def Collect_BirthDate():
    "----------------------- Needed Variables -----------------------"
    BirthDate_Add_Pass = None    # Define a variable with the NoneType value Which will be used to ask the user if they want to add their birthdate or not.
    Birth_Day = None     # Define a variable with the the NoneType value which will be used As the day of the user birth.
    Birth_Month = None   # Define a variable with the NoneType value which will be used as the month of the user birth.
    Birth_Year = None    # Define a variable with the NoneType value which will be used as the year of the user birth
    Birth_Date = None    # Define a variable with the NoneType value which will be used as the full birthdate (YY/MMM/DD)
    Date_Yes_No = None   # Define variable with the NoneType value which will be used as the input variable to make sure if the user accept the date as their birthdate.
    LOOP1 = True     # Define a variable with the  bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP2 = True     # Define a variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP3 = True     # Define a variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP4 = True     # Define a variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP5 = True     # Define a variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    "----------------------- Needed Variables -----------------------"


    clean()

    
    print("Now that you have a \33[31mMasterPassword\33[34m , You need a way for \33[31mrecovering\33[34m It If needed.")
    print("In this case , You can add your \33[31mBirthDate\33[34m for the \33[31mrecovery Operation.\33[34m")
    input("Press any key to continue.")


    # Start A While loop In order to ask the user If they want to add their birthdate or not.
    while LOOP1 == True:


        LOOP1 = True

    
        clean()
        print("Answer with \33[31mYes \33[34mor \33[31mno \33[34monly.")
        BirthDate_Add_Pass = input("Would You like to Add your \33[31mbirthdate\33[34m for the \33[31mrecovery Operation\33[34m? : ")
        BirthDate_Add_Pass = BirthDate_Add_Pass.lower() ; BirthDate_Add_Pass.strip()
        # Turn all the letter's in the User entry to LowerCase , Delete All spaces at the left and right side.


        if BirthDate_Add_Pass == "yes":


            LOOP2 = True


            while LOOP2 == True:


                clean()


                if LOOP2 == False:
                    break


                try:
                    Birth_Day = int(input("Please enter the \33[31mday\33[34m you were born (\33[31m1 To 31\33[34m) : "))
                

                except:
                    clean()
                    continue
                

                if isbirthday(Birth_Day):


                    while LOOP3 == True:


                        LOOP3 = True


                        clean()


                        if LOOP3 == False:
                            break


                        try:


                            Birth_Month = int(input("Please enter your \33[31mBirthMonth\33[34m (\33[31m1 To 12)\33[34m : "))



                                

                        except:
                                    

                            clean()


                            continue


                        if isbirthmonth(Birth_Month):


                            LOOP4 = True


                            while LOOP4 == True:


                                clean()


                                if LOOP4 == False:
                                    break


                                try:


                                    Birth_Year = int(input("Please enter the \33[31myear\33[34m you've been born (\33[31m1923 TO 2022)\33[34m : "))


                                    if isbirthyear(Birth_Year):


                                        LOOP5 = True


                                        clean()


                                        while LOOP5 == True:


                                            clean()


                                            if LOOP5 == False:
                                                break


                                            Birth_Date = F"{Birth_Day}/{Birth_Month}/{Birth_Year}"


                                            print("Answer with \33[31myes \33[34mor \33[31mno only.\33[34m")
                                            Date_Yes_No = input(F"Are You sure You accept This \33[31mdate\33[34m as your \33[31mbirthdate\33[34m : \33[31m{Birth_Date}\33[34m : ")

                                            Date_Yes_No = Date_Yes_No.lower() 
                                            Date_Yes_No = Date_Yes_No.strip()


                                            if Date_Yes_No == "yes":


                                                clean()


                                                Users_Info["Users"][Inputted_Username]["Birth_Date"] = Birth_Date
                                                

                                                print(F"\33[31m{Birth_Date}\33[34m Has Been Chosen as your \33[31maccount Birthday.\33[34m")
                                                print("Diverting to the main menu.")
                                                sleep(3)


                                                LOOP1 = False
                                                LOOP2 = False
                                                LOOP3 = False
                                                LOOP4 = False
                                                LOOP5 = False
                                            

                                            elif Date_Yes_No == "no":


                                                clean()
                                                print("\33[31m Returning...")


                                                LOOP5 = False
                                                LOOP4 = False
                                                LOOP3 = False
                                                LOOP2 = False
                                        







                                except:


                                    clean()
                                    continue


        elif BirthDate_Add_Pass == "no":
            

            clean()
            

            print("\33[31mDiverting to the menu...\33[34m")
            

            sleep(3)


            LOOP1 = False


"---------------------------- BirthDate Taking function (End)--------------------"


"------------------------------ Main Menu function (Start) ----------------------"


# Define a function Named Main Menu , Which Act's as the main menu of the password manager , Containing All the operation's the user can use.
def Main_Menu():
    "-------------------------- Needed Variables ------------------------"
    LOOP1 = True     # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP2 = True     # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP3 = True     # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP4 = True     # Define A bool (True) Variable In order to ube used as FLAG variable in the looping operation.
    LOOP5 = True     # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP6 = True     # Define A variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP7 = True     # Define A variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP8 = True     # Define A variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP9 = True     # Define A bool (True) Variable In order to be used as FLAG varibale in the forgot Password Operation Looping.
    LOOP10 = True    # Define A bool (True) Variable In order to use in the Change User Operation.
    LOOP11 = True    # Define A bool (True) Variable In order to use in the Change User Operation.
    LOOP12 = True    # Define A bool (True) Variable In order to use in the Add user Operation.
    LOOP13 = True    # Flag variable for looping in Delete User.
    masterpassword_input = ""    # Input container for the delete user Operation.
    user_confirmation = ""   # Input Container for the delete user Operation.
    adduser_operation_assurance = ""     # Define A variable with the value of str ("") In order to be used as user Input in the adding user operation , Asking the user if they are sure about Addind A New account or not.
    users_count = len(Users_Info["Users"])   # Define a variable Which keeps the lenght of the Users count as variable.
    changeuser_MasterPassword_Inbox = ""     # Define a variable with the value of str ("") In order to be used as MasterPassword Input in change user Operation.
    ForgotOperation_NewMasterPassword_inbox = ""     # Define A variable with the value of str ("") In order to be used as the NewMasterPassword Input in the forgot Password Operation
    ForgotOperation_BirthDate = ""   # Define A variable with the value of str ("") In order to be used in creating the new BirthDate in the forgot MasterPassword Operation.
    BirthDate_Check = ""  # Define A variable with the value of str ("") In order to be used to check If the user have a existing Birth_Date in their Info or not To be used in the forgot MasterPassword Operation
    Birth_Day_Inbox = ""     # Define A str ("") Variable In order to be used as BirthDay Input identifier In the forgot MasterPassword Operation.
    Birth_Month_Inbox = ""   # Define A str ("") Variable In order to be used as BirthMonth Input Identifier In the forgot MasterPassword Operation.
    Birth_Year_Inbox = ""    # Define A str("") Variable in order to be used as BirthYear Input Identifier In the forgot MasterPassword Operation.
    Current_MasterPassword = Users_Info["Users"][Inputted_Username]["MasterPassword"]    # Define a variable with the value of The user Current MasterPassword (Titled) , In order to be used in the MasterPassword Concerned Operation's.
    User_Desired_Operation = ""    # Define A str ("") Value Variable in Order to be used as the User Input storing Variable , In order to understand what operation they want to use.\
    MasterPassword_Inbox = ""    # Define A str ("") Value variable In order to use as an input , In the changing MasterPassword Operation.
    New_MasterPassword_Inbox = ""    # Define A str ("") Value Variable In order to use as an input , In the changing MasterPassword Operation.
    PassWord_Title = ""  # Define A str ("") Value variable , In order to keep the name of the password.
    Desired_PassWord = ""    # Define A str ("") Value variable in Order to store the password that the user want's to add in the Add_Password.\
    Want_To_Remove = ""     # Define A str("") Value Variable in Order to store the password that Is going to be deleted.
    PassWords = "PassWords"  # Define A str ("PassWords") Value variable in Order to use in A F string print (In order to avoid quotation mark.)
    Number = 1   # Define A int (1) Value variable In order to use as numbering in the loop.
    "--------------------------------------------------------------------"


    # Start a while Loop With the condition Of the first FLAG variable to be True , In order to LOOP through the menu and It's option's.
    while LOOP1 == True:


        # Note : This Variable Is setted here for ordinary Update , Do Not remove it.
        users_count = len(Users_Info["Users"])   # Define a variable Which keeps the lenght of the Users count as variable.

                
        clean()


        # Define an If statement , If the First Flag Variable
        if LOOP1 == False:
            break


        print("\33[31m_____________________________________________________\33[34m")
        print(F"Logged Into Account \33[31m ⁛  {Inputted_Username} ⁛")
        print("\33[31m_____________________________________________________\33[34m")


        print("")


        print("Here are all the avaliable operation codeNames : ")


        print("")
         

        for codename,operation in Operations.items():


            print(F"\33[31m{codename} . \33[34m{operation}")





        print("\33[31m---------------------- User Management -----------------------------\33[34m")


        print("")


        for user_operation_number , user_management_operation in user_management_operations.items():


            print(F"\33[31m{user_operation_number} . \33[34m{user_management_operation}")
        

        print("")


        User_Desired_Operation = input("Enter the desired \33[31mOperation CodeName\33[34m : ")

        if User_Desired_Operation.isdigit():


            User_Desired_Operation = int(User_Desired_Operation)
            

        else:


            clean()


            print("That Is not a \33[31mknown Operation Code name\33[34m.")
            print("\33[31mPlease try again\33[34m.")


            sleep(3)
        

        # VIEW PASSWORD.
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 1]:
    
    
            if len(Users_Info["Users"][Inputted_Username]["PassWords"]) == 0:
    
    
                clean()
    
    
                print(F"You currently Have \33[31mno Password's\33[34m stored . You can store \33[31mpassword's\33[34m in the password \33[31madding\33[34m menu.")
                print("Returning to the main menu")
    
    
                sleep(5)
    
    
                continue
    
    
            else:
    
    
                clean()
                    
    
                print("Here Are all the \33[31mPassword's\33[34m You've stored : ")
                print("")


                Number = 1


                for PassWord,Title in Users_Info["Users"][Inputted_Username]["PassWords"].items():
                            
                        
                    print(F"{Number} . {PassWord} : {Title}")
                    print('')


                    Number = Number + 1


                print("")
                input("\33[31mPress any key to return to the main menu\33[34m.")
    
    
        # ADD PASSWORD.
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 2]:
    
    
            LOOP2 = True
    
    
            while LOOP2 == True:
                        
    
                clean()
    
    
                if LOOP2 == False:
                    break
    
    
                Desired_PassWord = str(input("Please \33[31menter\33[34m the \33[31mPassword\33[34m you would like to add : "))

                clean()


                PassWord_Title = str(input("Now Please enter the \33[31mtitle\33[34m you want to specify the \33[31mpassword\33[34m : "))


                clean()


                # This If statement will check ( If the Entered password Is not an empty string and if the entered Password Allready Don't exist in the User passwords )
                if ispassword(Desired_PassWord) and PassWord_Title not in Users_Info["Users"][Inputted_Username]["PassWords"].values():
    
    
                    Users_Info["Users"][Inputted_Username]["PassWords"][Desired_PassWord] = PassWord_Title
    
    
                    print(F" \33[31m{Desired_PassWord}\33[34m Has been added to your password's list as \33[31m{PassWord_Title}\33[34m")
                    print("Diverting to the main menu.")
    
    
                    sleep(5)


                    LOOP2 = False

                
                elif PassWord_Title in Users_Info["Users"][Inputted_Username]["PassWords"].values():


                    clean()
                    print("\33[31m That PassWord title allready exists in your password's List , Please assign a new one.\33[34m")
                    sleep(4)
                

                elif Desired_PassWord in Users_Info["Users"][Inputted_Username]["PassWords"].keys():


                    clean()
                    print("\33[31m That Password Allready exist in your password list , Please add a unique one.")
                    sleep(4)
                    clean()

                    continue
        

        # REMOVE-DELETE PASSWORD.
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 3]:


            LOOP3 = True


            while LOOP3:


                if LOOP3 == False:
                    break


                clean()


                if len(Users_Info["Users"][Inputted_Username][PassWords]) == 0:


                    print("You currently Have no \33[31mPassword\33[34m Stored , You can add password's using the \33[31mAdd\33[34m Password Option In the menu.")
                    print("Diverting Back to the menu...")


                    sleep(4)


                    clean()


                    LOOP3 = False

                
                else:


                    Number = 1


                    for PassWord,PassWord_Title in Users_Info["Users"][Inputted_Username][PassWords].items():


                        print(F"\33[31m{Number}\33[34m . \33[31m{PassWord}\33[34m : {PassWord_Title}")
                        print("")


                        Number = Number + 1


                    print("\33[34m Remember You can type in \33[31mQuit\33[34m Anytime you would like to \33[31mexit\33[34m and return to the main menu.\33[34m")
                    print("Type in the \33[31mPassWord title \33[34m  Only .")
                    Want_To_Remove = input("Which One of theese Password's Would you like to \33[31mdelete\33[34m? : ")


                    if Want_To_Remove in [password_title for password_title in Users_Info["Users"][Inputted_Username]["PassWords"].values() if Want_To_Remove == password_title]:


                        clean()

                        try:


                            del Users_Info["Users"][Inputted_Username]["PassWords"][get_key_by_value(Users_Info , Want_To_Remove)]

                
                            print(F"\33[31m{PassWord_Title}\33[34m has been deleted.")


                            sleep(4)


                            LOOP3 = False
                        

                        except:


                            clean()


                            continue
                        

                    elif Want_To_Remove in QUIT_LETTERCASE:


                        clean()


                        print("\33[31m Diverting back to the menu...\33[34m")


                        sleep(4)


                        clean()


                        LOOP3 = False
                    

                    else:


                        clean()
                        print("The \33[31m The Chosen Password Does Not exist. Please try again.\33[34m")
                        sleep(4)
                        clean()


                        continue


        # CHANGE MASTERPASSWORD
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 4]:


            while LOOP4 == True:


                if LOOP4 == False:
                    break


                clean()


                print("Change \33[31mMasterPassWord Menu\33[34m :")
                print("")
                print("1. Remember You can Insert \33[31mquit\33[34m For returning to the main menu If you changed your mind.")


                MasterPassword_Inbox = input("Please enter your Current \33[31mMasterPassword\33[34m to Resume : ")
                MasterPassword_Inbox = MasterPassword_Inbox.strip()


                if MasterPassword_Inbox == Current_MasterPassword:


                    clean()

                    
                    print("Access granted.")

                    
                    sleep(3)

                    
                    LOOP4 = False


                    LOOP5 = True


                    while LOOP5 == True:


                        clean()

                        print("Remember that If you changed your mind , You can type in \33[31mquit\33[34m for returning to the main menu")
                        print("The Inserted \33[31mMasterPassword\33[34m Must Contain At least \33[31m1 UpperCase\33[34m , \33[31mLowerCase Letter\33[34m , And A \33[31mNumbe3\33[34m.")
                        print("")
                        New_MasterPassword_Inbox = input("Please type In your new MasterPassword : ")
                        New_MasterPassword_Inbox.strip()


                        if ismasterpassword(New_MasterPassword_Inbox):


                            try:

                                Users_Info["Users"][Inputted_Username]["MasterPassword"] = New_MasterPassword_Inbox


                                # Change the current password variable In order to avoid Upcoming Error's everytime the operation Rerun's.
                                Current_MasterPassword = Users_Info["Users"][Inputted_Username]["MasterPassword"]


                                clean()


                                print(F"\33[31m{New_MasterPassword_Inbox}\33[34m Has been set as your \33[31mMasterPassword\33[34m.")


                                sleep(2)


                                print("Diverting to the main menu...")


                                sleep(3)


                                LOOP5 = False


                            except:


                                print("The Operation was \33[31munsuccesfull\33[34m , \33[31mPlease try again Later.\33[34m")


                                LOOP5 = False
                        

                        # Checks if the user Typed in any form of the word "QUIT"
                        elif New_MasterPassword_Inbox in QUIT_LETTERCASE:


                            clean()


                            sleep(1)


                            print("Returning to the main menu...")


                            sleep(3)


                            LOOP5 = False

                        

                        else:


                            clean()


                            print("The entry Cannot be accepted as A \33[31mMasterPassword\33[34m ,\33[31m Please try again.")


                            sleep(3)


                            continue



                elif MasterPassword_Inbox in QUIT_LETTERCASE:


                    clean()


                    print("The Operation Has been \33[31mCancelled\33[34m.")


                    sleep(2)


                    print("Diverting to the main menu...")


                    sleep(3)


                    break


                else:


                    clean()
                    sleep(2)


                    print("\33[31mAccess Denied.\33[34m")


                    sleep(2)


                    continue

        
        # FORGOT MasterPassword.
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 5]:


            BirthDate_Check = Users_Info['Users'][Inputted_Username].get('Birth_Date' , False)


            if BirthDate_Check != False:


                LOOP6 = True
            

            else:


                clean()

                
                sleep(1)


                print("")


                print("You Have not added Your \33[31mbirthday\33[34m to your \33[31maccount\33[34, , You can't \33[31mrecover\33[34m your \33[31mMasterPassword\33[34m .")


                sleep(5)


                LOOP6 = False


                continue

            
            while LOOP6 == True:


                clean()

                
                print("Remember You can type in \33[31mQUIT\33[34m Anytime you have changed your mind.")


                print("Right Now , There Is only \33[31mone solution\33[34m for the \33[31mPassword Recovery\33[34m Operation.")


                sleep(2)


                print("")





                Birth_Day_Inbox = input("Please Type In your \33[31mBirth Day\33[34m (\33[31m1 TO 31\33[34m) : ")


                if Birth_Day_Inbox in QUIT_LETTERCASE:


                    break


                if Birth_Day_Inbox.isdigit():


                    Birth_Day_Inbox = int(Birth_Day_Inbox)

                

                else:


                    clean()


                    print("The entry Is not a \33[31mnumber\33[34m ,\33[341m Please try again\33[34m.")


                    sleep(2)


                    continue


                if isbirthday(Birth_Day_Inbox):


                    LOOP7 = True


                    while LOOP7 == True:


                        clean()


                        


                        print("Remember You can type in \33[31mQUIT\33[34m , for returning to the main menu.")


                        Birth_Month_Inbox = input("Now Please Type in the \33[31mmonth\33[34m you were born (\33[31m1 to 12\33[34m) :  ")


                        if Birth_Month_Inbox in QUIT_LETTERCASE:


                            LOOP7 = False
                            LOOP6 = False
                            

                        elif Birth_Month_Inbox.isdigit():


                            Birth_Month_Inbox = int(Birth_Month_Inbox)


                            if isbirthmonth(Birth_Month_Inbox):


                                LOOP8 = True


                                while LOOP8 == True:


                                    clean()

                                        
                                    Birth_Year_Inbox = input("At Last , Please type in the \33[31myear\33[34m you were born (\33[31m1923 , 2022\33[34m) : ")


                                    if Birth_Year_Inbox in QUIT_LETTERCASE:


                                        LOOP6 = False
                                        LOOP7 = False
                                        LOOP8 = False


                                        break


                                    if Birth_Year_Inbox.isdigit():


                                        Birth_Year_Inbox = int(Birth_Year_Inbox)

                                            
                                        if isbirthyear(Birth_Year_Inbox):


                                            ForgotOperation_BirthDate = F"{Birth_Day_Inbox}/{Birth_Month_Inbox}/{Birth_Year_Inbox}"


                                            if ForgotOperation_BirthDate == Users_Info['Users'][Inputted_Username]['Birth_Date']:


                                                LOOP9 = True


                                                while LOOP9 == True:


                                                    clean()


                                                    print("Now , You should enter the \33[31mnew MasterPassword\33[34m you would like.")
                                                    print("")
                                                    print("\33[31mMasterPassword\33[34m Must have at \33[31mleast 1 Upper case and lowerCase letter\33[34m , \33[31m1 Number\33[34m , \33[31Shouldn't be less than 5 characters\33[34m.")


                                                    ForgotOperation_NewMasterPassword_inbox = input("Please enter the \33[31mnew MasterPassword\33[34m : ")
                                                    ForgotOperation_NewMasterPassword_inbox = ForgotOperation_NewMasterPassword_inbox.strip()


                                                    if ismasterpassword(ForgotOperation_NewMasterPassword_inbox):


                                                        ForgotOperation_NewMasterPassword_inbox = Users_Info['Users'][Inputted_Username]['MasterPassword'] 


                                                        print(F"\33[31m{ForgotOperation_NewMasterPassword_inbox}\33[34m Has been chosen as your \33[31mnew MasterPassword.\33[34m")


                                                        sleep(4)


                                                        LOOP9 = False
                                                        LOOP8 = False
                                                        LOOP7 = False
                                                        LOOP6 = False
                                                    

                                                    else:


                                                        clean()


                                                        print("Remember that the \33[31mMasterPassword\33[4m should have at least \33[31,1 uppercae letter\33[34m , \33[31m1 LowerCase letter\33[34m , And \33[31m1 number\33[34m.")


                                                        print("\33[31mThat Is not a 31mMasterPassword , Please try again.\33[34m")


                                                        sleep(4)


                                            else:


                                                clean()


                                                print("\33[31mAccess denied , Returning to the menu.\33[34m")


                                                LOOP6 = False
                                                LOOP7 = False
                                                LOOP8 = False


                                        else:


                                            clean()


                                            print("The Inserted Content is not a \33[31mBirthYear\33[34m , Please try again.")


                                            sleep(4)

                                    
                                    else:

                                        clean()


                                        print("The inserted content Is not a \33[31mNumber\33[34m , Please try again.")


                                        sleep(4)
                                        
                                
                            else:


                                clean()


                                print("The entry Is not a \33[31mbirthmonth\33[34m , Please try again.")


                                sleep(4)


                        else:


                            clean()


                            print("The entry Is not a \33[31mNumber\33[34m , Please try again.")


                            sleep(4)
                        

                else:


                    clean()


                    print(" The Inserted Number Is not a \33[31mBirthDay\33[34m , \33[31mPlease try again\33[34m.")


                    sleep(4)
        

        # CHANGE USER.
        if User_Desired_Operation in [Number for Number in user_management_operations.keys() if Number == 7]:


            if users_count == 1:


                clean()

                
                print("You Have no other \33[31maccount's\33[34m , You can add Other Account's using \33[31madd user button\33[34m in the menu.")

                
                sleep(4)


                clean()


            else:


                LOOP10 = True


                while LOOP10 == True:


                    clean()


                    print("\33[31mHere are all the avaliable accounts : \33[34m")


                    print("")


                    for user in Users_Info["Users"]:


                        print(F"⁛  {user} ⁛")
                        

                        print("")

                    
                    sleep(1)


                    print("Remember you can type in \33[31mquit\33[34m for returning to the main menu , Anytime you desire.")


                    changeuser_username_Inbox = input("Which one of the \33[31maccount's\33[34m would you like to Login ? (\33[31mAccount Name\33[34m): \33[0m")
                    changeuser_username_Inbox = changeuser_username_Inbox.strip()


                    if changeuser_username_Inbox in [user for user in Users_Info["Users"] if changeuser_username_Inbox == user] and changeuser_username_Inbox != Inputted_Username:


                        clean()


                        LOOP11 = True


                        while LOOP11 == True:


                            clean()


                            changeuser_MasterPassword_Inbox = input(F"\33[34mPlease enter the \33[31m MasterPassword\33[34m For the account \33[31m{changeuser_username_Inbox}\33[0m : ")
                            changeuser_MasterPassword_Inbox = changeuser_MasterPassword_Inbox.strip()


                            if changeuser_MasterPassword_Inbox == Users_Info["Users"][changeuser_username_Inbox]["MasterPassword"]:


                                clean()


                                print(F"\33[34m Successfully Logged Into account \33[31m{changeuser_username_Inbox}\33[34m")


                                Inputted_Username == changeuser_username_Inbox


                                sleep(5)


                                LOOP10 = False
                                LOOP11 = False
                            

                            elif changeuser_MasterPassword_Inbox in [quit_type for quit_type in QUIT_LETTERCASE if changeuser_MasterPassword_Inbox == quit_type]:


                                clean()


                                print("\33[31mQuitting to the main menu.\33[34m")


                                LOOP10 = False
                                LOOP11 = False
                            

                            else:


                                clean()


                                print("\33[31mAccess denied.\33[34m")


                                sleep(3)


                                LOOP11 = False


                    elif changeuser_username_Inbox in [quit_type for quit_type in QUIT_LETTERCASE if changeuser_username_Inbox == quit_type]:


                        clean()


                        print("\33[31mQuiting to the main menu.\33[34m")


                        sleep(2)


                        LOOP10 = False
                    


                    elif changeuser_username_Inbox == Inputted_Username:


                        clean()


                        print(F"\33[31mYou are allready Logged Into account \33[31m{changeuser_username_Inbox} \33[34m")

                        
                        sleep(4)


                        clean()
                    

                    else:


                        clean()


                        print("\33[31mThat Account UserName does not exist , try again.\33[34m")


                        print("")


                        print("Please note that All \33[31maccount usernames\33[34m are \33[31m cAsE sEnSiTiVe\33[34m")


                        sleep(5)
        

        # Add User Operation
        if User_Desired_Operation in [Number for Number in user_management_operations.keys() if Number == 8]:


            LOOP12 = True


            while LOOP12 == True:


                clean()


                adduser_operation_assurance = input("Are You \33[31m \33[0mSURE \33[31mYou \33[34m Would like to add \33[31m Another Account\33[34m? (\33[31mYes Or No Only) : \33[0m")
                adduser_operation_assurance = adduser_operation_assurance.title()


                if adduser_operation_assurance == "Yes":


                    clean()


                    Collect_UserName()
                    collect_MasterPassword()
                    Collect_BirthDate()


                    LOOP12 = False


                elif adduser_operation_assurance == "No":


                    clean()


                    print("\33[31mReturning to the main menu...\33[34m")


                    sleep(4)


                    LOOP12 = False
                

                else:


                    print("That Is not A \33[31m Yes \33[34m Or \33[31mNo\33[34m , Please try again")


                    sleep(4)


                    continue
        

        # DELETE ACCOUNT.
        if User_Desired_Operation in [Number for Number in user_management_operations.keys() if Number == 8]:


            LOOP13 = True


            while LOOP13 == True:


                clean()


                sleep(3)


                user_confirmation = input("Are You sure You would like to \33[31m Delete the current account\33][34m(\33[31mYes \33[34m or \33[31m no \33[34m Only) : ")
                user_confirmation = user_confirmation.strip() 
                user_confirmation = user_confirmation.title()


                if user_confirmation != "Yes" and user_confirmation != "No":


                    clean()


                    print("\33[31m Incorrect Entry.\33[34m")
                    print("\33[34m Please \33[31m Try Again.\33[34m")


                    sleep(3)


                    continue

                
                elif user_confirmation == "Yes":


                    masterpassword_input = input("Please enter the \33[31mMasterPassword\33[34m for the \33[31m Current account\33[34m : ")



                    if equality_check(masterpassword_input ,Users_Info["Users"][Inputted_Username]["MasterPassword"]) == True:


                        del Users_Info["Users"][Inputted_Username]

                        
                        Collect_UserName()
                        collect_MasterPassword()
                        Collect_BirthDate()


                        clean()


                        LOOP13 = False


                    else:


                        clean()


                        print("\33[31m Access Denied.")


                        LOOP13 = False

                    

                elif user_confirmation == "No":


                    clean()


                    print("\33[31m Returning \33[34m To the \33[31m Main Menu\33[34m")


                    LOOP13 = False





        # Quitting Operation.
        if User_Desired_Operation in [Number for Number in Operations.keys() if Number == 6]:


            # One of the database Defined Function's , Which will terminate the program In a ordinary way , With a comfy GoodBye Message!
            termination()


"--------------------------- Main Menu Function (End) -------------------"


def running():

    starting()
    Collect_UserName()
    collect_MasterPassword()
    Collect_BirthDate()
    Main_Menu()


running()

