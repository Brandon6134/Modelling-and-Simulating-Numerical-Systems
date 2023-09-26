#Brandon Kong, 20885867

#Function f(x), the summation
def f(x,tol=10e-5):
    #Sum is the variable that holds the sum of all components
    sum=0

    #Loops the summation until tolerance value is reached, then returns sum
    for n in range(0,100):
        sum+=pow(x,n)
        if n>0:
            if abs(pow(x,n)-pow(x,n-1))<tol:
                return sum
            
print(f(-0.5))