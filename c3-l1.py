def function_check():
    program = input("Scrieti numerele ")
    result = program.split(" ")
    print(result)
    contor = len(result)
    print(contor)
    aux=-1
    count, count1 = 0, 0
    while int(result[aux]) != 0 :
        aux += 1
        if aux >= contor :
            break
        elif int(result[aux])% 2 == 0:
            count += 1
        elif int(result[aux]) % 2 == 1:
            count1 += 1
        print(aux)


    print("Numarul de numere pare este .{} si numarul de numere impare .{} ".format(count, count1))

function_check()