divisas = {"euro":"€", "dollar":"$", "yen":"¥"}
while True:
    divisa = input('indica la divisa:\n')
    divisa.lower()
    if divisa in divisas:
        print(divisas[divisa])
        break
    else:
        print('no tengo la divisa')