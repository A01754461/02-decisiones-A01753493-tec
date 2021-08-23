"""
Índice de mása corporal;
Ingresa tu peso en kg:;
Ingresa tu altura en m:;
if (peso es menor o igual a 0)
{
  if (altura es menor o igual a 0)
  {
    Imprimir Revisa tus datos, alguno de ellos es erróneo.;
  }
  else
  {
    Imprimir Revisa tus datos, alguno de ellos es erróneo.;
  }
}
else
{
  if (Índice es menor a 20)
  {
    Imprimir PESO BAJO;
  }
  else
  {
    if (20 es menor o igual a índice e índice es menor a 25)
    {
      Imprimir NORMAL;
    }
    else
    {
      if (25 es menor o igual a índice e índice es menor a 30)
      {
        Imprimir SOBREPESO;
      }
      else
      {
        if (30 es menor o igual a índice e índice es menor a 40)
        {
          Imprimir OBESIDAD;
        }
        else
        {
          if (Índice es mayor o igual a 40)
          {
            Imprimir OBESIDAD MORBIDA;
          }
        }
      }
    }
  }
}
"""
def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg:"))
    altura = float(input("Altura en m:"))
    indice = peso / altura ** 2
    if (peso <= 0):
      print ("Revisa tus datos, alguno de ellos es erróneo.")
    else:
         if (altura <= 0):
          print ("Revisa tus datos, alguno de ellos es erróneo.") 
         else:
             if (indice < 20):
                print("PESO BAJO")
             else:
                if (20 <= indice < 25):
                    print ("NORMAL")
                else:
                    if (25 <= indice < 30):
                        print ("SOBREPESO")
                    else:
                        if (30 <= indice < 40):
                            print ("OBESIDAD")
                        else:
                            if (indice >= 40):
                                print("OBESIDAD MORBIDA")
    
           
if __name__=='__main__':
    main()