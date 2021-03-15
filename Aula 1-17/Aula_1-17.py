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

    num_i = 10
    num_f = 5.2
    num_c = 1j
    num_r = []

    for i in range(6):
        num_r.append(random.randrange(0, 59))

    for i in range(len(num_r)):
        print("Valor {}: {}".format(i, num_r[i]))


def aula6():
    curso = "Curso de Python"
    # print(curso[9:15])
    # print(curso.strip()) => remover espaco ini e fim
    # print(curso.lower().strip()) => remover espaco ini e fim, minusculo
    # print(curso.upper()) => maiusculo
    # print(curso.replace("Python","C#")) => troca oque esta nas aspas
    a = curso.split(" ")  # remover espaco ou oque tiver entre aspas
    print(a[2])
    print("Tamanho: " + str(len(curso)))


def aula7():
    texto = "Curso Python"
    palavra = "python"
    cidade = "Belo Horizonte"
    dia = 15
    mes = "Dezembro"
    ano = 2019
    canal = "CFB Cursos"
    data = "{}, {} de {} de {}\n \"{}\""

    # itens especiais para formatação
    # \' => (aspas simples em string)
    # \" => (aspas duplas)
    # \n => (pular linha)
    # \r => (Enter)
    # \t => (Tab)
    # \b => (tecla apagar)

    res1 = palavra in texto  # comparacao de string
    print(res1)  # false

    res2 = palavra.upper() in texto.upper()  # comparacao de string em maiusculo
    print(res2)  # true

    print(data.format(cidade, dia, mes, ano, canal))


def aula8():
    aula = 0
    print(bool(aula))

    aula = 1
    print(bool(aula))


def aula9():

    carros = ["HRV", "Golf", "Argo", "Focus"]  # List
    carros1 = ["Fit", "Fusion", "Polo"]

    carros.append("Uno")  # Adcinar um item
    carros.extend(carros1)  # cada item do carros1

    carros2 = ["Fusca", "147", "Brasilia", "Celta"]

    carros3 = carros+carros2  # coloca ambos inclusive repetidos

    print(str(len(carros3)) + " carros na lista")

    print(carros3)


def aula10():
    a = 10
    b = 5
    res = 0
    op = "/"

    if op == "+":
        res = a+b

    if op == "-":
        res = a-b

    if op == "*":
        res = a*b

    if op == "/":
        res = a/b

    print(str(a) + op + str(b) + " = " + str(res))


def aula11():
    clima = "sol"
    dinheiro = 650
    lugar = ""

    if clima == "sol" or (dinheiro >= 300 and dinheiro <= 500):
        lugar = "clube"
    else:
        lugar = "cinema"

    print("Vou ao " + lugar)

    #   AND
    #   V   V   =   V
    #   V   F   =   F
    #   F   V   =   F
    #   F   F   =   F

    #   OR
    #   V   V   =   V
    #   V   F   =   V
    #   F   V   =   V
    #   F   F   =   F
