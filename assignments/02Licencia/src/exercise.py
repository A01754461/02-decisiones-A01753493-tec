"""
Licencia de manejo;
Ingresa tu edad;
if (Edad mayor a 0)
{
  if (Edad mayor o igual a 18)
  {
    if (¿Tienes identificación oficial?(s/n))
    {
      Imprimir Trámite de licencia concedido;
    }
    else 
    {
      if (Respuesta es igual n?)
      {
        Imprimir No cumples con los requisitos 
      }
      else
      {
        Imprimir Respuesta Incorrecta
      }
    }
  }
  else
  {
    Imprimir No cumples con los requisitos;
  }
}
else
{
  Imprimir Respuesta Incorrecta;
}
"""
def main():
 edad = int(input("Ingresa tu edad:"))
 if(edad>0):
    if(edad >= 18):
        ofic = str(input("¿Tienes identificación oficial?(s/n):"))
        if(ofic == "s"):
            print ("Trámite de licencia concedido")
        else:
            if(ofic == "n"):
                print("No cumples requisitos")
            else:
                print("Respuesta incorrecta")
    else:
        print("No cumples requisitos")
 else:
    print ("Respuesta incorrecta")


if __name__ == '__main__':
    main()
