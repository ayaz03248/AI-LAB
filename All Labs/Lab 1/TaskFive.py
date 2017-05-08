year = int(input("Enter any year to check whether is leap year or Not\n"))

if(year%4 == 0):
 if(year%100 == 0):
    if(year%400 == 0):
     print("This is Leap Year");
    else:
     print("This is Not Leap Year");
 else:
   print("This is Leap Year....");
else:
    print("This Year is Not A leap Year...");