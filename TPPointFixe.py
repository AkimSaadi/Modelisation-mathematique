from math import exp, log
def g (x):
    return x**2 - 3

def g_seconde (x):
    return 2*x

def f (x) :
    return x - g(x)

def methode_point_fixe (fct,x0) :
    print("point fixe standard :",x0,sep=' ',end=' ')
    x=x0
    for i in range (8):
        x = fct(x)
        if (x>100000000 or x<-100000000) :
            print("%e"%x,end=' ')
        else :
          print(round(x,7),end=' ')  
    print('\n')

def test (a,b):
    if (abs(a-b)<10**(-6)):
        return True
    else : 
        return False

def inverse (x) :
    return 1/x

def newton (fct,drv,x0):
    i_max = 100
    x=x0
    i=0
    x_temp = 10000
    print("Newton :",x0,sep=' ',end=' ')
    while(test(x,x_temp)==False and i<i_max):
        x_temp=x
        x = x-1*(fct(x)/drv(x))
        print(round(x,7),end=' ')
        i+=1
    print('nombre d iteration :',i,sep=' ',end='\n' )
    
        
methode_point_fixe(f,1)
methode_point_fixe(f,2)
methode_point_fixe(f,4)
methode_point_fixe(f,8)

print ('Pour x0=1 :')
newton(g,g_seconde,1)
print ('Pour x0=2 :')
newton(g,g_seconde,2)
print ('Pour x0=4 :')
newton(g,g_seconde,4)
print ('Pour x0=8 :')
newton(g,g_seconde,8)

