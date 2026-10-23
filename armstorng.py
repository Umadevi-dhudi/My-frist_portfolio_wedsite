
num=int(input("Enter value"))
temp=num
sum=0
while temp > 0:
   digit=temp % 10
   sum=sum+digit**3
   temp=temp//10
if sum == num :
  print("armstorng")
else:
  print("not armstorng")