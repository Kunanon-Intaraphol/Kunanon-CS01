import numpy as np
Lenght = []
Row = []
a = int(input("Enter your Row: "))
b = int(input("Enter your Lenght: "))
c = a*b
print("Input Number first Array: ")
for i in range(c):
    Lenght+=[int(input(""))]
NewRow = np.asarray(Row)
print("Input Second Array: ")
for a in range(c):
    Row+=[int(input(""))]
NewRow = np.asarray(Row)
NewLenght = np.asarray(Lenght)
NewRowNumpy = NewLenght.reshape(int(a),b)
print(NewRowNumpy)
NewLenghtNumpy = NewLenght.reshape(int(b),a)
print(NewLenghtNumpy)
z = np.add(NewRowNumpy,NewLenghtNumpy)
print(z)