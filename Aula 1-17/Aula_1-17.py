def aula1_2():
    print("Curso Python")

    num1 = num2 = res = 0

    canal = "CFB Cursos"

    curso = "Curso de Python"

    print(canal + " - " + curso)

    if 10 > 2:
        print("Maior")
        print("aula 2")

    print("FIM")
# aula1_2()


def aula3():
    '''def cn():
        canal="CFB Cursos"

    cn()

    print(canal) #erro'''

    def cn():
        global canal
        canal = "CFB Cursos"

    cn()

    print(canal)
# aula3()


def aula4():

    x = 1  # type(x) => int
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))
    
    x = "CFB Cursos"  # type(x) => string
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))
    
    x = 15.6  # type(x) => float
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))
    
    x = True  # type(x) => bool
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))

    x = complex(1j)
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))

    x = ["Carro", "Aviao", "Navio", 1, 58.3, True]  # type(x) => List / Array
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))

    x = ("Carro", "Aviao", "Navio", 1, 58.3, True)  # type(x) => Tupla
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))

    x = range(0, 100, 1)  # type(x) => List, range(inicio,fim,contador/passos)
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))

    x = {  # Dict => Dicionario
        "canal": "CFB Cursos",
        "curso": "Curso de Python",
        "nome": "Bruno"
    }
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))

    x = {5, 7, 4, 5, 7, 4, 8}  # set => Não repetir elementos
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))

    x = frozenset({5, 7, 4, 5, 7, 4, 8})  # frozenset => Tornar imutavel
    print("Tipo: "+str(type(x)))
    print("Valor: "+str(x))

def aula5():
    import random

    num_i=10
    num_f=5.2
    num_c=1j
    num_r=[]

    for i in range(6):
        num_r.append(random.randrange(0,59))

    for i in range(len(num_r)):
        print("Valor {}: {}".format(i,num_r[i]))
