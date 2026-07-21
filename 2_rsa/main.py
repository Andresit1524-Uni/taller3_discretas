#RSA
#Para usar este programa, simplemente ejecute este archivo (main.py)
#Luego en el archivo de tests.py, podrá probar lo definido aquí.

#Primero creamos la funcion que nos permite calcular el inverso modular de un número n módulo m
def inverso_modular(e, phi_n):
  #Iniciamos guardando el valor original de phi_n, y asignando los valores iniciales
  #De los coeficientes de la ecuacion de bezout, que nos permite calcular el inverso modular
  m0 = phi_n
  r0 = 0
  r1 = 1
  #Aqui se comprueba que phi_n sea mayor a 1, ya que si no lo es, no se puede calcular el inverso modular
  if phi_n < 2: 
    print('phi_n no es un valor válido, no puede ingresar estos valores de p y q')
    return None
  #Aquí aplicamos el algoritmo extendido de euclides
  while e > 1:
    #Esta condicion se da en el caso de que e y phi_n no sean coprimos, debido a que
    #si al iterar phi_n se vuelve 0 y e no ha llegado a 1 o menos, significa que
    #el mcd de e y phi es mayor a 1, por lo que no existe el inverso modular
    if phi_n == 0:
      print('e no es un valor válido para los valores de p y q ingresados')
      return None
    
    #En este bloque, calculamos el cociente de la division entera de e entre phi_n, 
    # y luego actualizamos los valores de e y phi_n para seguir iterando
    cociente = e // phi_n
    e, phi_n = phi_n, e % phi_n

    #En este punto, actualizamos los valores de r0 y r1, coeficientes de la ecuacion de bezout
    #Cuando r0 = 1, significa que hemos encontrado el inverso modular, y lo devolvemos
    r0, r1 = r1 - cociente*r0, r0
  
  #Ya que el coeficiente r1 puede dar negativo en la operacion anterior, aprovechamos
  #las propiedades de la aritmética modular para devolver un valor positivo, sumandole el modulo
  if r1 < 0:
    r1 = r1+m0

  return r1

#Definimos la funcion que nos permite cifrar un mensaje con el cifrado RSA
def cifrar_rsa(m, p, q, e):
  #Calculamos n
  n = p*q
  print("La llave pública es: ", n)
  #Calculamos phi_n y el inverso modular de e módulo phi_n, que nos da la llave privada d
  phi_n = (p-1)*(q-1)
  print("phi_n es: ", phi_n)
  d = inverso_modular(e, phi_n)
  #En este bloque comprobamos que d no sea nulo, ya que si lo es, significa que no se puede 
  # cifrar el mensaje con los valores de ingresados
  if d is not None:
    print("La llave privada es: ", d)
    #Ciframos el mensaje con la formula c = (m**e) mod n
    c = (m**e)% n
    print("El mensaje cifrado es: ", c)
  else:
    print("No se puede cifrar el mensaje")
  
#Aquí se define la función para descifrar un mensaje con el cifrado RSA
def descifrar_rsa(c, n, d):
    #Desciframos el mensaje con la formula m = (c**d) mod n
  m = (c**d) % n
  print("El mensaje descifrado es: ", m)