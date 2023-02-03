# COMPULSORY TASK 1

import math 

# initializing a flag
flag_in=True

# checking if the right option has been input

# defining list of acceptable inputs
accept_input=['investment','bond']

# initializing statments in a while loop
# checking the input, if input is in acceptable list ,break the loop
# else print error message and ask for the input again in the loop

while flag_in == True:
    # Prinitng the input options
    print("Choose wither \'investment\' or \'bond\' from the menu below to proceed")
    print('investment   -  to claculate the amout of interest you\'ll earn on your investment')
    print('bond         -  to calculate the amount you\'ll have to pay on a home loan')

    in_data=input()
    # converting input to lower case
    in_data=in_data.lower()
    
     
    #############################################################################################

    # If the users askd for INVESTMENT
    if in_data=='investment':

         # Asking user to input the values of inverstment, years and percenatage and typecasting accordingly

        money_in=float(input("Enter the money you want to deposit \n"))
        percent_in=int(input("Please enter the interest as a percentage \n"))
        years_in=int(input("Please enter the number of years you plan to invest for \n"))


        # validating input is S imple or compound only
        compound_flag=True

        while compound_flag==True:
            interest_type=input("Please select the interest type\n S for Simple\n C for Compound\n")     
            interest_type=interest_type.lower()

            if interest_type=='s':
                # For simple, calculate and break the loop
                amount= money_in*(1+(percent_in/100)*years_in)
                break
            elif interest_type=='c':
                # for compound, calculate and break the loop
                amount=money_in*math.pow((1+(percent_in/100)),years_in)
                break
            else:
                # otherwise print error
                print("**********Error************\n Choose either Compound C or Simple S")
                pass

        # after the while loop exit
        #   Rounding to 2 decimal values and printing the results
        amount=round(amount,2)
        print(f"For initial investment of £{money_in} for {years_in} years at interest rate {percent_in}%, the amount will be £{amount} \n\n")
        
        # changing flag value to exit the whil loop
        flag_in=False
   

    ##############################################################################################################################
    # if user selects bonds
    elif in_data=='bond':
        # Asking user to input the values of house value, interest rate and number of years and typecasting accordingly

        value_in=float(input("Enter the current value of the house \n"))
        interest_in=int(input("Please enter the interest  rate as a percentage \n"))
        monthly_interest=interest_in/(12*100)
        months_in=int(input("Please enter the number of months you plan to take to repay the bond\n"))

        # calculating using the formula
        amount=(monthly_interest*value_in)/(1-(math.pow((1+monthly_interest),(-1*months_in))))

        #   Rounding to 2 decimal values and printing the results
        amount=round(amount,2)
        print(f"The user will have to pay £{amount} each month for a bond on the value of £{value_in} for {months_in} months at interest rate {interest_in}% \n\n")
        
        # changing flag value to exit the while loop
        flag_in=False

    ################################################################################################################################
    # else print error and go to the start of the loop again
    else:
       print("*************************Error !!!!*******************************\n Please input a valid option.\n\n")

