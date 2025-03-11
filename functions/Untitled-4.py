""""Write a program that defines a function sum_avg() to accept marks of five subjects and calculates
total and average. It should return directly both values"""""
def sum_avg():
    sub1=int(input("enter marks for sub 1:"))
    sub2=int(input("enter marks for sub 2:"))
    sub3=int(input("enter marks for sub 3:"))
    sub4=int(input("enter marks for sub 4:"))
    sub5=int(input("enter marks for sub 5:"))
    total=sub1+sub2+sub3+sub4+sub5
    avg=(sub1+sub2+sub3+sub4+sub5)/5
    print("total:",total)
    print("avg:",avg)
sum_avg()    