n=int(input())
m=int(input())
z=str(n)
x=str(m)
f=len(z)
h=len(x)
if f>h:
  qw="0"*(f-h)
  x=qw+x
elif h>f:
  qw="0"*(h-f)               #padding
  z=qw+z

ner=len(z)
m=ner//2+ner%2
a=z[:m]
b=z[m:]
c=x[:m]
d=x[m:]
an=int(a)
bn=int(b)
cn=int(c)
dn=int(d)
bnm=2*m
answer=pow(10,bnm)*an*cn+bn*dn+pow(10,m)*(an*dn+bn*cn)
print(answer)

  
