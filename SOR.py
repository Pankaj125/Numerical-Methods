def main():
    print ("{:<8} {:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format('Num','u','v','w','x','y','z'))
    N = 1
    SOR = 1.1
    Tolerance = 0.01
    calculateEqn(SOR, Tolerance, N)

def s1(v,z):
    return (5-z+2*v)/6 
def s2(u,w,e):
    return (3+2*u+2*w-e)/6 
def s3(v,x):
    return (1+v+x)/3 
def s4(w,y):
    return (1+w+y)/3 
def s5(v,x,z):
    return (3-v+2*x+2*z)/6 
def s6(u,y):
    return (5-u+2*y)/6 

def calculateEqn(SOR,Tolerance,num):
    u0,v0,w0,x0,y0,z0 = 0,0,0,0,0,0 
    Tolerance1,Tolerance2,Tolerance3,Tolerance4,Tolerance5,Tolerance6 = 1,1,1,1,1,1  
    while Tolerance1>Tolerance and Tolerance2>Tolerance and Tolerance3>Tolerance and Tolerance4>Tolerance and Tolerance5>Tolerance and Tolerance6>Tolerance : 
        u1 = (1-SOR)*u0+SOR*s1(v0,z0)
        v1 = (1-SOR)*v0+SOR*s2(u1,w0,y0) 
        w1 = (1-SOR)*w0+SOR*s3(v1,x0) 
        x1 = (1-SOR)*x0+SOR*s4(w1,y0) 
        y1 = (1-SOR)*y0+SOR*s5(v1,x1,z0) 
        z1 = (1-SOR)*z0+SOR*s6(u1,y1) 
        
        print ("{:<8} {:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(num,round(u1,3),round(v1,3),round(w1,3),round(x1,3),round(y1,3),round(z1,3)))
        Tolerance1,Tolerance2,Tolerance3,Tolerance4,Tolerance5,Tolerance6 = abs(u0-u1),abs(v0-v1),abs(w0-w1),abs(x0-x1),abs(y0-y1),abs(z0-z1)
        
        num += 1 
        u0,v0,w0,x0,y0,z0 = u1,v1,w1,x1,y1,z1 
    print('Output: a=%0.3f b=%0.3f c=%0.3f p=%0.3f q=%0.3f r=%0.3f'% (u1,v1,w1,x1,y1,z1)) 
    
if __name__ == '__main__':
    main()

