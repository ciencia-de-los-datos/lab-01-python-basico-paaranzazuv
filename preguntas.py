"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv 

# def leer(input):
#     x=[ ]
#     with open("data.csv","r") as csv_file:
#         csv_reader = csv.reader(
#             csv_file,
#             delimiter="\t",
#             quotechar='',
#         )
#         for row in csv_reader:
#             x.append(row)
#     return x
         
# print(leer("data.csv"))
    #
    # El for debe estar dentro del ambito
    # del bloque with
    #

    # x= f.readlines()
    # print(x)
    # # x= open("data.csv","r").readlines() malas practicas
    # x = [z.replace("\t", ",") for z in x]
    # x = [z.replace("\n", "") for z in x]
    # x= [z.split(",") for z in x]
    # print(x)



 
def pregunta_01():
    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)
    y = [int(z[1]) for z in x[0:]]
    return sum(y)  



# """
#     Retorne la suma de la segunda columna.

#     Rta/
#     214

# """

def pregunta_02():
    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)
    l2 = []
    y = [z[0] for z in x[0:]]
    n=set(y)
    for i in n:
        z = y.count(i)
        q = (i, z)
        l2.append(q)
    t = sorted(l2)
    return t


# 
#     Retorne la cantidad de registros por cada letra de la primera columna como la lista
#     de tuplas (letra, cantidad), ordendas alfabéticamente.

#     Rta/
#     [
#         ("A", 8),
#         ("B", 7),
#         ("C", 5),
#         ("D", 6),
#         ("E", 14),
#     ]

#     """



# #print(l3)
 

def pregunta_03():
    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)

    l3 = []
    new_l3= []
    diccionario = {}

    r = [z[0:2] for z in x [0:]]

    for i,j in r:
        z = int (j)
        l3.append ((i,z))
    
    for key, value in l3:


        if key not in diccionario.keys():
            diccionario [key] = 0
        diccionario [key] += value

    for key, value in diccionario.items():
            tupla = (key, value)
            new_l3.append (tupla)
    
    result_p3 = sorted(new_l3)
    
    return result_p3




"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

def pregunta_04():

    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            
        )
        for row in csv_reader:
            x.append(row)

    l4=[]
    y = [z[2].split("-")[1] for z in x[0:]]
    h = set(y)
    for i in h:
            z = y.count(i)
            q = (i, z)
            l4.append(q)
            t = sorted(l4)
    return t


"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

def pregunta_05():
     x=[ ]
     with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)
     l5 = []
     l51 = []  
     diccionariomin = {}

     r = [z[0:2] for z in x [0:]]
     for i, j in r:
        z = int (j)
        l5.append ((i,z))

     for key, value in l5:
       
        if key not in diccionariomin.keys(): ###### por que no corre  con or  diccionariomax.keys
            diccionariomin [key] = []
           
        diccionariomin [key].append(value)
    
     for i in diccionariomin.keys():
                 tupla = (i,max(diccionariomin[i]), min(diccionariomin[i]))
                 l51.append (tupla)
     result_p5 = sorted(l51)
     return result_p5



"""
Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
letra de la columa 1.

Rta/
[
("A", 9, 2),
("B", 9, 1),
("C", 9, 0),
("D", 8, 3),
("E", 9, 1),
]

"""
# revisar como guardar en diccionerio una lista
def pregunta_06():
    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)
    l6=[]
    r = [z[4].split(",") for z in x [0:]] 
    for i in r:
        z=len(i)
        for j in range(z):
            t=i[j]
            l6.append((t[:3],int(t[4:])))
    diccionario = {}
    
    for key, value in l6:
        if key not in diccionario.keys(): ###### por que no corre  con or  diccionariomax.keys
            diccionario [key] = []
        diccionario[key].append(value)
           
    l61=[]
    for i in diccionario.keys():
                    tupla = (i, min(diccionario[i]), max(diccionario[i]))
                    result_p6=l61.append (tupla)
    
    
    result_p6 = sorted(l61)
    return result_p6



"""
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """



def pregunta_07():
    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)
    diccionario={}
    l7=[]

    r = [z[0:2] for z in x [0:]]
    
    for value, key in r:
            if key not in diccionario.keys(): ###### por que no corre  con or  diccionariomax.keys
                diccionario [key] = []
            diccionario [key].append(value)

    
    for key, value in diccionario.items():
                tupla = (int(key), (value))
                l7.append (tupla)
    
    result_p7 = sorted(l7)
    
    return result_p7

print(pregunta_07())
"""
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
  ]

    """


def pregunta_08():
    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)

    diccionario={}
    l8=[]
    
    r = [z[0:2] for z in x [0:]]
    
    for value, key in r:
            if key not in diccionario.keys(): 
                diccionario [key] = []
            diccionario [key].append(value)

    
    for key, value in diccionario.items():
                tupla = (int(key), sorted(list(set(value))))
                l8.append (tupla)
    
    result_p8 = sorted(l8)
    
    return result_p8
print(pregunta_08())


"""
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """


def pregunta_09():
    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)

    l9=[]
    r = [z[4].split(",") for z in x [0:]] 
    for i in r:
        z=len(i)
        for j in range(z):
                t=i[j]
                l9.append((t[:3]))
    l91=sorted(l9)
    
    diccionario = {}
        
    for key in l91:
            if key not in diccionario.keys(): ###### por que no corre  con or  diccionariomax.keys
                         diccionario [key] = 0
            diccionario[key] += 1

    return diccionario
    
    


"""
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

   

"""     
       

def pregunta_10():
    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)
    
    l10 = []
    r = [[z [0]] + [z[3].split(",")]+[z[4].split(",")] for z in x [0:]]

    for i in range(len(r)):
         f=r[i][0]
         p=len(r[i][1])
         z=len(r[i][2])
         l10.append((f,p,z))

    return l10    

"""
Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
"""


def pregunta_11():
    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)

    diccionario11 = {}
    l11 = []
    r = [[z [3].split(",")] + [int(z[1])] for z in x [0:]]
    f = (len(r))

    for i in range (f):
            o = len(r[i][0])
            t = r[i][1]
        
            for j in range (o):
                z = r[i][0][j]
                l11.append((z,t))

    for key, value in sorted(l11):
            if key not in diccionario11.keys(): 
                            diccionario11 [key] = 0
            diccionario11[key] += value

    return  diccionario11



"""
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


"""
 
def pregunta_12():
    x=[ ]
    with open("data.csv","r") as csv_file:
        csv_reader = csv.reader(
            csv_file,
            delimiter="\t",
            quotechar='"',
        )
        for row in csv_reader:
            x.append(row)
    l12 = []
    diccionario12 = {}

    r = [[z[0]]+[z[4].split(",")] for z in x [0:]]

    for i in r:
            z=len(i[1])
            for j in range(z):
                    t=i[1][j]

                    l12.append((i[0],(int(t[4:]))))
    l121 = sorted(l12)

    for key , value in l121:
            if key not in diccionario12.keys():
                diccionario12[key]=0
            diccionario12[key] += value
    return diccionario12




              

"""
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
