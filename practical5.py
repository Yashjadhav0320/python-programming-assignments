price1= float(input("enter price of product 1: "))
quantity1= int(input("enter quantity of product 1: "))

price2= float(input("enter price of product 2: "))
quantity2= int(input("enter quantity of product 2:"))

price3= float(input("enter price of product 3: "))
quantity3= float(input("enter quantity of product 3: "))

subtotal= (price1 * quantity1)+(price2 * quantity2)+ (price3 * quantity3)

discount = subtotal * 10/100

amount= subtotal - discount

gst= amount * 18/100

final_amount= amount + gst


print("subtotal:",subtotal)
print("Discount:",discount)
print("GST:",gst)
print("final Payable Amount:",final_amount)
