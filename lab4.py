names={}
n=int(input("enter no.of names :"))
for i in range(n):
    names[i+1]=input("enter name  ")
name=list(names.values())
pos=int(input("enter position : "))
name.sort(key=lambda x:x[pos])
print(name)