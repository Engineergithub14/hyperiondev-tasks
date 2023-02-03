##################################################################
#            CAPSTONE PROJECT 2

# inporting the modules
import datetime

# defining the functions

# defining function for registring user
def reg_user(file_name):
    file_user=open(file_name,'a+')
    # asking user to input user name
    flag=True
    while flag==True:
        new_user=input("Enter the new username \n")
        # opening the file to read data
        file_user.seek(0)
        # reading data from file one line at a time and checking the new_user matches it
        for line in (file_user.readlines()):
            line_split=line.split(', ')
            name=line_split[0]
            if name==new_user:
                print("User name already exists")
                flag=True
                break
            else:
                flag=False

    # asking user to enter the password 
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
    # closing the file
    file_user.close()
        

########################################################
# defining function for adding a task
def add_task(file_name):
    # asking user to enter the details
    print("Details for enetering a new task for a user")
    user_a=input("Please enter the user the task is assigned for:\n")
    title_a=input("Please enter the title of the task \n")
    desc_a=input("Please enter a description of the task \n")
    duedate_a=input("Please enter a due date for the task \n")
    currentdate_a=input("Please enter todays date \n")

    # adding data to the file 
    with open(file_name,"a+") as task_file:
        space=', '
        write_string=user_a+space+title_a+space+desc_a+space+duedate_a+space+currentdate_a+space+'No'+'\n'
        
        task_file.write(write_string)


#######################################################
# defining function for view all
def view_all(file_name):
    # opening the file
    with open(file_name,'r') as view_all_file:
        # checking the length of file
        content_all=view_all_file.readlines()
        length_f=len(content_all)
        view_all_file.seek(0)
        # printing data for each line
        for count in range(0,length_f):
            # reading a line at a time
            present_line=view_all_file.readline()
            # splittting the data removing the symbols between
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

