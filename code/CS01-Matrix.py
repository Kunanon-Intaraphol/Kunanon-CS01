import numpy as np
Lenght = []
Row = []
m = int(input("Enter your Row: "))
n = int(input("Enter your Lenght: "))
v = m*n
print("Input Number first Array: ")
for i in range(v):
    Lenght+=[int(input(""))]
NewRow = np.asarray(Row)
print("Input Second Array: ")
for a in range(v):
    Row+=[int(input(""))]
NewRow = np.asarray(Row)
NewLenght = np.asarray(Lenght)
NewRowNumpy = NewLenght.reshape(int(m),n)
print(NewRowNumpy)
NewLenghtNumpy = NewLenght.reshape(int(n),m)
print(NewLenghtNumpy)
z = np.add(NewRowNumpy,NewLenghtNumpy)
print(z)