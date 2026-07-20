#Pruebas para el cifrado de cesar
#Simplemente ejecute el archivo tests.py para ver los resultados de las pruebas
#En el archivo encontrará los valores de entrada

#Para las pruebas, primero importamos las funciones que ya definimos en main.py
from main import cifrar_mensaje, descifrar_mensaje, descifrar_mensajes_posibles

#Prueba 1 para las funciones (Mensaje Hola Unal):
print("Prueba 1 para las funciones (Mensaje Hola Unal):")
print("cifrar la frase Hola Unal con" \
" una llave de 3:\n", cifrar_mensaje("Hola Unal", 3))


print("Krod Xqdo (mensaje anterior) descifrado con la misma llave de 3:",
       descifrar_mensaje("Krod Xqdo", 3))


print("Mensajes posibles para 'Krod Xqdo':")
descifrar_mensajes_posibles("Krod Xqdo")

#Prueba 2 para las funciones (Mensaje Viva Colombia):
print("\nPrueba 2 para las funciones (Mensaje Viva Colombia):")
print("cifrar la frase Viva Colombia con" \
" una llave de 5:\n", cifrar_mensaje("Viva Colombia", 5))

print("Anaf Htqtrgnf (mensaje anterior) descifrado con la misma llave de 5:\n",
       descifrar_mensaje("Anaf Htqtrgnf", 5))

print("Mensajes posibles para 'Anaf Htqtrgnf':")
descifrar_mensajes_posibles("Anaf Htqtrgnf")

#Prueba 3 para las funciones (Mensaje Mateo, no descongelaste el pollo):
print("\nPrueba 3 para las funciones (Mensaje Mateo, no descongelaste el pollo):")
print("cifrar la frase Mateo, no descongelaste el pollo con" \
" una llave de 10:\n", cifrar_mensaje("Mateo, no descongelaste el pollo", 10))

print("Wkdoy, xy nocmyxqovkcdo ov zyvvy (mensaje anterior) descifrado con la misma llave de 10:\n",
       descifrar_mensaje("Wkdoy, xy nocmyxqovkcdo ov zyvvy", 10))

print("Mensajes posibles para 'Wkdoy, xy nocmyxqovkcdo ov zyvvy':")
descifrar_mensajes_posibles("Wkdoy, xy nocmyxqovkcdo ov zyvvy")