############################################################################
# defining function to view my tasks
def view_mine(file_name,user):
    # opening the file
    with open("tasks.txt",'r+') as read_file:
        # reading the file to find the tasks for the specific user
        content=read_file.readlines()
        length_f=len(content)
        read_file.seek(0)
        # counter for counting the tasks of the specific user
        cnt_display=0
        # storing the task line numbers for that user in a list
        out_task=[]

        # running the for loop for the whole length
        # checking one line at a time
        # checking if the username for that line is the required user
        # if yes, ass the task number to the list, otherwise just pass
        for count in range(0,length_f):
            present_line=read_file.readline()
            split_line=present_line.split(', ')

            # counter for task of user             
            if split_line[0]==user:
                # noting the lines with the taskd for user
                out_task.append(count)
                cnt_display+=1
            else:
                pass
            
        # displaying the user has total tasks
        print(f"You have {cnt_display} tasks")
        
        # asking user they want to view all their tasks or some of them
        task_choose=input("Do you want to view all tasks? \nEnter\n A for view and edit Tasks \n-1 to return to main menu\n")
        task_choose=task_choose.lower() 
        
        # if the user wants to view all his/her tasks
        if task_choose=='a':
            # reading data from file for this user and displaying it
            read_file.seek(0)
            task_count=0
            for count in range(0,length_f):
                if task_count==len(out_task):
                    break
                elif count==out_task[task_count]:
                    present_line=content[count]
                    split_line=present_line.split(', ')

                
                    # printing the data if it is for the user name logged in
                    print('\n--------------------------------------------------')
                    print("Task:                            "+split_line[1])
                    print('ASsigned to:                     '+split_line[0])
                    print("Date assigned:                   "+split_line[4])
                    print("Due date:                        "+split_line[3])
                    print("Task completed?                  "+split_line[5])
                    print("Task description:")
                    print('  '+ split_line[2])
                    task_count+=1
                else:
                    pass

            print('-----------------------------------------------\n')
            # asking user if they want to edit a task
            task_edit=(input('Do you want to edit a task?\nY or N \n')).lower()

            # if user wants to edit
            if task_edit=='y':
                # asking user to enter the task number they want to edit
                print(f"You have {cnt_display} tasks")
                # if user has more than 0 tasks
                if cnt_display>0:
                    task_number=input("Enter the task number you want to edit \n")
                    # loop to avoid any non numeric inputs
                    check_cnt=0
                    while check_cnt==0:
                        if task_number.isnumeric():
                            task_number=int(task_number)
                            check_cnt=1
                        else:
                            print("Error, Enter a task number")
                            task_number=input("Enter a task number\n")                
                        

                    # getting the line that the user wants to change
                    not_line=content[out_task[task_number-1]]
                    not_split=not_line.split(', ')
                    
               
                    # Displaying the data thats the user wants to change
                    print('\n--------------------------------------------------')
                    print(f"TASK NUMBER {task_number}")
                    print("Task:                            "+not_split[1])
                    print('ASsigned to:                     '+not_split[0])
                    print("Date assigned:                   "+not_split[4])
                    print("Due date:                        "+not_split[3])
                    print("Task completed?                  "+not_split[5])
                    print("Task description:")
                    print('  '+ not_split[2])
                    print('-----------------------------------------------\n')

                    # checking if the task has been completed or not
                    task_modify=(not_split[5]).lower()
                    print(task_modify[0])
                    if (task_modify[0]) =='n':
                        # counter to keep track of any change
                        cnt_change=0
                        # asking user if they want to edit due date
                        # if yes, asking for new due date
                        due_date_change=(input("Do you want to change due date? Y or N \n")).lower()
                        if due_date_change=='y':
                            new_date=input("Please enter a new duedate\n")
                            not_split[3]=new_date
                            cnt_change=1
                        else:
                            pass

                        # asking user if they want to change who the task is assigned to
                        user_change=(input("Due to want to change who the task is assigned to? enter Y or N \n")).lower()
                        if user_change=='y':
                            input_task_user=input("Please enter who the task is now assigned to\n ")
                            not_split[0]=input_task_user
                            cnt_change=1
                        else:
                            pass

                        # asking user if they want to mark the task as done
                        task_done=(input("Do you want to mark the task as done? Enter Y or N \n")).lower()
                        if task_done=='y':
                            not_split[5]='Yes \n'
                            cnt_change=1
                        else:
                            pass

                        # if any changes done write it to file
                        if cnt_change==1:
                        
                            # joining to make a string to write in file
                            space=', '
                            write_string2=not_split[0]+space+not_split[1]+space+not_split[2]+space+not_split[3]+space+not_split[4]+space+not_split[5]
                
                            read_file.seek(0) 
                            read_data = read_file.read()  
                            # Read the contents of the file into memory.
                            # Return a list of the lines, breaking at line boundaries.
                            li = read_data.splitlines()
                            # now writing the data back in file
                            read_file.seek(0)
                            cnt_line=0
                            for item in li:
                                # if this is the edited line number, write the new string
                                if cnt_line==out_task[task_number-1]:
                                    read_file.write(write_string2)
                                    cnt_line+=1
                                else:
                                    #otherwise write the actual read line back
                                    read_file.writelines(item+'\n')
                                    cnt_line+=1
                        else:
                            # if no changes done
                            print("no changes done\n")
                            pass

                    else:
                        print("Task already completed, It cant be edited\n")
 
                # if user has 0 tasks
                elif cnt_display==0:
                    print("You do not have any tasks assigned.\n")
            elif task_edit=='n':
                
                print(" User doesn't want to edit a task. Returning to main menu\n")
            else:
                print("You can enter only yes or no, Wrong choce, Returning to main menu \n")
                   
        # is user wants to return to main menu
        elif task_choose=='-1':
            #read_file.close()
            print("Returning to main menu\n")
        
        else:
            # if any other choice made
            pass

################################################################
# defining function to generate reports
def generate_reports(file1_name,file2_name):

    # calling the function for writing report in task_overview.txt 
    write_task_overview(file1_name)

    write_user_overview(file1_name,file2_name)
   
           
       
##############################################################
# function to generate reports and write in task_overwiew.txt

