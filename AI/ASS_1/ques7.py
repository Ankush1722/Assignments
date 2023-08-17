import ques7func
principal=int(input("Enter the principal amt.:"))
rate=float(input("Enter the rate of interest:"))
time=float(input("Enter time in years:"))
n=int(input("Enter number of times interest applied per years:"))
C=ques7func.fn_CI(principal,rate,time,n)
print(C)