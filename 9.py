altura = int(input("Introduce la altura del triangulo pro:  "))  
for i in range(1, altura + 1):  
    print(" ".join(str(2*j-1) for j in range(i, 0, -1)))  
