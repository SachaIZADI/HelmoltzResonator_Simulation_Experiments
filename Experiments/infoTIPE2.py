from matplotlib.pyplot import*


monfichier=open('Documents/liste de grandeurs autour de 10 s.txt','r')
tab=monfichier.readlines()
monfichier.close

n=len(tab)

A=[]
B=[]
T=[]


for k in range(n):
    tab[k]=tab[k].strip().split('\t')
    
    a=len(tab[k][0])
    x=''
    for j in range(a):
        if tab[k][0][j]!=',':
            x=x+tab[k][0][j]
        else:
            x=x+'.'
    A=A+[eval(x)]
    
    b=len(tab[k][1])
    y=''
    for j in range(b):
        if tab[k][1][j]!=',':
            y=y+tab[k][1][j]
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

plot(T,A)
plot(T,B)

N=len(A)
X=[]
Y=[]
t=[]

y=max(B)

for k in range(N-2):
    if A[k+1]>A[k] and A[k+1]>A[k+2] and A[k+1]>0:
        X=X+[A[k+1]]
        t=t+[T[k+1]]
        Y=Y+[y]


plot(t,X)
plot(t,Y)

m=len(X)
R=[]
for i in range(m):
    R=R+[20*log10(X[i]/Y[i])]

plot(t,R)

show()





