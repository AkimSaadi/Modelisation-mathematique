from numpy.linalg import qr, det, inv
import numpy as np
def coef_diag(B,epsilon):
    n=len(B)
    for i in range (1,n):
        for j in range (i):
            if B[i,j]<epsilon:
                return False
    return True

def methode_qr (A,epsilon):
    B = np.copy(A)
    i=0
    while(coef_diag(B,epsilon) or i<1000):
        Q, R = qr(B)
        B = R.dot(Q)
        i+=1
    return B

def valeur_propre (B):
    n=len(B)
    X=[]
    for i in range (n):
        X.append(B[i,i])
    return X

M = 10*np.random.randn(4,4)
Mt=M.transpose()
P=M.dot(Mt)
if det (P) != 0 :
    PI= inv(P)
    D1 =np.array([[6,0,0,0],[0,5,0,0],[0,0,2,0],[0,0,0,1]]) 
    D2 =np.array([[5,0,0,0],[0,1,0,0],[0,0,2,0],[0,0,0,6]]) 
    D3 =np.array([[5,0,0,0],[0,3,0,0],[0,0,2,0],[0,0,0,3]])
    D4 =np.array([[5,0,0,0],[0,2,0,0],[0,0,0,1],[0,0,1,0]])
    A1 = P.dot(D1.dot(PI))
    A2 = P.dot(D2.dot(PI))
    A3 = P.dot(D3.dot(PI))
    A4 = P.dot(D4.dot(PI))
    A1_vp = valeur_propre(methode_qr(A1,10**(-6)))
    A2_vp = valeur_propre(methode_qr(A2,10**(-6)))
    A3_vp = valeur_propre(methode_qr(A3,10**(-6)))
    A4_vp = valeur_propre(methode_qr(A4,10**(-6)))
    print('Les valeurs propre de A1 sont approximativement:',A1_vp)
    print('Les valeurs propre de A2 sont approximativement:',A2_vp)
    print('Les valeurs propre de A3 sont approximativement:',A3_vp)
    print('Les valeurs propre de A4 sont approximativement:',A4_vp)
    print('On remarque que les approximations des valeurs propres de A4 ne sont pas bonnes')
    print('En prenant une sous matrice du resultat de la fonction "methode_qr", on retrouve toujours pas les valeurs propres, pour cela il aurait fallu prendre les 2 premiers lignes et colonnes')
    A4_vp = valeur_propre(methode_qr(A4,10**(-6))[2:,2:])
    print(A4_vp)
