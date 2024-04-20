#1 Escribe un programa en Python para multiplicar todos los elementos de un diccionario.
a={
    "a":10,
    "b":2,
    "c":4,
    "d":8
}
aa=1
for i in a.values():
    aa*=i
print(f'el producto de los elemneto del diccionario es : {aa}')



#2 Escribe un programa en Python para eliminar una clave de un diccionario.
b=a.pop("b")
print(a)

#3 Escribe un programa en Python para convertir dos listas en un diccionario.
l1=["h","g","j","i"]
l2=[5,3,2,7]
dic=dict(zip(l1,l2))
print(dic)

#4 Escribe un programa en Python para ordenar un diccionario dado por clave.
c={
    "material":"carton",
    "ancho":10,
    "largo":20,
    "alto":15
}
dic_alp={}
keys = c.keys()
sorted_keys = sorted(keys)
for key in sorted_keys:
  dic_alp[key] = c[key]
print(dic_alp)
#5 Escribe un programa en Python para obtener los valores máximo y mínimo de un diccionario.
aaa=max(a.values())
ccc=min(a.values())
print(f"el maximo valor en el diccionario es :{aaa}")
print(f"el minimo valor en el diccionario es {ccc}")

#6 Escribe un programa en Python para obtener un diccionario a partir de los campos de un objeto.
w = ["azul","morado","rojo","amarillo","cafe"]
w1 = {}
for i in range(len(w)):
    w1[str(i)]=w[i]
print(w1)

#7 Escribe un programa en Python para eliminar duplicados del diccionario.
cantidad_de_dulces = { 'maria' : 10, 'javier' : 15, 'lucia' : 20, 'camila' : 10, 'antonio' : 20}
f = []
sin_repetir = dict()
for key, val in cantidad_de_dulces.items():
    if val not in f:
        f.append(val)
        sin_repetir[key] = val
  
print(f'el diccionario sin valos repetidos es {sin_repetir}')

#8 Escribe un programa en Python para verificar si un diccionario está vacío o no.
if len(cantidad_de_dulces)>0:
    print("No esta vacio")
else:
    print("esta vacia")
#9 Escribe un programa en Python para extraer una lista de valores de una lista dada de diccionarios.
l4=[{'Matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}]
l5=[]
for i in l4:
    for j in i.values():
        l5.append(j)
print(l5)
#10 Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Ciencias[92, 94, 88]
[{'matematicas': 90, 'ciencia': 92}, {'Matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}]
ciencias=l5[1::2]
print(ciencias)
#11 Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Matemáticas
#[90, 89, 92]
matematicas=l5[::2]
print(matematicas)

#12 Escribe un programa en Python para encontrar la longitud de un diccionario de valores.
print(f'la longitud de {c} es: {len(c)}')
#13 Escribe un programa en Python para obtener la profundidad de un diccionario.

#14 Escribe un programa en Python para acceder al elemento de la clave de un diccionario por índice.
Materias={1:'fisica',
          2:'matematica',
          3:'arquitectura',
          4:'bioquimica',
          5:'quimica'}
I=[0,1,4]
s=0
for i in Materias:
    if s in I:
        print(Materias[i])
    s+=1

#15 Escribe un programa en Python para convertir un diccionario en una lista de listas.
R={1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'}
l6=[]
for i in R.items():
    l7=list(i)
    l6.append(l7)
print(l6)

#16 Escribe un programa en Python para filtrar números pares de un diccionario de valores.
d1={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
d2={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
def filtpar(a):
    b = []
    c = []
    for i in a:
        b = a[i]
        c = [i for i in b if i%2==0]
        a[i]=c

filtpar(d1)
filtpar(d2)
print(f'el diccionario obtenido para el primer diccionario filtrado es {d1}')
print(f'el diccionario obtenido para el segundo dicionario filtrado es:{d2}')
