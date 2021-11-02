def obtene_fizzbuff(n):#definimos l funcion fizzbuff
    if n % 3 == 0 and   n % 5 == 0  : #le damos una condion para  obtener fizzbuff

        return "fizzbuff"
    elif n % 3 == 0:#si es multriplo de 34 obtendra fizz
        return "fizz"
    elif n % 5 == 0 :#si es de 5 buzz
        return"buzz"
    else :
        return n #si es de ambos fizzzbuf
resultado=obtene_fizzbuff(15)

print(resultado)


