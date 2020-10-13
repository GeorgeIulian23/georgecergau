def read_char():
    b=0
    a=input("Scrie un cuvant: ")

    for caracater in a:
        if caracater !=' ':
            return 0
        else:
            b+=1
    print(b)

read_char()
