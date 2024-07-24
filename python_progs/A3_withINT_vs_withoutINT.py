"""
 NOTE: Input() accepts the input only in STRING format. So, if any mathematical calculation
 is to be performed , we need to convert the input to integer format.
 For converting the input to integer  format python provide a function called INT().
 """

#WITHOUT INT

a=input("Enter 1st number: ");
b=input("Enter 2nd number: ");
c=a+b;
print("Addition",c);

# WITH INT

a=int(input("Enter 1st number: "));
b=int(input("Enter 2nd number: "));
c=a+b;
print("Addition",c);


