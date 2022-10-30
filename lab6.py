import numpy as np
row1,col1=list(map(int,input("enter rows and columns").split()))
A=np.array(list(map(int,input("enter matrix A").split())))
A.shape=(int(row1),int(col1))
print(A)
row2,col2=list(map(int,input("enter row and col").split()))
B=np.array(list(map(int,input("enetr matrix B").split())))
B.shape=(int(row2),int(col2))
print(B)
if(row1==row2 and col1==col2):
   print("addition=",np.add(A,B))
   print("element by element multiplication ",np.multiply(A,B))
else:
   print("addition and multiplication is not possible")
if(col1==row2):
   print("multiplication=",np.dot(A,B))
else:
   print("multiplication is not possible")