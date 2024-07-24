#comment
"""helloo every one"""
print("every one love each other\n just like python love by every one")
#o multple comment ctrl +forward slash
# no yes 
# nonlocalno
# no
print("hello hushbu" ,sep='>', end='well')
print("everything is object n python")

#to replicate the line alt+shift+down
#alt+shift to change multiple values togeter


#typecasting convert one data type to another data type
a="1"
b="3"
print(a+b)
print(int (a)+ int (b))#explicit
#implicit python khud se karta hai high level se low level vice versa

#basic
age=int(input("enter your age"))
print("my age is",age)

if age>+18:
    print("i can drive")
elif(age<18):
    print("i cannot drive the car")
else:
    ("happy driving")
    
    
#strng and functions
a="anita tiwari"
print(a)

#methods
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.title())
print(a.split())
print(a.swapcase())

#loop
for i in a:
    print(i)
    
    
for  i  in range(0,6):
    print(a[i])  
    
#slicing  
print(a[0:5])
print(a[5:12])
print(a[1:12])
print(a[0:12])
print(a[0:6])
print(a[1:-8])
print(a[4:-1])
print(a[-12:-1])
print(a[0:12:1])
print(a[2:11:2])
print(a[4:7:1])
print(a[2:9:3])
print(a[0:11:1])
print(a[0:-3])
print(a[0:len(a)-3])
print(a[-2:-5])
print(a[len(a)-2:len(a)-5])
#string  slice gap is never negative
#reverse strng[::-1]
#0-12(0-[12-1]11)
#[0:-3] means [0:len(a)-3]
#negative slce o actual len of string se mnus kar dete ha
#[-2:-5]-[len(a)-2:len(a)-5]=10:

#basic calculator 
a=2
b=4
print("add two no ",a+b)
print("subtract to no",a-b)
print("multiplication of two no",a*b)
print("dvision of two no",a/b)
print("modulos of two no",a%b)
print("float division",a//b)

# by taken input 
a=int(input("enter the first no"))
b=int(input ("enter the second no"))
c=int(input("enter the choice 1.add,2.subtact,3.multiply,4,didvion,5.modulus,6.float"))

if c ==1:
        print("adtion is",a+b)
elif c ==2:
        print("substraction is",a-b)
elif c ==3:
        print("multipliction is",a*b)
elif c ==4:
        print("dividion is",a/b)
elif c ==5:
        print("modulus is",a%b)
elif c ==6:
        print("float division is",a//b)  
else:
        print("no")  
    
#fuction 
def calculator(a,b):
        return(a+b,a-b,a*c,a/b,a%b,a//b)
a=int(input("enter the first no"))
b=int(input("enter the second  no"))
c=calculator(a,b)
print(c)

###while and forloop
thickness = int(input(9)) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
    
('.|.').center(21,'-')
('.|.'*2).center(21,'-')
('.|.'*3).center(21,'-')
('WELCOME').center(21,'-')
('.|.'*3).center(21,'-')
('.|.'*2).center(21,'-')
('.|.').center(21,'-')


N,M=7,21

for i in range(1,N,2):
    print(('.|.'*i).center(M,'-'))
print(('WELCOME').center(M,'-'))

for i in range(N-2,-1,-2):
    print(('5'*i).center(M,'-'))
    
#loops    

    
i=1
while i<=100:
    print(i)
    i=i+1
    
i=100
while i>=1:
    print(i)
    i=i-1
# --------------------------------
n=3    
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1
    
#----------------------------------------    
list=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(list):
    print(list[i])
    i=i+1
    #----------------------------------
    
list=(1,4,9,16,25,36,49,64,81,100)
x=36 
i=0

while i<len(list):
    if list[i]==x:
        print("found at index",i)
        break
    else:
        print("finding")
    i=i+1
    name=("khushbu",1,3,"tiwari")
    for i in name:
        print(i)
#_-------------------------   
    l=[1,2,3,4,5]
    for i in l:
        print(i)
#
    str="ankita"
    for i in str:
        print(i)
#
list=(1,4,9,16,25,36,49,64,81,100)
x=36
for i in list:
    if i==x:
        print(i)
#
    n=5
    sum=0
    for i in range(1,n+1):
        sum=sum+i
        
    print(sum)
    
 #   
    n=5
    sum=1
    for i in range(1,n+1):
        sum=sum*i
        
    print(sum)
#
n=7  
    
for i in range(1,n,2):
    print(('5').center(21,'-'))



a=list["abcdefghijklmnopqrstuvwxyz"]
print(a)




    
   
