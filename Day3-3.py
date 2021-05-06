height = int(input("hat is your height in cm? "))


if height >= 120 :
     print("can ride")
     age = int(input("hat is your age "))
     if age < 12:
        print("please pay 5.")                         
     elif age <= 18:
        print("please pay 7")
     else:
        print("please pay 12")                    
else:
  print("can't ride")