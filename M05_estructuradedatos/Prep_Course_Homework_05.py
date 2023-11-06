#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

lista = ['Madrid','Cordoba','Lisboa','Londres','Acapulco']
print(lista)
type(lista)


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

lista = ['Madrid','Cordoba','Lisboa','Londres','Acapulco']
segundo_elemento = lista[1]
print(segundo_elemento)


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:
lista = ['Madrid','Cordoba','Lisboa','Londres','Acapulco']
filtrado = lista[1:5]
print(filtrado)




# 4) Visualizar el tipo de dato de la lista

# In[12]:
lista = ['Madrid','Cordoba','Lisboa','Londres','Acapulco']
type(lista)




# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

lista = ['Madrid','Cordoba','Lisboa','Londres','Acapulco']
filtrado2 = lista[2:]
print(filtrado2)



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

lista = ['Madrid','Cordoba','Lisboa','Londres','Acapulco']
filtrado3 = lista[0:4]
print(filtrado3)

    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

lista = ['Madrid','Cordoba','Lisboa','Londres','Acapulco']
lista.append('Chicago')
print(lista)







# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

lista = ['Madrid','Cordoba','Lisboa','Londres','Acapulco']
lista.insert(3, 'Tokio')
print(lista)



# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:

lista = ['Madrid','Cordoba','Lisboa','Londres','Acapulco']
continenetes = ['Europa','Latino America','Europa','Europa','Latino America']

lista.extend(continenetes)
print(lista)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:
lista =['Madrid', 'Cordoba', 'Lisboa', 'Londres', 'Acapulco', 'Chicago']
lista.index('Chicago')




# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

# Si buscas un elemento que no existe arrojaria error: 

lista = ['Madrid', 'Cordoba', 'Lisboa', 'Londres', 'Acapulco', 'Chicago']
lista.index('Villa Carlos Paz')



# 12) Eliminar un elemento de la lista

# In[25]:


lista = ['Madrid', 'Cordoba', 'Lisboa', 'Londres', 'Acapulco', 'Chicago']
lista.pop(0)


# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

# No permite eliminarlo y da error.

lista = ['Madrid', 'Cordoba', 'Lisboa', 'Londres', 'Acapulco', 'Chicago']
lista.pop(8)



# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

lista = ['Madrid', 'Cordoba', 'Lisboa', 'Londres', 'Acapulco', 'Chicago']
lista_sin_chicago = lista.pop(5)
print(lista_sin_chicago)
print(lista)



# 15) Mostrar la lista multiplicada por 4

# In[29]:

lista = ['Madrid', 'Cordoba', 'Lisboa', 'Londres', 'Acapulco', 'Chicago']
print(lista * 4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:
tupla1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,)
type(tupla1)



# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

tupla1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,)
print(tupla1[10:15])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

20 in tupla1
30 in tupla1


# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

lista = ['Madrid', 'Cordoba', 'Lisboa', 'Londres', 'Acapulco', 'Chicago']


var_ciudad_faltante = 'París'

if(not var_ciudad_faltante in lista):
    lista.append(var_ciudad_faltante)
    print(lista)
else:
    print('Ya estaba la ciudad en la lista')



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:


print(lista.count('Cordoba'))
print(tupla1.count(15))


# 21) Convertir la tupla en una lista

# In[52]:

list(tupla1)



# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:


tupla1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,)
elemento0 = tupla1[0]
elemento1 = tupla1[1]
elemento2 = tupla1[2]
print(elemento0)
print(elemento1)
print(elemento2)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:


lista_ciudades = ['Madrid','Cordoba','Lisboa','Londres','Acapulco']
Paises = ['España', 'Argentina','Portugal', 'Inglaterra','Mexico']

diccionario = {'Ciudades': lista_ciudades, 'Paises': Paises}



# 24) Imprimir las claves del diccionario

# In[59]:
claves_lista = list(diccionario.keys())
print(claves_lista)



# 25) Imprimir las ciudades a través de su clave

# In[61]:

diccionario = {'Ciudades': ['Madrid','Cordoba','Lisboa','Londres','Acapulco'],
               'Paises': ['España', 'Argentina','Portugal', 'Inglaterra','Mexico']}
ciudades = diccionario['Ciudades']
print(ciudades)


