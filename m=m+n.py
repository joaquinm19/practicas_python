def multiplicacion5(N): #DEFINIMOS UNA FUNCION
    M = 0
    M = M + N
    M = M + N
    M = M + N
    M = M + N
    M = M + N
    
    return M 
resultado=multiplicacion5(4) #LLAMAMOS LA FUNCION Y LE PONEMOS UN VALOR 
print(resultado) 


#CICLO


def multiplicaion5(N):

    M = 0
    for i in range (3): #desde cero hasta el rango 3 en este ejemplo
        M = M + N 
        return M

for i in range (5) :#la sumatoria de 0,,1,2,3,4,
    print (i)



def elevar3(n): #definimos la funcion
    m = 1
    m = m + n
    m = m + n
    m = m + n
    m = m + n
    m = m + n
    return m     #para que el valor de cada vuleta retorne en m
        
resultado=elevar3(3)  #llamamos la funcion y leponemos valor

print(resultado) #comando print no es funcion



#reutilizacion de funciones

def mulplicar5yelevar3(n):
    m=0
    m = m + n
    m = m + n
    m = m + n
    m = m + n
    m = m + n
    return elevar3(multiplicacion5(n))

resultado=mulplicar5yelevar3(1,2)

print(resultado)










