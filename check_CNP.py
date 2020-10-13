def range1(start,end):
    return range(start,end+1)

def validator_CNP():
    CNP=input("Sa verificam CNP ul: ")
    if CNP.isdigit()==False or len(CNP)>13 or len(CNP)<13 or int(CNP[0])<1 or int(CNP[0])>9 or int(CNP[1])<0:
        return 0
    elif int(CNP[3]) not in range1(0,1):
        return 0
    elif int(CNP[3])==1 and int (CNP[4]) not in range1(0,2):
        return 0
    elif int (CNP[5]) not in range1(0,2):
        return 0
    elif (int(CNP[7]) == 4 and int(CNP[8])>6) or (int(CNP[7]) == 5 and int(CNP[8]) not in range1(1,2)):
        return 0
    else:
        validare="279146358279"
        check_number=CNP[:-1]
        count=0
        numar=0
        for valid in validare:
            numar=int(valid)*int(check_number[count])+numar
            count+=1
        #print(numar)
        if int(CNP[12])==numar%11 or numar%11==10:
            print("CNP ul este valid")
        else:
            print("cifra de control gresita!")


validator_CNP()