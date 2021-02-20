
def INICIO ():
  input('Enter para volver a inicio.')
  CAJERO()
def CAJERO ():

  print('BANCO FDP INVERSMENTS.')
  
  print('1: Este banco.')
  print('2: Otro banco.')

  BANCO  = int(input('Seleccione su banco:'))

  if BANCO == 1:
    MONTO1= int(input('Monto a retirar:'))
    if MONTO1 > 20000:
      print('Este monto no es permitido por su banco.')
      INICIO()
    else: 
      if MONTO1 <= 20000:
        bi1000 = MONTO1 //1000
        print( str (bi1000) + ' de 1000.')
        MONTO1 = MONTO1 % 1000

        bi500 = MONTO1 // 500
        print(str (bi500) + ' de 500.')
        MONTO1 = MONTO1 % 500

        bi200 = MONTO1 // 200
        print(str (bi200)+ ' de 200.')
        MONTO1 = MONTO1 % 200

        bi100 = MONTO1 // 100
        print(str (bi100)+ ' de 100.')
        MONTO1=MONTO1 % 100
        INICIO()

  if BANCO == 2:
    MONTO2= int(input('Monto a retirar:'))
    if MONTO2 > 10000:
      print('Este monto no es permitido por su banco.')
      INICIO()
    else: 
      if MONTO2 <= 20000:
        bi1000 = MONTO2 // 1000
        print( str (bi1000) + ' de 1000.')
        MONTO2 = MONTO2 % 1000

        bi500 = MONTO2 // 500
        print(str (bi500) + ' de 500.')
        MONTO = MONTO2 % 500

        bi200 = MONTO2 // 200
        print(str (bi200)+ ' de 200.')
        MONTO = MONTO2 % 200

        bi100 = MONTO2 // 100
        print(str (bi100)+ ' de 100.')
        MONTO2=MONTO2 % 100
        INICIO()
  else:
      INICIO()

 

CAJERO()
