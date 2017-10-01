from math import*
from matplotlib.pyplot import*


monfichier=open('Documents/autre balayage.txt','r')
tab=monfichier.readlines()
monfichier.close


n=len(tab)

A=[]
B=[]
T=[]


for k in range(n):
    tab[k]=tab[k].strip().split('\t')
    
    a=len(tab[k][1])
    x=''
    for j in range(a):
        if tab[k][1][j]!=',':
            x=x+tab[k][1][j]
        else:
            x=x+'.'
    A=A+[eval(x)]
    
    b=len(tab[k][0])
    y=''
    for j in range(b):
        if tab[k][0][j]!=',':
            y=y+tab[k][0][j]
        else:
            y=y+'.'
    B=B+[eval(y)]
    
    t=len(tab[k][2])
    z=''
    for j in range(t):
        if tab[k][2][j]!=',':
            z=z+tab[k][2][j]
        else:
            z=z+'.'
    T=T+[eval(z)]

#plot(T,B)
#plot(T,A)


N=len(A)
X=[]
Y=[]
t=[]

y=max(B)

for k in range(N-2):
    if A[k+1]>A[k] and A[k+1]>A[k+2] and A[k+1]>0:
        X=X+[A[k+1]]
        t=t+[T[k+1]]

for k in range(N-2):
    if B[k+1]>B[k] and B[k+1]>B[k+2] and B[k+1]>0:
        Y=Y+[B[k+1]]
Y[len(t):len(Y)]=[]


#plot(t,X)
#plot(t,Y)

m=len(X)
R=[]
for i in range(m):
    R=R+[20*log10(X[i]/Y[i])]

l=len(t)
F=[]
for k in range(l):
    F=F+[100+5*t[k]]

plot(F,R,'darkred')
grid()
xlabel('Fréquence (Hz)')
ylabel('G(f) (dB)')
title ('Courbe expérimentale du gain en fonction de la fréquence')

show()