def write_task_overview(file1_name):
# opening the file to read data
    with open(file1_name,'r') as read_file:
        content=read_file.readlines()
        length_f=len(content)
        read_file.seek(0)
        # counter to count task completed
        task_com=0
        # counter to count tasks uncompleted
        task_uncom=0
        # counter for overdue tasks
        overdue_cnt=0

        # checking all the tasks in the file

        for count in range(0,length_f):
            present_line=read_file.readline()
            split_line=present_line.split(', ')

            # checking each line
            task_status=(split_line[5]).lower()       
            # if task has been completed                        
            if task_status[0]=='y':
                task_com+=1
            # if task not already completed
            elif task_status[0]=='n':
                task_uncom+=1

                # calling function for check_overdue

                overdue=check_overdue(split_line)
                overdue_cnt=overdue_cnt+overdue

            

    # percentage of tasks uncomplete
    per_uncomp=round(((task_uncom/length_f)*100),2)

    # overdue tasks percentage
    per_overdue=round(((overdue_cnt/length_f)*100),2)

    # writing the report in task_overview.txt
    with open("task_overview.txt",'w') as write_task:
        write_task.write("TASK REPORT\n")
        write_task.write(f"Total tasks generated            {length_f}\n")
        write_task.write(f"Total completed tasks            {task_com}\n")
        write_task.write(f"Incompleted tasks                {task_uncom}\n")
        write_task.write(f"Overdue tasks                    {overdue_cnt}\n")
        write_task.write(f"Incompleted tasks percentage     {per_uncomp}%\n")
        write_task.write(f"Overdue tasks percentage         {per_overdue}%\n")

##########################################################
# function call for checking task overdue or not
def check_overdue(split_line):

    # checking if the task is over due or not
    # getting the due date of the project
    due_date_pro=split_line[3]
    #print(due_date_pro)
    due_date_s=due_date_pro.split(' ')
    due_year=int(due_date_s[2])
    due_month=due_date_s[1]
    # calling the function to return numerical month
    get_month=month_string_to_number(due_month)
    due_date=int(due_date_s[0])
    # converting using the datetime module
    d1 = datetime.date(due_year,get_month,due_date)

    # todays date
    d2 = datetime.date.today()

                
    #now check if todays date is more than the due date
    if d2>d1:
        # counting the overdue projects
        return 1
    else:
        return 0
       

