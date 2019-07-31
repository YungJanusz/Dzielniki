number = int(input("Wprowadz liczbe: "))
while number <= 2:
    number = int(input("Podaj liczbe większą niz 2!"))
lista = range(2, number+1)
lista2=[]
for i in lista:
    if number % i == 0:
        lista2.append(i)
print("Lista dzielników liczby " + str(number) + ":")
print(lista2)
