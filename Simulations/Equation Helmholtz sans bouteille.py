from matplotlib.pyplot import*
from math import*

h=0.01 # pas de discrétisation
w=120*2*pi # pulsation de travail
c=340 # vitesse du son
mu0=1.2 # masse volumique de l'air

S=pi*(10**(-2))**2 #section du goulot
col=8*10**(-2) #longueur du goulot
V=0.75*10**(-3) # Volume bouteille


L=mu0*col/S # partie inductive de ZH
C=V/mu0/c**2 # partie capacitive de ZH

M=[[1 for i in range (101)] for j in range(101)] #définition de M_0
A=[[1 for i in range (101)] for j in range(101)] #définition de A_0, matrice "témoin", ie sans résonateur
l=len(M)

X0=l//2 -5 # abscisse début du résonateur : milieu et 1/10 de la longueur totale

for K in range(5000):
    #Copie de la Matrice M_n
    N=[[1 for i in range (101)] for j in range(101)]
    for i in range(0,l):
        for j in range(0,l):
            N[i][j]=M[i][j]
    #Copie de la Matrice A_n
    B=[[1 for i in range (101)] for j in range(101)]
    for i in range(0,l):
        for j in range(0,l):
            B[i][j]=A[i][j]
    
    #Conditions aux limites du résonateur
    for j in range(X0,X0+10+1):
        M[l-1][j]=0
        #M[l-1][j]=(N[l-2][j])*(-(1/C-L*w**2)/(mu0*h*w**2-(1/C-L*w**2)))
        #M[l-1][j]=(N[l-2][j])/(1-mu0*h*(L*C*w**2-1)/L)
    
    #Conditions aux limites du haut parleur
    for j in range(l):
        M[0][j]=N[1][j]-2*h
        A[0][j]=B[1][j]-2*h
    
    
    #Conditions aux limites du mur
    for i in range(l-1):
        M[i][0]=N[i][1]
        M[i][l-1]=N[i][l-2]
        A[i][0]=B[i][1]
        A[i][l-1]=B[i][l-2]
    
    # Conditions aux limites du mur hors résonateur
    for j in range (l-1):
        if j<X0:
            M[l-1][j]=N[l-1][j]
        elif j>X0+10:
            M[l-1][j]=N[l-1][j]
        A[l-1][j]=B[l-1][j]
    
    #Calcul du coeur de la Matrice M_n+1
    for i in range(1,l-1):
        for j in range(1,l-1):
            M[i][j]=(1/(4-(w*h/c)**2))*(N[i+1][j]+N[i-1][j]+N[i][j+1]+N[i][j-1])
            #M[i][j]=(1/(4+(w*h/c)**2))*(N[i+1][j]+N[i-1][j]+N[i][j+1]+N[i][j-1])
            A[i][j]=(1/(4-(w*h/c)**2))*(B[i+1][j]+B[i-1][j]+B[i][j+1]+B[i][j-1])
    
P=[[M[i][j]/A[i][j] for j in range (101)] for i in range(101)]

imshow(M)
colorbar()
#X=[k for k in range(100)]
#plot(M[50],X)
show()