############################################################
# function to convert day from one format to other  
# i have taken help for this function from internet                       
def month_string_to_number(check_month):
    # defining a dictionary of months
    months= {'jan': 1,'feb': 2,'mar': 3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
    # taking the first three letters of the input for comparison to the dictionary
    the_month = check_month.strip()[:3].lower()

    try:
        out = months[the_month]
        return out
    except:
        raise ValueError('Not a month')    

###############################################################
# function to generate reports in user_report.txt

def write_user_overview(file1_name,file2_name):
    
                
    # getting registered users from the user.txt file
    user_info=open(file2_name,'r')
    total_users=len(user_info.readlines())


    # getting total number of tasks from tasks.txt
    with open(file1_name,'r') as read_file:
        content=read_file.readlines()
        length_f=len(content)
        total_tasks=length_f
        read_file.seek(0)
        user_list={}
        for count in range(0,length_f):
            # checking the present line
            present_line=read_file.readline()
            split_line=present_line.split(', ')

            # if user not in the user_list dictionary, add the user 
            if split_line[0] not in user_list:
                                
                if ((split_line[5]).lower())[0]=='y':
                    # assign the counter for task completed and not completed accordingly
                    task_c=1
                    task_n=0
                    task_over=0
                elif ((split_line[5]).lower())[0]=='n':
                    task_n=1
                    task_c=0
                    task_over=check_overdue(split_line)
                    

                
                user_list[split_line[0]]=[1,task_c,task_n,task_over]
                
            # if user already in dictionary, update the values accordingly
            else:
                current_value=(user_list[split_line[0]][0])+1
                
                if ((split_line[5]).lower())[0]=='y':
                    task_c+=1
                        
                elif ((split_line[5]).lower())[0]=='n':
                    task_n+=1
                    this_task=check_overdue(split_line)
                    task_over=task_over+this_task
                    # checking if overdue


                user_list[split_line[0]]=[current_value,task_c,task_n,task_over]
            

        # opening the user_overview text file for writing data
         # writing user_overview in user_over.txt file
        with open("user_overview.txt",'w') as write_user:
            write_user.write("USER OVERVIEW\n")
            write_user.write(f"Total number of users registered     {total_users}\n")
            write_user.write(f"Total number of tasks                {total_tasks}\n")
            write_user.write("USER DETAILS\n")
            write_user.write("User, Total tasks,task completed, task not completed, percentage assigned to user,percentage completed,percentage still to complete,percent overdue\n")
        
            for key,[value,v2,v3,v4] in user_list.items():
                if key=='\n':
                    pass
                else:
                    percent_assign=str(round(((value/total_tasks)*100),2))
                    percent_completed=str(round(((v2/value)*100),2))
                    percent_to_complete=str(str(round(((v3/value)*100),2)))
                    percent_overdue=str(round(((v4/v3)*100),2))
                    sentence=key+', '+str(value)+', '+str(v2)+', '+str(v3)+', '+percent_assign+', '+percent_completed+', '+percent_to_complete+', '+percent_overdue+'\n'
                    write_user.write(sentence)

              
            # finding other users not in the list but in the users.txt file
            user_info.seek(0)
            for line in user_info.readlines():
                user_name_extract=line.split(', ')
                user_name_e=user_name_extract[0]
                if user_name_e not in user_list:
                    sentence2=user_name_e+', 0, 0, 0, 0, 0, 0, 0\n'
                    write_user.write(sentence2)
                else:
                    pass

        
    user_info.close()
   
        
################################################################
# defining function to view stats
def view_stats(file1_name,file2_name):
    # Reading data from task_overview file
    with open(file1_name,'r') as read_file:
        for line in read_file.readlines():
            print(line)
    
    # reading data from user overwiew
    with open(file2_name,'r') as readuser_file:
        count=0
        for line in readuser_file.readlines():
            if count<4:
                print(line)
                count+=1
            elif count==4:
                count+=1
            elif count>4:
                count+=1
                
                split_line=line.split(', ')
                print(split_line[0] +'\n')   
                print(f'Tasks assigned                                     {split_line[1]}')
                print(f'Tasks completed                                    {split_line[2]}')
                print(f'Tasks not yet completed                            {split_line[3]}')
                print(f'Percentage of total tasks assigned to this user    {split_line[4]}%') 
                print(f'Percentage of tasks completed                      {split_line[5]}%')
                print(f'Percentage of tasks still to complete              {split_line[6]}%')
                print(f'Percentage of tasks overdue                        {split_line[7]}%')
                print('-----------------------------------------------\n')

############################################################################
# the main rogram

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
# if user enters wrong user name, asked them to enter a correct user name and continue until correct name entered
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
    cnt=0
    while (in_password) != (check_password):
        print("Wrong password")
        cnt+=1

        if cnt<3:
            #allowing user to input password 3 times
            in_password=input("Please enter your password \n")
       
        elif cnt==3:
            # after 3 wrong passwords
            print("\n\nToo many wrong passwords, Try later\n\n")
            break


#########################################################################
while flag:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    # menu based on user name

     # menu for admin
    if in_user=='admin':
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
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
            # calling the function
            reg_user('user.txt')

        else:
            pass

    elif menu== 'a':
        # if user selects adding a new task
        # calling the function
        add_task('tasks.txt')
        
    elif menu== 'va':
        # if the user wants to view all the tasks
        # function call for view all
        view_all('tasks.txt')
            
    elif menu== 'vm':
        # view my task
        # ufnction call for view_mine
        view_mine('tasks.txt',in_user)

    
    elif menu== 'gr':
        #if admin selects to generate reports
        if in_user=='admin':
            # function call to view_Stats
            generate_reports('tasks.txt','user.txt')

            print("Reports generated \n")
           
        # if other users try to access just pass
        else:
            pass
       

    elif menu== 'ds':
        #if admin selects to view statistics
        if in_user=='admin':
            # checking if the task_overview file exists
            import os.path
            file_exists = os.path.exists('task_overview.txt')
            
            # if file doesn't exist, call the generate function to create the report
            if file_exists==False:
                generate_reports('tasks.txt','user.txt')
            
            
            # function call to view_Stats
            view_stats('task_overview.txt','user_overview.txt')
           
        # if other users try to access just pass
        else:
            pass


    
    elif menu== 'e':
        # if user wants to exit
        print("Good bye")
        exit()

    else:
        print("You have made a wrong choice, Please try again")


