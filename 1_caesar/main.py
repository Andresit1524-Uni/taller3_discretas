#Cifrado de cesar
#Para este ejercicio, simplemente ejecute este archivo primero
#Luego en el archivo de tests.py, podrá probar lo definido aquí.

#Primero creamos la funcion que nos permite cifrar un mensaje con el cifrado de cesar
def cifrar_mensaje(mensaje, k):
  #Creamos un arreglo vacio donde guardaremos el resultado del cifrado
  resultado = []
  #Luego iteramos sobre cada letra que contenga el mensaje original
  for i in mensaje:
    #Para poder mover la letra, obtenemos el código ascii del caracter
    # (Obteniendo a su vez su "posicion" en el abecedario)
    ascii_letra = ord(i)
    # Si el caracter no es una letra, lo añadimos tal y como está al resultado
    if not((ascii_letra>=97 and ascii_letra<=122) or (ascii_letra>=65 and ascii_letra<=90)):
      resultado.append(i)
    # En caso de ser una letra, primero comprobamos si es mayúscula o minúscula
    # Luego, obtenemos la posicion de la letra "a" en el código dependiendo de lo anterior
    else:
      base_ascii = 65 if i.isupper() else 97 
      #Para la letra cifrada, tomamos el ascii de la letra, le restamos el ascii de la base
      #Le sumamos k (las posiciones que se moverá), le hacemos un modulo 26 
      # (para que si pasa de la z vuelva a la a), volvemos a sumarle la base y convertimos
      # el resultado a un caracter, el cual añadimos al resultado final
      resultado.append(chr((ascii_letra - base_ascii + k) % 26 + base_ascii))
  return "".join(resultado)

#Para descrifrar el mensaje, hacemos el mismo procedimiento que para cifrarlo,
# pero en vez de sumarle k, se lo restamos de manera que volvamos hacia atrás a la letra original.
def descifrar_mensaje(mensaje, k):
  resultado = []
  for i in mensaje:
    ascii_letra = ord(i)
    if not((ascii_letra>=97 and ascii_letra<=122) or (ascii_letra>=65 and ascii_letra<=90)):
      resultado.append(i)
    else:
      base_ascii = 65 if i.isupper() else 97
      resultado.append(chr((ascii_letra - base_ascii - k) % 26 + base_ascii))
  return "".join(resultado)

#Por ultimo, para poder descifrar un mensaje sin conocer la llave
#Usamos el mismo principio que para cifrar, recorriendo todos los posibles valores
#de k (de 0 a 25) y mostrando el resultado de cada uno, 
# de modo que el usuario pueda distinguir cual es el mensaje original.
def descifrar_mensajes_posibles(mensaje):
  for k in range(26):
    resultado = []
    for i in mensaje:
      ascii_letra = ord(i)
      if not((ascii_letra>=97 and ascii_letra<=122) or (ascii_letra>=65 and ascii_letra<=90)):
        resultado.append(i)
      else:
        base_ascii = 65 if i.isupper() else 97
        resultado.append(chr((ascii_letra - base_ascii + k) % 26 + base_ascii))
    print("".join(resultado))