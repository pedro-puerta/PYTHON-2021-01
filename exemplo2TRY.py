# Exemplo de validação.
# solicitar pro o usuário um numero inteiro positivo.
# se ocorrer erro, pedir novamente.


while True:
    try:
        numero = int(input("Informe um numero inteiro e positivo"))
        if numero <= 0:
            raise TypeError
    except TypeError:
        print("O numero deve ser positivo. Tente novamente")
    except ValueError:
        print("O numero deve ser inteiro. Tente novamente")
    except Exception:
        print("Erro inesperado")
    else:
        break

print("O programa continua.....")
