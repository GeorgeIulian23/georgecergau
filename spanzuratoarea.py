import random

lista_cuv = ['abercedar','lambriu', 'algoritm','termopan']




def get_cuvinte_in_lista():
    file = open(file='word.txt')
    lines = list(file.readlines())
    poc = []
    ana = ''
    for line in lines:
        ana = str(line).replace("\n", '')
        poc.append(ana)

    return poc


def tabela_joc(cond):
    if cond == 6:
        print(" ---------- \n |     6  | \n | \n | \n | \n | \n | _____________ ")
    elif cond == 5:
        print(" ---------- \n |   5    | \n |        O  \n | \n | \n | \n | _____________ ")
    elif cond == 4:
        print(" ---------- \n |   4    | \n |        O  \n |       /  \n | \n | \n | _____________ ")
    elif cond == 3:
        print(" ---------- \n |   3    | \n |        O  \n |       / \   \n | \n | \n | _____________ ")
    elif cond == 2:
        print(" ---------- \n |   2    | \n |        O  \n |       / \   \n |        | \n | \n | _____________ ")
    elif cond == 1:
        print(" ---------- \n |   1    | \n |        O  \n |       / \   \n |        | \n |       / \n | _____________ ")
    elif cond == 0:
        print(" ---------- \n |        | Sfarsit de joc  \n |        O  \n |       / \   \n |        | \n |       / \ \n | _____________ ")
    elif cond == 7:
        print(" ---------- \n \n | \n | \n | \n | \n | _____________ ")



def Joc_nou():
    global cuvant_spatiat
    global cuvantul_ascuns
    global numar_de_incercari
    global cuvant
    numar_de_incercari = 0
    cuvant = random.choice(get_cuvinte_in_lista())
    cuvant=cuvant.lower()
    cuvant_spatiat = " ".join(cuvant)
    #print(cuvant_spatiat)
    cuvantul_ascuns = (" ".join("_" * len(cuvant)))
    # print(cuvantul_ascuns)


def Ghicim_litera():
    contor = 7
    lista_litere_incercate = []
    n = 0
    while contor != 0:
        global numar_de_incercari
        cuvant_de_incercat = list(cuvant_spatiat)
        if contor == 7 and n ==0:
            guess = list(cuvantul_ascuns)
        guess[0] = cuvant_de_incercat[0]
        guess[-1] = cuvant_de_incercat[-1]
        contor_auxilar = guess[0]
        contor_auxilar2 = guess[-1]
        val_int = n
        tabela_joc(contor)
        aux1 = 0  # retin intr-o var sa vad indexul unde mai am acea litera
        aux2 = 0

        if n == 0:
            for i in range(1,len(guess)):
                if contor_auxilar == cuvant_de_incercat[i] :
                    aux1=i
            for i in range(1, len(guess)):
                if contor_auxilar2 == cuvant_de_incercat[i] :
                    aux2=i
                    break

        if aux1!=0:
            guess[aux1] = contor_auxilar
        if aux2!=0:
            guess[aux2] = contor_auxilar2

        str2 = ""
        for string in guess:
          str2 += string
        if n==0:
            print(str2)

        litera = input("Introdu o litera")
        lista_litere_incercate.extend(litera)
        #print(lista_litere_incercate)
        count =0
        for lit in lista_litere_incercate:
            if lit == litera:
                count +=1
                if count == 2:
                   print ("Ai mai incercat litera asta")



        for i in range(len(cuvant_de_incercat)):
            if cuvant_de_incercat[i] == litera:
                guess[i] = litera
                n += 1
                #print(n)
        if n <= val_int:
            contor = contor - 1
            #print(contor)
        str1 = ""
        for string in guess:
            str1 += string
        # print(str1)
        # print(contor)
        guess = list(str1)

        contoriz = 0
        print(str(str1))
        #contor = contor -1
        for i in range(len(guess)):
            if guess[i] == cuvant_de_incercat[i]:
                contoriz += 1


        if contoriz == len(guess):
            print("Ai invins! Cuvantul a fost {}".format(str1.replace(' ','')))

            return 0

    else:
        tabela_joc(0)
        print("Ai pierdut ! Cuvantul era {}".format(str(cuvant).replace(',','')))
        return 0



Joc_nou()
Ghicim_litera()
