#------------------CAPSTONE PROJECT IV---------------------------------

from tabulate import tabulate


#========The beginning of the class==========
class Shoe:
    ''' shoe class to store the shoe objects in the inventory. It contains the constuctor function and methods'''

    def __init__(self, country, code, product, cost, quantity):
        # class cnstructor to assign the attributes 
        self.country=country
        self.code=code
        self.product=product
        self.cost=cost
        self.quantity=quantity

    # method function to return the cost of the shoe   
    def get_cost(self):
        return self.cost
        
    # method function to return the quantity of the shoes
    def get_quantity(self):
        return self.quantity
       
    # method function to return the string representation of the class
    def __str__(self):
        print(f'{self.country}  {self.code} {self.product}  {self.cost} {self.quantity}\n')
        


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    # shoe list initialized to store data
    
    # opening the file to read
    # using try-except for error handling
    try:
        data_file=open("inventory.txt",'r')
        #reading the first line and skipping it
        line=data_file.readline()
        for line in data_file.readlines():
            
            # for the rest of the lines, splitting into seperate words 
            txt_line=line.strip('\n').split(',')
            # creating a class object from the attributes
            shoe_obj=Shoe(txt_line[0],txt_line[1],txt_line[2],txt_line[3],txt_line[4])
            # appending shoe object to the shoe list
            shoe_list.append(shoe_obj)
    except FileNotFoundError as error:
        print("Error, File does not exist")
        print(error)
   
    # closing the file
    data_file.close()
    
#=  =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =
# function to capture a new shoe
def capture_shoes(country_in,code_in,product_in,cost_in,quantity_in):
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    # creating a new shoe object
    new_shoe=Shoe(country_in,code_in,product_in,cost_in,quantity_in)

    # writing data in inventory file
    with open('inventory.txt','a+') as add_data:
        write_string=country_in+','+code_in+','+product_in+','+cost_in+','+quantity_in+'\n'
        add_data.write(write_string)

    # adding it into the shoe list
    
    shoe_list.append(new_shoe)
    

    # writing data in inventory file
    with open('inventort.txt','a+') as add_data:
        write_string=country_in+','+code_in+','+product_in+','+cost_in+','+quantity_in+'\n'
        add_data.write(write_string)

#=  =   =   =   =   =   =   =   =   =   =   =   =   =   =   =
# function definition for function to view all
def view_all(shoe_list_input):
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    #print(len(shoe_list_input))
    for cnt in range(0,len(shoe_list_input)):
        line=shoe_list_input[cnt]
        line.__str__()


#=  =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =
# function definition to view all in form of a table
def view_all_table(shoe_list_input):
    # defining a list of class objects
    all_data=[]
    # using a for loop for the whole length of shoe list objects
    for list_len in range(0,len(shoe_list_input)):
        # storing the attributes of the object in a list
        the_shoe=shoe_list_input[list_len]
        the_shoe_object=[the_shoe.country,the_shoe.code,the_shoe.product,the_shoe.cost,the_shoe.quantity]
        # stroing the data in an output list
        all_data.append(the_shoe_object)

    # priniting the table using the tabulate module
    head_line=["Country","Code","Product","Cost","Quantity"]
    print(tabulate(all_data,headers=head_line))

