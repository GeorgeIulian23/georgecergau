import random

global scor_omulet
global scor_pisi
scor_pisi = scor_omulet = 0

def tabla_de_joc():
    str1 = "__1____2____3__"
    str2 = "__4____5____6__"
    str3 = "__7____8____9__"
    print(str1+'\n'+str2 +'\n '+str3)


def alegere_litera() :
    global alegere_omulet
    global alegere_pisi
    criteriu_alegere_1 = random.choice(range(0,100))
    criteriu_alegere_2 = random.choice(range(0,100))
    lista_alegeri=['x', 0]
    if criteriu_alegere_1 > criteriu_alegere_2:
        alegere_omulet = str(input("Alege x sau 0"))
        print("Incepe persoana cu {} ".format(alegere_omulet))
        for ales in lista_alegeri:
            if alegere_omulet.lower() in lista_alegeri or alegere_omulet == ales:
                lista_alegeri.remove(ales)
                if ales == 'x':
                    aux = 0
                else:
                    aux = 1
                alegere_pisi = str(lista_alegeri[aux - 1])
            else:
                alegere_omulet = str(input("Alege x sau 0 omuletule!"))
                return
    else:
        alegere_pisi = 'x'
        print("Incepe Pisi cu {}".format(alegere_pisi))
        aux =''
        for ales in lista_alegeri:
            if alegere_pisi == ales:
                aux = ales
                if aux == 'x':
                    alegere_omulet = 0
                else:
                    alegere_omulet = 'x'
    print('Se va juca astfel: \n Omuletul cu {} \n Pisi cu {} ! \n \t Bafta!! '.format(alegere_omulet, alegere_pisi))

    return  alegere_omulet, alegere_pisi



def inceput_de_joc() -> int:
    global diferentiere
    diferentire = 0
    criteriu_alegere_1 = random.choice(range(0,100))
    criteriu_alegere_2 = random.choice(range(0,100))
    if criteriu_alegere_1 > criteriu_alegere_2:
        print("Omuletul alege primul pozitia")
        diferentiere = 1
    else:
        print("Pisi alege pozitia ")
        diferentiere = 2
    return diferentire


def liste_pozitii_alese():
    global lista_omulet
    global lista_pisi
    lista_omulet=[]
    lista_pisi=[]
    return lista_omulet,lista_pisi




