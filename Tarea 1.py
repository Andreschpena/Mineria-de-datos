#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Ejercicio 1
#Realiza una variable con tu matricula y realiza una secuencia de imprimir con tu nombre y tu matricula concatenados.
Mat = int(input("Introduce tu matrícula: "))
Nombre = input("Introduce tu nombre: ")
print (Nombre, Mat)


# In[6]:


#Ejercicio 2
#Pidiendo el input del usuario pide dos números y crea una pequeña calculadora con los operadores básicos de suma, resta, multiplicación, división, y exponente.
a = float(input("ingresa un número: "))
b = float(input("ingresa otro número: "))
c = a+b
d = a-b
e = a/b
f = a*b
print("La suma es: ",c)
print("La resta es: ",d)
print("La división es: ",e)
print("El producto es: ",f)


# In[9]:


#Ejercicio 3
#Con loop while o for, realiza una lista de 10 numeros multiplos de 3, y después realiza una función de loop que sume todos los números dentro del arreglo.
a = 1
s = 0
for i in range (1,11):
    x = i*3
    s = s+x
    print(x)
print ("La suma de los numeros es: ", s)


# In[25]:


#Ejercicio 4
#Con una función de if else, revisar si un número es par o es impar.
#Con una función de if else, revisar si un número es primo o no.
a = int(input("Introduce un número: "))
if a%2 != 0:
    print(a, "no es un par")
else:
    print(a, "si es par")
    
valor= range(2,a)
contador = 0
for n in valor:
  if a % n == 0:
    contador +=1
    print("divisor:", n)
 
if contador > 0 :
  print("El número no es primo" )
else:
  print("El número es primo")


# In[16]:


#Ejercicio 5
#Utilizando diferentes clases en python, crea una calculadora con los operadores básicos de suma, resta, multiplicación, división, y exponente.
class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=cal(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 
 
print()
#Fuente: https://www.sanfoundry.com/python-program-class-performs-basic-calculator-operations/


# In[18]:


#Crear una tupla con valores enteros imprimir el primer y ultimo valor.
t=(1, 2, 3, 4, 5, 6)
print ("el primer valor de la tupla es: ", t[0])
print ("el último valor de la tupla es: ", t[5])


# In[36]:


#Crear una variable flotante, integer, boleana y compleja e imprimir el tipo de variable que es.
a = 5
b = 1.62
c = 4 + 3j
d = False
print("La variable a es de tipo: ", type(a))
print("La variable b es de tipo: ", type (b))
print("La variable c es de tipo: ", type (c))
print("La variable d es de tipo: ", type (d))


# In[37]:


#Añadir 3 valores de string a la tupla.
#No se puede


# In[39]:


#Verificar si una variable existe dentro de la tupla.
t=(1, 2, 3, 4, 5, 6)
print("¿El 5 está en la tupla?", 5 in t)
print("¿El 10 está en la tupla?", 10 in t)


# In[53]:


#Crear una lista con 40 elementos aleatorios enteros
import random as r
L = []
for i in range (0,39):
    L.append(r.randint(1, 100))
print (L)


# In[71]:


#Creamos una lista de 40 elementos enteros aleatorios
import random as r
L = []
for i in range (0,39):
    L.append(r.randint(1, 100))

#Definimos una funcion para reconocer los numeros pares e imprimimos la lista
def num_pares(numeros):
    pares = []
    
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
            
    return pares
listapares = num_pares(L)

#Hacemos lo mismo para impares
def num_impares(numeros):
    impares = []
    
    for n in numeros:
        if n % 2 != 0:
            impares.append(n)
            
    return impares
listaimpares = num_impares(L)

#Imprimimos ambas listas
print ("La lista de pares es: ", listapares)
print ("La lista de impares es: ", listaimpares)

#Crear dos variables con la longitud de ambas listas nuevas e imprimir las variables.
x=[]
y=[]

for i in range(0,len(listapares)):
        x.append(listapares[i])
    
for i in range(0,len(listaimpares)):
        y.append(listaimpares[i])

#Ordenar pares de mayor a menor e impares de menor a mayor
x.sort()
y.sort(reverse=True)
print(x)
print(y)

#


# In[82]:


#Crear un diccionario de 6 personas que conozcas con su primer nombre y su edad.
diccionario = {'nombre' : ["Andres","Karime","Patricia","Jesús","Juan","Mauricio"], "edad" : ["20","19","45","47","21","22"]}
print(diccionario["nombre"])

print()
#Crear una lista con los valores de la edad y reacomodar la lista de menor a mayor valor.
x = []

for i in range(0,6):
    x.append(diccionario["edad"][i])
x.sort()
print(x)

print()
#Usando el diccionario y un loop, imprimir solo los nombres.

y = []
for i in range(0,6):
    y.append(diccionario["nombre"][i])
print(y)

print()
#Añadir dos personas nuevas a tu diccionario, incluyendo edad.


# In[106]:


#Crea un set con 100 numeros aleatorios enteros del 1 al 25
import random as r
L = []
for i in range (0,100):
    L.append(r.randint(1, 25))
s = set(L)
print(s)
print()
#Comprueba la longitud de tu set.


print(len(s))
print()

#Crea una lista de 5 numeros aleatorios del 1 al 10 y comprueba si cada valor aparece en el set inicial.
M = []
for i in range (0,5):
    M.append(r.randint(1, 25))
print(M)


# In[ ]:




