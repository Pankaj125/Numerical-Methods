def main():
    print ("{:<8} {:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format('N','u','v','w','x','y','z'))
    N = 1
    Tolerance = 0.01
    calculateEqn(Tolerance, N)

def g1(v,z):
    return (5-z+2*v)/6 
def g2(u,w,y):
    return (3+2*u+2*w-y)/6 
def g3(v,x):
    return (1+v+x)/3 
def g4(w,e):
    return (1+w+e)/3 
def g5(v,x,z):
    return (3-v+2*x+2*z)/6 
def g6(u,y):
    return (5-u+2*y)/6 


def calculateEqn(Tolerance,n):
    u0,v0,w0,x0,y0,z0 = 0,0,0,0,0,0 
    Tolerance1,Tolerance2,Tolerance3,Tolerance4,Tolerance5,Tolerance6 = 1,1,1,1,1,1  
    while Tolerance<Tolerance1 and Tolerance<Tolerance2 and Tolerance<Tolerance3 and Tolerance<Tolerance4 and Tolerance<Tolerance5 and Tolerance<Tolerance6: 
        u1 = g1(v0,z0)
        v1 = g2(u1,w0,y0) 
        w1 = g3(v1,x0) 
        x1 = g4(w1,y0) 
        y1 = g5(v1,x1,z0) 
        z1 = g6(u1,y1) 
        print ("{:<8} {:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(n,round(u1,3),round(v1,3),round(w1,3),round(x1,3),round(y1,3),round(z1,3)))
        Tolerance1,Tolerance2,Tolerance3,Tolerance4,Tolerance5,Tolerance6 = abs(u0-u1),abs(v0-v1),abs(w0-w1),abs(x0-x1),abs(y0-y1),abs(z0-z1) 
        n += 1 
        u0,v0,w0,x0,y0,z0 = u1,v1,w1,x1,y1,z1 
    print('Output: u=%0.3f v=%0.3f w=%0.3f x=%0.3f y=%0.3f z=%0.3f'% (u1,v1,w1,x1,y1,z1)) 

if __name__ == '__main__':
    main()