def alegem_pozitia():
    print("\t \t \t\b Bun venit in jocul nostru  de X si o \n    Va trebui sa alegi o pozitie din cele de mai jos ")
    tabla_de_joc()
    alegere_litera()
    inceput_de_joc()
    dict_initial = {1: '.', 2: '.', 3: '.', 4: '.', 5: '.', 6: '.', 7: '.', 8: '.', 9: '.'}
    lista_initiala=[]
    str1 = "__1____2____3____4____5____6____7____8____9__"
    for key in dict_initial.keys():
        lista_initiala.append(key)

    liste_pozitii_alese()
    var_aux = 0
    if var_aux == 0:
        if diferentiere == 1:
            print("Alege o pozitie omuletule" )
            poz = int(input(''))
            if poz < 1 or poz > 9:
                print('Alege o alta pozitie omuletule')
                poz = input('')

            lista_omulet.append(poz)
            for valoare in lista_initiala:
                if valoare == poz:
                    lista_initiala.remove(valoare)
            #print(lista_initiala)
            poz_pisi=random.choice(lista_initiala)
            lista_pisi.append(poz_pisi)
            for valoare in lista_initiala:
                if valoare == poz_pisi:
                    lista_initiala.remove(valoare)
            #print(poz_pisi)
        if diferentiere == 2:

            poz_pisi = random.choice(range(1,10))
            print("Alege o pozitie pisi")
            lista_pisi.append(poz_pisi)
            print("E randul tau omuletule, alege o pozitie diferita fata de cea a lui pisi. Pisi a ales {}".format(poz_pisi))
            for valoare in lista_initiala:
                if valoare == poz_pisi:
                    lista_initiala.remove(valoare)
            poz = int(input(''))
            while poz not in lista_initiala:
                print('Alege o alta pozitie omuletule')
                poz = int(input(''))

            for valoare in lista_initiala:
                if valoare == poz:
                    lista_initiala.remove(poz)
            lista_omulet.append(poz)
    global lista_string_tabla
    lista_string_tabla = list(str1)
    # if alegere_pisi == '0':
    for i, val in enumerate(lista_string_tabla):
        if str(poz_pisi) == val:
            lista_string_tabla[i] = alegere_pisi
    # else:
    #     for i, val in enumerate(lista_string_tabla):
    #         if str(poz_pisi) == val:
    #             lista_string_tabla[i] = alegere_pisi

    # if alegere_omulet == '0':
    for i, val in enumerate(lista_string_tabla):
        if str(poz) == val:
            lista_string_tabla[i] = alegere_omulet
    # else:
    #     for i, val in enumerate(lista_string_tabla):
    #         if str(poz) == val:
    #             lista_string_tabla[i] = alegere_omulet


    modificare_tabela()
    n = 4
    conditie = True
    while n > 0:
        if diferentiere == 1 and conditie is True:
            print('Este randul tau omuletule, Introdu {} in pozitiile libere'.format(alegere_omulet))
            poz = int(input("Alege pozitia cu atentie: "))
            while poz not in lista_initiala:
                print(" Alege din pozitiile libere {}".format(str(lista_initiala)))
                poz = int(input("Alege pozitia cu atentie din nou: "))
            lista_omulet.append(poz)
            modificare_tabela()
            for valoare in lista_initiala:
                if valoare == poz:
                    lista_initiala.remove(poz)
            poz_pisi = random.choice(lista_initiala)
            lista_pisi.append(poz_pisi)
            for valoare in lista_initiala:
                if valoare == poz_pisi:
                    lista_initiala.remove(poz_pisi)
            # if alegere_pisi == '0':
            for i, val in enumerate(lista_string_tabla):
                if str(poz_pisi) == val:
                    lista_string_tabla[i] = alegere_pisi
            # else:
            #     for i, val in enumerate(lista_string_tabla):
            #         if str(poz_pisi) == val:
            #             lista_string_tabla[i] = alegere_pisi

            # if alegere_omulet == '0':
            for i, val in enumerate(lista_string_tabla):
                if str(poz) == val:
                    lista_string_tabla[i] = alegere_omulet
            # else:
            #     for i, val in enumerate(lista_string_tabla):
            #         if str(poz) == val:
            #             lista_string_tabla[i] = alegere_omulet
            modificare_tabela()
        else:
            print('Este randul tau Pisi, Introdu {} in pozitiile libere'.format(alegere_pisi))
            poz_pisi = random.choice(lista_initiala)
            lista_pisi.append(poz_pisi)

            for valoare in lista_initiala:
                if valoare == poz_pisi:
                    lista_initiala.remove(poz_pisi)
            modificare_tabela()
            poz = int(input("Pozitia trebuie sa fie aleasa din nou de jucator cu atentie. Pisi a ales {} \n Alege o pozitie diferita: ".format(poz_pisi)))
            while poz not in lista_initiala:
                print(" Alege din pozitiile libere {}".format(str(lista_initiala)))
                poz = int(input("Alege pozitia cu atentie: "))
            modificare_tabela()
            lista_omulet.append(poz)
            for valoare in lista_initiala:
                if valoare == poz:
                    lista_initiala.remove(poz)
            # if alegere_pisi == '0':
            for i, val in enumerate(lista_string_tabla):
                if str(poz_pisi) == val:
                    lista_string_tabla[i] = alegere_pisi
            # else:
            #     for i, val in enumerate(lista_string_tabla):
            #         if str(poz_pisi) == val:
            #             lista_string_tabla[i] = alegere_pisi

            # if alegere_omulet == '0':
            for i, val in enumerate(lista_string_tabla):
                if str(poz) == val:
                    lista_string_tabla[i] = alegere_omulet
            # else:
            #     for i, val in enumerate(lista_string_tabla):
            #         if str(poz) == val:
            #             lista_string_tabla[i] = alegere_omulet

        n -= 1
        booll = True
        modificare_tabela()

        if choice_check_omulet(conditie) is True:
                conditie = True
        else:
            booll = False
            print("Felicitari ai castigat omuletule! ")
            scor_omulet += 1

        if choice_check_pisi(conditie) == True:
                conditie = True

        else:
            booll = False
            print("Felicitari ai castigat pisi! ")
            scor_pisi += 1
        if booll is False:
            print( "Scorul partidelor este... Pisi {} Omulet {}".format(scor_pisi, scor_omulet))
            print("Joc terminat. Vrei sa mai joci o data? Daca da, apasa 1, daca nu, apasa orice alta tasta")
            break

        if n == 1:
            print("Egalitate! Nimeni nu a castigat! Mai jucati? Daca da, apasa 1, daca nu orice altceva")
            break
        #print(lista_initiala)
    check = input('')
    if check == '1':
        alegem_pozitia()


def modificare_tabela():

    print("\n \n \n ")
    string1 = ''
    string2 = ''
    string3 = ''
    for i, val in enumerate(lista_string_tabla):
        if i < 15:
            string1 = string1 + str(val)
        elif i < 30:
            string2 = string2 + str(val)
        elif i < len(lista_string_tabla):
            string3 = string3 + str(val)

    print(string1)
    print(string2)
    print(string3)


def choice_check_omulet(cond):
    if all(x in lista_omulet for x in [1, 2, 3]) == cond:

        return 0
    elif all(x in lista_omulet for x in [1, 4, 7]) == cond:
        return 0
    elif all(x in lista_omulet for x in [2, 5, 8]) == cond:
        return 0
    elif all(x in lista_omulet for x in [3, 6, 9]) == cond:
        return 0
    elif all(x in lista_omulet for x in [4, 5, 6]) == cond:

        return 0
    elif all(x in lista_omulet for x in [7, 8, 9]) == cond:

        return 0
    elif all(x in lista_omulet for x in [1, 5, 9]) == cond:

        return 0
    elif all(x in lista_omulet for x in [3, 5, 7]) == cond:

        return 0

    return cond

def choice_check_pisi(cond) :
    if all(x in lista_pisi for x in [1, 2, 3]) == cond:

        return 0
    elif all(x in lista_pisi for x in [1, 4, 7]) == cond:
        return 0
    elif all(x in lista_pisi for x in [2, 5, 8]) == cond:
        return 0
    elif all(x in lista_pisi for x in [3, 6, 9]) == cond:
        return 0
    elif all(x in lista_pisi for x in [4, 5, 6]) == cond:

        return 0
    elif all(x in lista_pisi for x in [7, 8, 9]) == cond:

        return 0
    elif all(x in lista_pisi for x in [1, 5, 9]) == cond:

        return 0
    elif all(x in lista_pisi for x in [3, 5, 7]) == cond:

        return 0
    return cond

alegem_pozitia()