#=  =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   
# function definition to restock the shoe with the least quantity
def re_stock(shoe_list_input):
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # defining a variable to store the object with least stock and assigning it the calue of the first object
    obj_least=shoe_list_input[0]
    # running a for loop for the whole length of the list and compairing the shoe stock number to find the minimum number
    for cnt in range(1,len(shoe_list_input)):
        #if the quantity of the present object is less than the least quantity, make the present object the least quantity object
        # type casting to int for comparsion of numbers
        if int(((shoe_list_input[cnt]).quantity))< int(obj_least.quantity):
            obj_least=shoe_list_input[cnt]
        else:
            pass

    # printing the object with the least stock
    print(f"The object with the lowest quantity is {obj_least.product}\n")

    # asking user if they want to order more
    # using two while loop to keep on looping until user enter the correct input
    input_num=True

    # while the condition is true
    while input_num==True:
        # asking user if they want to restock
        input_arg=input("Do you want to restock this shoe? yes or no?\n")
        # if the user enter yes, ask the user how many items they want to add
        if input_arg=='yes':
            # using a while loop for exception incase user enters a wrong input
            while True:
                try:
                    # asking user to enter the quantity they want to order
                    order_more=int(input("How many items do you want to order?\n"))
                    #' making input_num False to break the outer while loop
                    input_num=False
                
                    break

                except Exception:
                    print("Enter a number please \n")

            # updating quantity in the file
            # the object the user wants to update
            find_object=obj_least.product
            # opening the file and reading the data as contents
            # then closing the file
            data_file=open("inventory.txt",'r+')
            contents=data_file.readlines()
            data_file.close()

            # now finding the data in the file for the item the user wants to order
            # initializing thge line counter as cnt to 0

            cnt=0
            # running a for loop for the whole length of contents
            for line in contents:
                # splitting the line 
                split_data=line.strip('\n').split(',')
                #getting the item name of the item on that line
                chk_stock=split_data[2]
                # checking if the item name is the one we are looking for
                if chk_stock==find_object:
                    # if this is the item user wants to order, converting the quantity to int
                    # adding the new stock number to present number
                    # making a string of the product information
                    the_quantity=int(split_data[4])
                    new_quantity=str(the_quantity+order_more)
                    # new updated product information
                    new_data=split_data[0]+','+split_data[1]+','+split_data[2]+','+split_data[3]+','+new_quantity+'\n'
                    # assigning this new value at the contents at the cnt location
                    contents[cnt]=new_data
                else:
                    # otherwise just update the counter
                    cnt+=1
            
            # writing the updated data in the file
            # opening the file to write data
            # writing data 1 line at a time
            # closing the file when finished
            write_file=open("inventory.txt",'w')
            for cnt_write in range(0,len(contents)):
                write_file.write(contents[cnt_write])

            write_file.close()

            print("Data updated in inventory, Returning to main menu \n")

        # if user enters no, break the loop
        elif input_arg=='no':
            print('Returning to main menu \n')
            break
        # if user enters anyother input than yes/no, print an error
        else:
            print("Wrong input entered, Enter yes or no\n")

  
            
#=  =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   
# function definition to search a show with a particular code
def search_shoe(shoe_list,the_code):
    
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    the_object=0
    # running a for loop for the whole length of shoe_list
    for shoe_cnt in range(0,len(shoe_list)):
        if (shoe_list[shoe_cnt]).code==the_code:
            the_object=(shoe_list[shoe_cnt]).product

    # if the object is found
    if the_object != 0:
        return(the_object)
    else:
        return ("Error,Code not found")

#=  =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   
# function definition to print the value of all the items in the list
def value_per_item(shoe_list):
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    value=[]
    shoe_data=[]
    header_line=["Product","Value"]
    for chk_value in range(0,len(shoe_list)):
        shoe_value=(int((shoe_list[chk_value].cost)))*(int((shoe_list[chk_value].quantity)))
        shoe_data.append([shoe_list[chk_value].product,shoe_value])
        value.append(shoe_value)
    print(tabulate(shoe_data,headers=header_line))
    #return value

