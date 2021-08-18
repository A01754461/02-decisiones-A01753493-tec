![Tec de Monterrey](../../images/logotecmty.png)
# Año Bisiesto

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
    # Escribe el código adecuado para completar el programa
    year = int(input("Año:"))

if __name__ == '__main__':
    main()
```

Recuerda, la línea `# Escribe el código adecuado para completar el programa` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema  

El siguiente algoritmo se puede usar para determinar si un año determinado es bisiesto:

   * Los años bisiestos son cualquier año que es divisible por 4 (como 2012, 2016, etc).  
   * Excepto si puede dividirse por 100, entonces no lo es (como 2100, 2200, etc).  
   * A menos que pueda ser divisible por 400, como 2000, 2400.

Escribe el programa que determine si un año es bisiesto o no (**True o False**)

**Entradas**  
Un año (**valor entero mayor a cero**).
  
**Salidas**  
La salida será un valor **True** para indicar que el año es bisiesto y **False** si no lo es.   
Si el dato es 0 o menor, deberá mostrar el siguiente mensaje: **Dato incorrecto**
 
## Ejemplos  

Ejemplo 1    

```plaintext
Año:2012
True
```

Ejemplo 2

```plaintext
Año:2100
False
```

Ejemplo 3

```plaintext
Año:1995
False
```

Ejemplo 4

```plaintext
Año:0
Dato incorrecto
```

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
