from random import*
length=randint(5,10)
x=[0]*length
sum=0
for i in range(length):
    x[i]=randint(1,100)
    print(x[i],end=' ')
y=[x[i]for i in range(length)]
print(y,end=' ')