#=  =   =   =   =   =   =       ==  =   =   =   =   =   
# function definition to prit the item with the highest qunatity
def highest_qty(shoe_list_input):
    
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # defining the max_quantity variable and initializing to the first value of the list
    obj_max=shoe_list_input[0]
    cost_obj=0

    # running a for loop for the whol elength of shoe_list

    for cnt in range(1,len(shoe_list_input)):
        #if the quantity of the present object is greater than the max_quantity, make the present object the max quantity object
        # type casting to int for comparsion of numbers
        if int(((shoe_list_input[cnt]).quantity))> int(obj_max.quantity):
            obj_max=shoe_list_input[cnt]
        else:
            pass

    #print(obj_max.)      
    print(f"The shoe with the highest quantity is {obj_max.product} \n")
    print(f"Its cost is {obj_max.cost}\n")
    percent_discount=int(input("How much discount do you want to put on it (Enter a percentage number)?\n"))
    new_cost=(int(obj_max.cost))*(100-percent_discount)/100
    print(f"The new cost of the shoe is noe {new_cost}")
   
    # updating data in the inventory.txt file
    # opening the file and reading the data as contents
    # then closing the file
    data_file=open("inventory.txt",'r+')
    contents=data_file.readlines()
    data_file.close()

    # now finding the data in the file for the item the user wants to order
    # initializing thge line counter as cnt to 0

    cnt=0
    # running a for loop for the whole length of contents
    for line in contents:
        # splitting the line 
        split_data=line.strip('\n').split(',')
        #getting the item name of the item on that line
        chk_stock=split_data[2]
        # checking if the item name is the one we are looking for
        if chk_stock==obj_max.product:
            # if this is the item user wants put on discount , then change th cost to new cost
            new_data=split_data[0]+','+split_data[1]+','+split_data[2]+','+str(new_cost)+','+split_data[4]+'\n'
            # assigning this new value at the contents at the cnt location
            contents[cnt]=new_data
        else:
            # otherwise just update the counter
            cnt+=1
    
    # writing the updated data in the file
    # opening the file to write data
    # writing data 1 line at a time
    # closing the file when finished
    write_file=open("inventory.txt",'w')
    for cnt_write in range(0,len(contents)):
        write_file.write(contents[cnt_write])

    write_file.close()
            
    print("Data updated in inventory \n\n")

####################################################################################################################################################################
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
print("WELCOME TO THE SHOE INVENTORY   \n\n")
while True:
    # printing the menu and asking user to choose option
    option=input('''Select one of the following Options below:
v - View data in inventory
a - Add new shoe data
r - Restock shoe
s - Search shoe with code
p - View value of shoes
h - View shoe with highest quantity
e - Exit
: ''').lower()

    #reading data from shoe file and converting it into list of objects
    read_shoes_data()

    # performing action depending on user input
    if option=='v':
        #if user wants to view data in inventory
        #read_shoes_data()
        shoe_list=[]
        read_shoes_data()
        view_all_table(shoe_list)
        print('\n\n')

    elif option=='a':
        # if user wants to enter new data to the inventory
        # asking user to input the data
        
        code_found=True

        while code_found==True:
            
            # asking user to enter the shoe code
            code_shoe=(input("Enter the code of the shoe\n")).upper()
            # checking if the code already exists
            for check_cnt in range(0,len(shoe_list)):
                if code_shoe== shoe_list[check_cnt].code:
                    print("Code already exists \n \n")
                    code_found=True
                    break
                else:
                    code_found=False

        
        country_shoe=(input("Enter the country\n")).capitalize()
        product_shoe=(input("Enter the product name\n")).capitalize()
        cost_shoe=input('Enter the cost of the shoe \n')
        quantity_shoe=input("Enter the quantity\n")

        # calling function to add the data to the shoe inventory
        capture_shoes(country_shoe,code_shoe,product_shoe,cost_shoe,quantity_shoe)

        # printing the message that shoe is added
        print("Shoe data successfully added. Returning to main menu \n\n")
        
        
    elif option=='r':
        # if user selects to restock
        # function call to restock shoe
        re_stock(shoe_list)

    elif option=='s':
        # if user wants to search a show with code
        # asking user to enter the code he/she wants to search
        # converting it to uppercase to make it case insensitive
        code_in=(input("Enter the shoe code you want to search \n")).upper()

        # calling the function to search for the shoe using the code
        shoe_found=search_shoe(shoe_list,code_in)
        # printing the output
        print(shoe_found+'\n')


    elif option=='p':
        # if the user selects to view value of shoes
        # calling function to get the value of the shoes
         value_per_item(shoe_list)
         print('\n')

    elif option=='h':
        # if the user wants to view shoe with highest quantity
        highest_qty(shoe_list)
        
    elif option=='e':
        print("Goodbye")
        exit()
    else:
        print("You have made a wrong choice, Please try again\n")

