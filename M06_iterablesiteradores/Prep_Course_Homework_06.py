#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
lista = []
i = -15
while i <= -1:
    lista.append(i)
    i += 1
print(lista)





# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:

lista = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
n = 0
while n < len(lista):
    if lista[n] % 2 == 0:
        print(lista[n])
    n += 1



# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

lista = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
for pares in lista:
    if pares % 2 == 0:
        print(pares)



# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:

lista = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
for pares in lista[:3]:
     print(pares)


# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:

lista = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
for i, e in enumerate(lista):
    print(i, e)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
lista = [1,2,5,7,8,10,13,14,15,17,20]
num = 1
while num <= 20:
    if not(num in lista):
        lista.insert(num-1, num)
    num +=1
print(lista)



# In[11]:


n = 1



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
secunecia_fibo = [0, 1]
for i in range(2, 30):
    numero_fibo = secunecia_fibo[i - 1] + secunecia_fibo[i - 2]
    secunecia_fibo.append(numero_fibo)
print(secunecia_fibo)




# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

sum(secunecia_fibo)


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:


elementos = 15
num = elementos - 5
while num < elementos:
    print(secunecia_fibo[num] / secunecia_fibo[num - 1])
    num += 1

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i, c in enumerate(cadena):
    if c == 'n':
        print(i)



# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:

diccionario = {'Ciudades ': ['Cordoba', 'Villa Carlos Paz', 'CABA','Caballito','Londres'],
               'Paises': ['Argentina', 'Argentina', 'Argentina', 'Argentina', 'Inglaterra'],
               'Continente': ['LATAM','LATAM','Latam','LaTam','Europa']}
for i in diccionario:
    print(i)



# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
print(type(cadena))

cadena = list(cadena)
print(type(cadena))

iterador1 = iter(cadena)
largo = len(cadena)
for i in range(0, largo):
    print(next(iterador1))



# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

lista1 = ['Matias','Santiago','Papa','Mama']
lista2 = ['27','19', '63', '57']
lista_zip = zip(lista1, lista2)
print(list(lista_zip))



# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

lis = [18, 21, 29, 32, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100]
lis2 = [i for i in lis if i % 7 == 0]
print(lis2)



# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
type(lis)

cant = 0 
for elemento in lis:  
    if type(elemento) == list: 
        cant += len(elemento) 
    else:
        cant += 1  

print('La cantidad total de elementos es', cant) 


# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:


for indice, elemento in enumerate(lis):
    if type(elemento) != list:
        lis[indice] = [elemento]
print(lis)
