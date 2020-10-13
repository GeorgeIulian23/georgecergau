def check_number():
    number = input("Introdu un numar de telefon ")  # un numar de telefon are 10 cifre

    if number.isdigit() == False or len(number) < 10 or number[0] != "0" or number[1] != "7":
        return 0
    else:
        print(number)


check_number()
