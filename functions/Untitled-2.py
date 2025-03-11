""""Write a program that defines a function compute() that calculates the value of n + nn + nnn + nnnn,
where n is digit received by the function. test the function for digits 4 to 7."""""
def compute():
    n=int(input("number:"))
    sum=(n+n*n+n*n*n+n*n*n*n)
    print(sum)
compute()
compute()
compute()
compute()