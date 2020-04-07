#CODE: TO PRINT FIBONACCI SERIES.
n=int(input("Enter the total number of terms you want in series:"));
if n<0:
    print("enter positive value only");
elif n==1:
    print(1);
else:
    print("Fibonacci series consisting",n,"terms is:");
    a=0;
    b=1;
    for i in range(0,n):
        print(a);
        c=a+b;
        a=b;
        b=c;

 
