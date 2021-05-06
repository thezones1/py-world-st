print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
sb=0
if size == "S":
    sb=15
    if add_pepperoni == "Y":
        sb += 3             
    if extra_cheese == "Y":
        sb += 1     
    print(f"your final bill in {sb}")           
elif size == "M":
    sb=20
    if add_pepperoni == "Y":
        sb += 3             
    if extra_cheese == "Y":
        sb += 1      
    print(f"your final bill in {sb}")     
elif size == "L":
    sb=25   
    if add_pepperoni == "Y":
        sb += 3                   
    if extra_cheese == "Y":
        sb += 1      
    print(f"your final bill in {sb}")      