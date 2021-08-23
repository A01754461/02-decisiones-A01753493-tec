"""
Año bisiesto;
Ingresa el año:;
if (Año es menor o igual a 0)
{
  Imprimir Dato incorrecto
}
else
{
  if (residuo entre año y 4 es igual a 0)
  {
    if (residuo entre año y 100 es igual a 0)
    {
      if (residuo entre año y 400 es igual a 0)
      {
        Imprimir True
      }
      else
      {
        Imprimir False
      }
    }
    else
    {
      Imprimir True
    }
  }
  else
  {
    Imprimir False
  }
}
"""
def main():
    #escribe tu código abajo de esta línea
  year = int(input("Año:"))
  if (year <= 0):
    print ("Dato incorrecto") 
  else:
    if (year % 4 == 0):
        if (year % 100 == 0):
          if (year % 400 == 0):
              print (True)
          else:
              print (False)
        else:
          print (True)
    else: 
      print (False)
                   
if __name__=='__main__':
    main()
