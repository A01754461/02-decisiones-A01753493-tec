"""
Ordena 3 números;
Ingresa el primer número;
Ingresa el segundo número;
Ingresa el tercer número;
if (X es menor o igual a Y AND X es menor o igual a Z)
{
  if (Y es menor o igual a Z)
  {
    X es el número menor;
    Y es el número medio;
    Z es el número mayor;
  }
  else
  {
    X es el número menor;
    Z es el número medio;
    Y es el número mayor;
  }
  
}
else
{
  if (Y es menor o igual a X AND Y es menor o igual a Z)
  {
    if(X es menor o igual a Z)
    {
      Y es el número menor;
      X es el número medio;
      Z es el número mayor;
    }
    else
    {
      Y es el número menor;
      Z es el número medio;
      X es el número mayor;
    }
  }
  else
  {
    if (Z es menor o igual a X AND Z es menor o igual a Y)
    {
      if(X es menor o igual a Y)
      {
        Z es el número menor;
        X es el númmero medio;
        Y es el número mayor;
      }
      else
      {
        Z es el número menor;
        Y es el número medio;
        X es el número mayor;
      }
    }
  }
}
"""
def main():
 x = int(input("Ingresa el primer número:"))
 y = int(input("Ingresa el segundo número:"))
 z = int(input("Ingresa el tercer número:"))
 if (x <= y) and (x <= z):
   nmenor = x
   if (y <= z):
     nmedio = y
     nmayor = z
   else:
     nmedio = z
     nmayor = y
 elif (y <= x and y <= z):
   nmenor = y
   if (x <= z):
     nmedio = x
     nmayor = z
   else:
     nmedio = z
     nmayor = x
 else:
   nmenor = z
   if (x <= y):
     nmedio = x
     nmayor = y
   else:
     nmedio = y
     nmayor = x
 print (nmenor)
 print (nmedio)
 print (nmayor)

if __name__=='__main__':
    main()
