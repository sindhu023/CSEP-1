from matplotlib import pyplot as pt
def compound_interest(p,r,t):
    a=[]
    x=[]
    for i in range(1,n+1):
        x.append(i)
        a=p*(1+(r/100))**(i*t)
        ci=a-p
        a.append(ci)
    pt.plot(x,a)
    return ci
p=int(input("enter the principle amount:"))
r=int(input("enter the rate of interest:"))
t=int(input("enter time"))
n=int(input("enter the compound interest interval:"))
print("compound interest is" ,compound_interest(p,r,t))
