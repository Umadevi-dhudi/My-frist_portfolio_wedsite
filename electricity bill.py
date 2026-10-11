units=int(input("enter electricity units"))
if units<=100:
 bill=units*1.50
elif units<=200:
 bill=(100*1.50)+((units-100)*2.50)
elif units<=300:
 bill=(100*1.50)+(100*2.50)+((units-200)*4)
else:
 bill=(100*1.50)+(100*2.50)+(100*4)+(units-300)*5
 print("electricity bill=",bill)
