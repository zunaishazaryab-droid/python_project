a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

a=4>2
print(a)
b=4<2
print(b)
c=4>=4
print(c)
d=4>=2
print(d)
e=2!=2
print(e)
f=2!=2
print(f)
g=2==2
print(g)

marks=int(input("enter your marks:"))
print(type(marks))
if marks>90:
    print("your grade is A")
elif marks>80:
    print("your grade is B")
elif marks>70:
    print("your grade is C")
else:
    print("your grade is D")

marks=int(input("enter overall marks percentage:"))
cs_marks=int(input("enter overall cs marks percentage:"))
if marks>=88 or cs_marks>=88:
    print("you are eligible for admission")
else:
    print("you are eligible for admission")

marks=int(input("enter overall marks percentage:"))
cs_marks=int(input("enter overall cs marks percentage:"))
if marks>=88 and cs_marks>=88:
    print("you are eligible for admission")
else:
    print("you are eligible for admission")

year=int(input("enter the year"))
print(type(year))
if year % 4==0:
    if year % 100==0:
        if year % 400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
     print("not leap year")


