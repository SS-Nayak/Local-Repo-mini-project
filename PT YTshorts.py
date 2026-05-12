'''Gender= input("enter your Gen: ")
Salary= int(input("enter your Salary: "))

if Gender == "m" and Salary==10000:
    bonos=20000
    print("Your monthly Pay is: ", Salary+bonos)
elif Gender=="f" and Salary==10000:
        bonos=5000
        print("Your monthly Salary is: ",Salary+bonos)'''

#------------  JANUARY 2023  ---------------------

#FIND THE UPPERCASE & LOWERCASE LETTER IN A STRING
'''a= input("enter name: ")
lcharx=ucharx=0

for chare in a:
    if chare.islower()==True:
        lcharx+=1   
    elif chare.isupper()==True:
        ucharx+=1
print("total upper: ",lcharx)  
print("total lower",ucharx)  '''

'''A = input("eneter name: ")
lcase=0
ucase=0
dcase=0
scase=0

for name in A:
    if name.islower():
        lcase=lcase+1
    elif name.isupper():
        ucase=ucase+1
    elif name.isdigit():
        dcase=dcase+1
    else: 
        scase=scase+1

print("lowercase is : ", lcase)
print("upper case is : ", ucase)
print("dcase is : ", dcase)
print("scase is : ",scase)'''

#write a python program to fine the Divisible of 2 and multiply of 5
'''for number in range (1, 101):
    if number%2==0 and number%5==0:
        print(number)'''
'''def muldiv():
    for i in range (1, 100):
        if i%2==0 and i%5==0:
            print(i)
muldiv()'''

#WRITE A PYTHON PROGRAME TO FIND THE FEBONACCI SERIES OF A NUMBER USING FUNCTION
'''def febonacci(n):
    a, b= 0,1
    print(a, b, end=",")
    for i in range (2, n):
        c=a+b
        a=b
        b=c
        print(c, end=",")
febonacci(10)'''

#WRITE A PYTHON PROGRAME TO FIND THE SAME ELEMENT IN TWO LIST
'''def mathcase():
    a=[1,3,5,8]
    b=[9,7,3,1]
    for i in a:
        for j in b:
            if i==j:
                print(i)
mathcase()'''

# Write a programe to Find the First Gretest Devisior of a number, take input from user

'''a=int(input("Enter fst num: "))
b=int(input("Enter snd num: "))

while(b!=0):
    temp=b
    b=a%b
    a=temp
print(a)'''

'''e=int(input("Enter A Number:  "))
n=int(input("Enter 2nd Number:  "))

sum=0
for i in range(n):
    sum=sum+e
    print(sum)'''

'''l1= "sudh", "apple", "banana"
l2= "cherry", "mango", "stabery"

print(" ".join([l1+l2]))'''

for i in range(1,10):
    print("i love")
