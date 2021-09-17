#Full Retirement Calculator
#Design and Coded by: Shenessa Shaw
#CSC256 Unit 1

#import needed modules
import sys
import Calculator

#Variables to hold user inputted values
userBirthYear = 0
userBirthMonth = 0
retirementAgeYear = 0
retirementAgeMonth = 0

#Print program title
print("Social Security Full Retirement Age Calculator\n")

#Use while loop to control program
endProgram = False

#Ask user for a birth year
askForBirthYear = input("Enter year of birth or press enter to exit: ")

while (endProgram == False):

    #Use if else structure to determine the next step of the program based on user's input
    
    #If askForBirthYear is blank (user pressed Enter without entering a value), exit program
    if (askForBirthYear == ''):
        endProgram = True
        sys.exit()
    #Else if askForBirthYear contains non-numeric characters display error message and ask user to reenter birth year
    elif (askForBirthYear.isdigit() == False ):
        print("Invalid entry. Please Try again.")
        askForBirthYear = input("Enter year of birth or press enter to exit: ")
    #Else if askForBirthYear is less then 1900 thus not meeting the requirement of being in or after 1900,
    #display error message and ask user to reenter birth year
    elif (int(askForBirthYear) < 1900):
        print("Birth year must be in or after 1900, up to the current year.")
        askForBirthYear = input("Enter year of birth or press enter to exit: ")
    #Else if askForBirthYear is greater than 1899 thus meeting the requirement of being in or after 1900, 
    #store askForBirthYear value in userBirthYear and proceed to next step of program
    elif (int(askForBirthYear) > 1899):
        userBirthYear = int(askForBirthYear)

        #Ask user for birth month
        askForBirthMonth = input("Enter the month of birth (as a number): ")

        #Validate user's input for birth month
        #Use while loop to evaluate if user's input is valid and if valid store value in variable named userBirthMonth
        isBirthMonthValid = False
        while (isBirthMonthValid == False):

            #Use if else structure to determine the next step of the program based on user's input

            #If askForBirthMonth contains anything other than a numeric value
            if (askForBirthMonth.isdigit() == False):
                print("Invalid entry. Please Try again.")
                askForBirthMonth = input("Enter the month of birth (as a number): ")
            #Elif askForBirthMonth is between 1 and 12, it meets the requirement of being a valid month
            elif (int(askForBirthMonth) >= 1 and int(askForBirthMonth) <= 12):
                userBirthMonth = int(askForBirthMonth)
                isBirthMonthValid = True
            #Else user inputted nonething and value is invalid
            else:
                print("Invalid entry. Please try again.")
                askForBirthMonth = input("Enter the month of birth (as a number): ")

        Calculator.calculate(userBirthYear, userBirthMonth)

        #Restart program
        askForBirthYear = input("Enter year of birth or press enter to exit: ")