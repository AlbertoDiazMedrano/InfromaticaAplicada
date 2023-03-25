
### Operador +.

#python
print("Resultados de sumas aritmeticas >INT<")
print("-----------------------------------")
a = 7 + 3
print(type(a))                                       #10
a = 5
b = 3
c = a + b
print(type(c))                                        #8
print(type(3+4))                                      #7
print("-----------------------------------")

print("Resultados de resta aritmeticas >INT<")
print("-----------------------------------")
a = 6 - 2
print(type(a))                                        #4
a = 5
b = 3
c = a - b
print(type(c))                                        #2
print(type(2-6))                                      #-4
print("-----------------------------------")

### Operador *.
print("Resultados de multiplicacion aritmeticas CLASE <INT>")
#python
print("-----------------------------------")
a = 3 * 4
print(a)            #12
a = 6
b = 3
c = a * b               #18
print(c)
print(5*7)              #35
print("-----------------------------------")

print("Resultados de dicivion aritmeticas   clase float")
### Operador /.
print("-----------------------------------")
#python
a = 6 / 2
print(type(a))            # 3
a = 5
b = 3
c = a / b
print(type(c))            #1.666
print(type(10/3))         #3.3333
#
print("-----------------------------------")
### Operador %.

print("Resultados porcentuales clase int ")
print("-----------------------------------")
#python
a = 8 % 4
print(type(a))            #0
a = 9
b = 2
c = a % b
print(type(c))            #1
print(type(6%3))          #0
#
print("-----------------------------------")
### Operador **.


print("Resultados de potencias  clase int")
#python
print("-----------------------------------")
a = 3 ** 3
print(type(a))            #27
a = 2
b = 4
c = a ** b
print(type(c))            #16
print(type(4**3))         #64
print("-----------------------------------")

#Operador <.

#python
print("Resultados de menor que   clase bool")
print("-----------------------------------")
a = 3 < 3
print(type(a))            #FALSE
a = 2
b = 4
c = a < b
print(type(c))            #TRUE
print(type(4<3))          #FALSE
#
print("-----------------------------------")
### Operador >.
print("Resultados de mayor que  clase bool")
#python
print("-----------------------------------")
a = 4 > 2
print(type(a))            #TRUE
a = 5
b = 7
c = a > b
print(type(c))            #FALSE
print(type(9>2))          #FALSE
#
print("-----------------------------------")
### Operador ==.

#python
print("Resultados de igual a  clase bool")
print("-----------------------------------")
a = 5 == 5
print(type(a))            #TRUE
a = 6
b = 9
c = a == b
print(type(c))            #TRUE
print(type(6==2))         #FALSE
#
print("-----------------------------------")
# Operador !=.

#python
print("Resultados de diferente a clase bool")
print("-----------------------------------")
a = 4 != 2
print(type(a))            #FALSE
a = 5
b = 3
c = a != b
print(type(c))            #FALSE
print(type(8!=8))         #FALSE
#
print("-----------------------------------")
### Operador <=.

print("Resultados de menor o igual  clase bool")
#python
print("-----------------------------------")
a = 5 <= 3
print(type(a))            #FALSE
x = 7
y = 5
z = x <= y
print(type(z))            #FALSE
print(type(9<=4))         #FALSE
#
print("-----------------------------------")
### Operador >=.

#python
print("Resultados de mayor o igual a clase bool")
print("-----------------------------------")
a = 2 >= 8
print(type(a))        #FALSE
a = 3
b = 4
c = a >= b
print(type(c))        #FALSE
print(type(7>=3))     #TRUE
#
print("-----------------------------------")

## Expresiones lógicas.


#python
print("Resultados de la compuerta AND  clase bool")
print("-----------------------------------")
print(type(4-1==3 and 5>6))       #FALSE
print(type(6+7 > 11 and 3==3))    #TRUE
#
print("-----------------------------------")
# Operador or.
print("Resultados de la compuerta OR clase bool")
#python
print("-----------------------------------")
print(type(4-1==3 or 5>6))        #TRUE
print(type(6+7 > 11 or 3==3))     #TRUE
#
print("-----------------------------------")
### Operador not.

#python
print("Resultados de la compuerta NOT clase bool")
print("-----------------------------------")
print(type(not 5>6))      #true
print(type(not 5>4))      #FALSE
#
print("-----------------------------------")
## Expresiones de carácter

#A diferencia de las demás expresiones no existe un operador estático sino una búsqueda de secuencias, números o caracteres dentro de una variable.

#Estas expresiones de búsqueda comúnmente llamadas expresiones regulares, sirven para captar ciertos elementos o patrones dentro de un valor

#python
print("-----------------------------------")
import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
re.findall(type(patron, frase))
#
print("-----------------------------------")