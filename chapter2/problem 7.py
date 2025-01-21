def year():
    a = int(input("Enter year: "))
    if a%4==0 or a%100==0 or a%400:
        print("the year is a leap year")
    else:
        print("the year is not a leap year")
year()
year()
