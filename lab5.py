s=input("enter a string:")
d={}
if s.isspace():
    print("String is empty")
elif s.isdigit():
    print("enter characters only")
else:
    for i in s:
        d[i]=s.count(i)
    print(d)