"""
De centímetros a Kilómetros, Metros y Centímetros;
Introduce los cm:;
if (centímietros menores a 100)
{
  Imprimir Cm:;
}
else
{
  if (centímetros son menores a 1000)
  {
    Imprimir m;
    Imprimir cm;
  }
  else
  {
    if (centímetros son mayores o iguales a 100000)
    {
      Imprimir Km;
      Imprimir M;
      Imprimir Cm
    }
  }
}   
"""
def main():
    # Escribe tu código abajo de esta línea
    c = int(input("Introduce los cm:"))
    if (c < 100):
     cm = c
     print (cm, "cm")
    else:
      if (c < 1000):
        m = (c // 100)
        cm = (c - m * 100)
        print (m, "m")
        if (cm != 0):
            print (cm, "cm")
      else:
        if (c >= 100000):
            km = (c // 100000)
            res = (c - km * 100000)
            m = (res // 100)
            cm = (res - m * 100)
            print (km, "km")
            if (m != 0):
                print (m, "m")
            if (cm != 0):
               print (cm, "cm")  

if __name__ == '__main__':
    main()
