#RSA
#Para los test, simplemente ejecute main.py para definir las funciones
#En este archivo encontrará las entradas a las funciones definidas
#Para las salidas simplemente ejecute el archivo tests.py

from main import inverso_modular, cifrar_rsa, descifrar_rsa
#Casos de prueba
#Caso 1: p = 61, q = 53, e = 17 y m = 65
print("Caso 1: p = 61, q = 53, e = 17 y m = 65\n")
cifrar_rsa(65, 61, 53, 17)
descifrar_rsa(2790, 3233, 2753)

#Caso 2: p = 11, q = 13, e = 7 y m = 9
print("\nCaso 2: p = 11, q = 13, e = 7 y m = 9\n")
cifrar_rsa(9, 11, 13, 7)
descifrar_rsa(48, 143, 103)

#Caso 3: p = 17, q = 19, e = 5 y m = 10
print("\nCaso 3: p = 17, q = 19, e = 5 y m = 10\n")
cifrar_rsa(10, 17, 19, 5)
descifrar_rsa(193, 323, 173)