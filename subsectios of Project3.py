#A program that works out if a given year is a leap year



#This is how you work out if a particular year is a leap year:
#on every year that is evenly  divisible by 4
    #except every year that is evenly divisible by 100 
        #unless the year is also evely divisible by 400

year = int(input("Enter the year:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("A leap year")
    else: 
        print ("A leap year")
else:
    print("Not a leap year")