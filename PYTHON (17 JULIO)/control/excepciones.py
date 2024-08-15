try:   
    n = int (input("Digite numerador: "))
    d = int (input("Digite denominador: "))
    r = n / d
    print(f"Resultado: {r}" )

except ZeroDivisionError:
    print("ERROR --- División por cero")

except ValueError:
    print("Debe escribir únicamente números")

