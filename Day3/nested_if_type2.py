print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    #the indentation in python is very importangt
    print("you can ride the ROLLERCOASTER!")
    age=int(input("What is your age?"))
    if age <=12:
        bill=5
        print("Please pay $5")
    elif age <=18:
        bill=7
        print("Please pay $7")
    elif age>=45 and age<=55:
        print("You get a free ride!")
        bill=0
    else:
        bill=12
        print("Please pay $12") 
    
    photo=input("Do you want a photo taken? Y or N: ")  
    if photo == "Y":
        bill += 3
        print("Your photo will be taken and you will be charged an additional $3")
        print(f"Your bill is ${bill}")
else:
    print("Sorry you hav to grow taller before you can ride")
    