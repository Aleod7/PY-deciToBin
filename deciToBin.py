def deciToBin(n):
    if(n > 1):
        deciToBin(n//2)
    print(n%2, end='')
deci = int(input("Veuillez entrer une valeure de base 10: "))
print(str(deciToBin(deci)).replace("None", ""))
