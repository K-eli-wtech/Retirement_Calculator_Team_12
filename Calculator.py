#Full Retirement Calculator
#Design and Coded by: Shenessa Shaw
#CSC256 Unit 1

def calculate(userBirthYear, userBirthMonth):
    #Determine full retirement age based on userBirthYear, userBirthMonth, and SSA Retirement Benefit By Year Chart
    #Dictionary containing numeric month:written month key:value values
    monthsDict = {1:"Janurary", 2:"Feburary", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    if (userBirthYear <= 1937):
        print("Your full retirement age is 65 years and 0 months.")
        #Calculate month and year of user's retirement
        retirementYear = userBirthYear + 65
        print("This will be in " + monthsDict[userBirthMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear == 1938):
        print("Your full retirement age is 65 years and 2 months.")
        retirementMonth = userBirthMonth + 2
        if (retirementMonth > 12):
            retirementYear = userBirthYear + 66
            retirementMonth = retirementMonth - 12
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
        else:
            retirementYear = userBirthYear + 65
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear == 1939):
        print("Your full retirement age is 65 years and 4 months.")
        retirementMonth = userBirthMonth + 4
        if (retirementMonth > 12):
            retirementYear = userBirthYear + 66
            retirementMonth = retirementMonth - 12
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
        else:
            retirementYear = userBirthYear + 65
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear == 1940):
        print("Your full retirement age is 65 years and 6 months.")
        retirementMonth = userBirthMonth + 6
        if (retirementMonth > 12):
            retirementYear = userBirthYear + 66
            retirementMonth = retirementMonth - 12
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
        else:
            retirementYear = userBirthYear + 65
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear == 1941):
        print("Your full retirement age is 65 years and 8 months.")
        retirementMonth = userBirthMonth + 8
        if (retirementMonth > 12):
            retirementYear = userBirthYear + 66
            retirementMonth = retirementMonth - 12
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
        else:
            retirementYear = userBirthYear + 65
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear == 1942):
        print("Your full retirement age is 65 years and 10 months.")
        retirementMonth = userBirthMonth + 10
        if (retirementMonth > 12):
            retirementYear = userBirthYear + 66
            retirementMonth = retirementMonth - 12
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
        else:
            retirementYear = userBirthYear + 65
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear >= 1943 and userBirthYear <= 1954):
        print("Your full retirement age is 66 years and 0 months.")
        #Calculate month and year of user's retirement
        retirementYear = userBirthYear + 66
        print("This will be in " + monthsDict[userBirthMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear == 1955):
        print("Your full retirement age is 66 years and 2 months.")
        retirementMonth = userBirthMonth + 2
        if (retirementMonth > 12):
            retirementYear = userBirthYear + 67
            retirementMonth = retirementMonth - 12
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
        else:
            retirementYear = userBirthYear + 66
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear == 1956):
        print("Your full retirement age is 66 years and 4 months.")
        retirementMonth = userBirthMonth + 4
        if (retirementMonth > 12):
            retirementYear = userBirthYear + 67
            retirementMonth = retirementMonth - 12
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
        else:
            retirementYear = userBirthYear + 66
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear == 1957):
        print("Your full retirement age is 66 years and 6 months.")
        retirementMonth = userBirthMonth + 6
        if (retirementMonth > 12):
            retirementYear = userBirthYear + 67
            retirementMonth = retirementMonth - 12
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
        else:
            retirementYear = userBirthYear + 66
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear == 1958):
        print("Your full retirement age is 66 years and 8 months.")
        retirementMonth = userBirthMonth + 8
        if (retirementMonth > 12):
            retirementYear = userBirthYear + 67
            retirementMonth = retirementMonth - 12
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
        else:
            retirementYear = userBirthYear + 66
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear == 1959):
        print("Your full retirement age is 66 years and 10 months.")
        retirementMonth = userBirthMonth + 10
        if (retirementMonth > 12):
            retirementYear = userBirthYear + 67
            retirementMonth = retirementMonth - 12
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
        else:
            retirementYear = userBirthYear + 66
            print("This will be in " + monthsDict[retirementMonth] + " of " + str(retirementYear) + "\n")
    elif (userBirthYear >= 1960):
        print("Your full retirement age is 67 years and 0 months.")
        #Calculate month and year of user's retirement
        retirementYear = userBirthYear + 67
        print("This will be in " + monthsDict[userBirthMonth] + " of " + str(retirementYear) + "\n")