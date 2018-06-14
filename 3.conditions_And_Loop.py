#getting input from the user

donut= int(input("do you have 0 donuts or 1? "))

#using conditions

if donut==1:
    print("eat the donut")
else:
    print("can't eat the donut")


#another program
    
price=int(input("enter the price of a donut : Rs.. "))
quantity=int(input("enter th e no. of donuts: "))

amount = price*quantity

if amount>100:
    print("Yayy idscount of 10% is appiles")
    discount=amount*10/100
    amount=amount-discount
    
print("your total amount is Rs: ",amount)
