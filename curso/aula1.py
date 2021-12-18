print("###################")
print("ADIVINHE O NUMERO")
print("###################")

num = '10'

while True:
    usuario = input('Digite seu numero: ')

    if(num == usuario):
        print('Voce acertou!!')
        break
    else:
        print('Errou!')