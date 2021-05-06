print("welcoe to the tip calculator")
bill= input("what was the total bill ?")
tip= input("what percentage tip would you like to give ? 10, 12, or 15 ?")
people= input("howmany people to split the bill ?")
bill1=float(bill)
tip1=float(tip)
people1=float(people)
allbill = (((bill1*tip1/100)+bill1)/people1)
allbill1 = round (allbill , 2)
print (allbill1)


