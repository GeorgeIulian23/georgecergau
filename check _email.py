def check_email():
    e_mail=input("Introdu o adresa de e-mail")
    a=0
    b=0
    for conditie in e_mail:
        if conditie=="@":
            a=a+1
        if conditie ==".":
            b=b+1
            if b==1 and a==0:
                print("Adresa INVALIDA")
                return 0
    if (a>=2 or b>=2):
        print("Adresa de e-mail invalida")
    else:
        if (a<1 or b<1):
            print("Adresa de e-mail invalida")
        else:
            print(e_mail)

check_email()