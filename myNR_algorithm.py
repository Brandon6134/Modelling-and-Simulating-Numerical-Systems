
def myNR(myfun,x0,myfund=None):
    
    #error defined with large value, so first if statement/calculation
    #always runs
    error=100


    for i in range(1,100):

        #if no derivative function given and relative error is not 
        #below 10e-6
        if myfund==None and error>10e-6:
            #below line uses secant method to estimate derivative
            deriv=(myfun(x0*1.01)-myfun(x0))/(x0*1.01-x0)

            #execute newton-raphson method
            x_new=x0-myfun(x0)/deriv

        #if derivative function is given and relative error is not
        #below 10e-6
        elif error>10e-6:
            x_new=x0-myfun(x0)/myfund(x0)
        
        #if relative error is below 10e-6, return guess for root
        else:
            return x_new

        #calculate relative approximate error
        error = abs((x_new-x0)/x_new)
        
        #set new calculated x value as the x(i-1) value
        x0=x_new

def testFunc(x):
    return x**5 - 11*x**4 +43*x**3-73*x**2 +56*x-16

def derivTestFunc(x):
    return 5*x**4 - 44*x**3 +43*3*x**2 -73*2*x+56

if __name__ =="__main__":
    print(myNR(testFunc,-2))
    print(myNR(testFunc,-2,derivTestFunc))

