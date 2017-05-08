S = input("Enter Any type of String ........\n");
a =b =0;
for x in S:
    if(x.isdigit()):
        a=a+1;
    elif(x.isalpha()):
        b=b+1;
c =len(S)
print("Total digits in your sentence...",a)
print("Totla Alphabets in your Sentence...",b)
print("Total Letters in your Sentence...",c)