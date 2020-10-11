def read_char():
    b=0
    a=input("Scrie un cuvant: ")

    for caracater in a:
        if caracater !=" ":
            b=b+1;

    print(b)

read_char()
