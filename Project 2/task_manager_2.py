##################################################################
#            CAPSTONE PROJECT 2

flag=True

#====Login Section====
# opening the user.txt file 
file_user=open("user.txt","r+")
# reading the data
data=file_user.readlines()
# finding how many users are stored
file_user.seek(0)
length=len(data)

# defining a dictionary to store user name and password
user_dict={}
for my_len in range (0,length):
    present_user=file_user.readline()
    present_user=present_user.split()
    user_name=present_user[0]
    user_name=user_name[0:-1]
    pass_word=present_user[1]
    # updating the username and password in dictionary
    user_dict.update({user_name:pass_word})


dict_length=len(user_dict)

##################################################################
cnt=3

# ASking user to input user name and password
# if user enters wrong user name, askd them to enter a correct user name and continue until correct name entered
while cnt==3:
    in_user=input('Please enter your username \n')
    # if name not found in the dictionary, asking to enter again until right name found
    while in_user not in user_dict:
        print("User name not found \n")
        in_user=input("Please enter your user name \n")

        # asking user to enter the password
        # checking if its the correct password from dictionary
        #  if wrong password entered, print a warning that wrong password
        # askes user to enter the password again 3 times
        # after 3 tries, print too many wrong passwords,try again
        # ask user to enter the user name again
    in_password=input("Please enter your password \n")
    check_password=user_dict[in_user]
    cnt=1
    while (check_password) != (in_password):
        print("Wrong password")
        in_password=input("Please enter your password \n")
        # allowing to enter the password 3 times
        cnt+=1
        if cnt==3:
            print("\n\nToo many wrong passwords, Try later\n\n")
            # flag made False so cant access tha system
            break


#########################################################################
while flag:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    # menu based on user name

     # menu for admin
    if in_user=='admin':
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
sv - statistics view
e - Exit
: ''').lower()

    # for all other users, menu
    else:
        menu = input('''Select one of the following Options below:

a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()


    if menu == 'r':
        # Allowing user to register a new user
        # making sure only admin cas access it

        if in_user=='admin':

            new_user=input("Enter the new username \n")
            new_password=input("Enter the new password\n")
            new_password_con=input("Please confirm the password \n")

            # if they are not same, asking to input again
            while new_password != new_password_con:
                print("Two passwords not same \n")
                new_password=input("Please renetre the password \n")
                new_password_con=input("Please confirm your password \n")
        
            # writing the data to file
            data_write='\n'+new_user+', ' +new_password
            file_user.write(data_write)
            file_user.close()
        
        else:
            pass

    elif menu== 'a':
        # if user selects adding a new task
        print("Details for enetering a new task for a user")
        user_a=input("Please enter the user the task is assigned for:\n")
        title_a=input("Please enter the title of the task \n")
        desc_a=input("Please enter a description of the task \n")
        duedate_a=input("Please enter a due date for the task \n")
        currentdate_a=input("Please eneter todays date \n")

        # adding data to the file 
        with open("tasks.txt","a") as task_file:
            space=', '
            write_string='\n'+user_a+space+title_a+space+desc_a+space+duedate_a+space+currentdate_a+space+'No'
            task_file.write(write_string)

    elif menu== 'va':
        # if the user wants to view all the tasks
        with open("tasks.txt",'r') as read_file:
            content=read_file.readlines()
            length_f=len(content)
            read_file.seek(0)
            for count in range(0,length_f):
                present_line=read_file.readline()
                split_line=present_line.split(', ')
                # printing the data
                print('\n--------------------------------------------------')
                print("Task:                            "+split_line[1])
                print('ASsigned to:                     '+split_line[0])
                print("Date assigned:                   "+split_line[4])
                print("Due date:                        "+split_line[3])
                print("Task completed?                  "+split_line[5])
                print("Task description:")
                print('  '+ split_line[2])
            print('-----------------------------------------------\n')
            print('-----------------------------------------------\n')
            
    elif menu== 'vm':
        # view my task
        with open("tasks.txt",'r') as read_file:
            content=read_file.readlines()
            length_f=len(content)
            read_file.seek(0)
            for count in range(0,length_f):
                present_line=read_file.readline()
                split_line=present_line.split(', ')

                if split_line[0]==in_user:
                    # printing the data if it is for the user name logged in
                    print('\n--------------------------------------------------')
                    print("Task:                            "+split_line[1])
                    print('ASsigned to:                     '+split_line[0])
                    print("Date assigned:                   "+split_line[4])
                    print("Due date:                        "+split_line[3])
                    print("Task completed?                  "+split_line[5])
                    print("Task description:")
                    print('  '+ split_line[2])
                else:
                    pass

            print('-----------------------------------------------\n')

    elif menu== 'sv':
        #if admin selects to view statistics
        if in_user=='admin':
            with open("tasks.txt",'r') as read_file:
                content=read_file.readlines()
                length_f=len(content)
                read_file.seek(0)
                user_list={}
                for count in range(0,length_f):
                    present_line=read_file.readline()
                    split_line=present_line.split(', ')
                                      
                    if split_line[0] not in user_list:
                        user_list[split_line[0]]=1
                
                    else:
                        current_value=user_list[split_line[0]]
                        user_list[split_line[0]]=current_value+1

                # printing the dictionary
                for key,value in user_list.items():
                    print(key,'          ',value)
                    
            
                              

            print('-----------------------------------------------\n')
        # if other users try to access just pass
        else:
            pass


    
    elif menu== 'e':
        # if user wants to exit
        print("Good bye")
        exit()

    else:
        print("You have made a wrong choice, Please try again")


