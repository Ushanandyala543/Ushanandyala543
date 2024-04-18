import random
import string
l=eval(input("Enter the length of the password you require:"))
ro=eval(input("do you want numbers 1-->yes and 0-->no:"))
rt=eval(input("do you want special char 11-->yes and 00 -->no:"))
if(ro==1 and rt==11):
    set=string.ascii_letters+string.digits+string.punctuation
elif(ro==0 and rt==11):
    set=string.ascii_letters+string.punctuation
elif(ro==0 and rt==00):
    set=string.ascii_letters
elif(ro==1 and rt==00):
    set=string.ascii_letters+string.digits
p = ''.join(random.choices(set,k=l))
print("Your PASSWORD is:",p)