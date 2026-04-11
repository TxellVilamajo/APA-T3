# Tercera tarea de APA: Multiplicación de vectores y ortogonalidad

## Nom i cognoms

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Txell Vilamajó i Puixeu

## Aviso Importante

> [!Caution]
>
> 
> El objetivo de esta tarea es programar en Python usando el pardigma de la programación
> orientada a objeto. Es el alumno quien debe realizar esta programación. Existen bibliotecas
> que, si lugar a dudas, lo harán mejor que él, pero su uso está prohibido.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Fecha de entrega: 6 de abril a medianoche

## Clase Vector e implementación de la multiplicación de vectores

El fichero `algebra/vectores.py` incluye la definición de la clase `Vector` con los
métodos desarrollados en clase, que incluyen la construcción, representación y
adición de vectores, entre otros.

Añada a este fichero los métodos siguientes, junto con sus correspondientes
tests unitarios.

### Multiplicación de los elementos de dos vectores (Hadamard) o de un vector por un escalar

- Sobrecargue el operador asterisco (`*`, correspondiente a los métodos `__mul__()`,
  `__rmul__()`, etc.) para implementar el producto de Hadamard (vector formado por
  la multiplicación elemento a elemento de dos vectores) o la multiplicación de un
  vector por un escalar.

  - La prueba unitaria consistirá en comprobar que, dados `v1 = Vector([1, 2, 3])` y
    `v2 = Vector([4, 5, 6])`, la multiplicación de `v1` por `2` es `Vector([2, 4, 6])`,
    y el producto de Hadamard de `v1` por `v2` es `Vector([4, 10, 18])`.

- Sobrecargue el operador arroba (`@`, multiplicación matricial, correspondiente a los
  métodos `__matmul__()`, `__rmatmul__()`, etc.) para implementar el producto escalar
  de dos vectores.

  - La prueba unitaria consistirá en comprobar que el producto escalar de los dos
    vectores `v1` y `v2` del apartado anterior es igual a `32`.

### Obtención de las componentes normal y paralela de un vector respecto a otro

Dados dos vectores $v_1$ y $v_2$, es posible descomponer $v_1$ en dos componentes,
$v_1 = v_1^\parallel + v_1^\perp$ tales que $v_1^\parallel$ es tangencial (paralela) a
$v_2$, y $v_1^\perp$ es normal (perpendicular) a $v_2$.

> Se puede demostrar:
>
> - $v_1^\parallel = \frac{v_1\cdot v_2}{\left|v_2\right|^2} v_2$
> - $v_1^\perp = v_1 - v_1^\parallel$

- Sobrecargue el operador doble barra inclinada (`//`, métodos `__floordiv__()`,
  `__rfloordiv__()`, etc.) para que devuelva la componente tangencial $v_1^\parallel$.

- Sobrecargue el operador tanto por ciento (`%`, métodos `__mod__()`, `__rmod__()`, etc.)
  para que devuelva la componente normal $v_1^\perp$.

> Es discutible esta elección de las sobrecargas, dado que extraer la componente
> tangencial no es equivalente a ningún tipo de división. Sin embargo, está
> justificado en el hecho de que su representación matemática es dos barras
> paralelas ($\parallel$), similares a las usadas para la división entera (`//`).
>
> Por otro lado, y de manera *parecida* (aunque no idéntica) al caso de la división
> entera, las dos componentes cumplen: `v1 = v1 // v2 + v1 % v2`, lo cual justifica
> el empleo del tanto por ciento para la componente normal.

- En este caso, las pruebas unitarias consistirán en comprobar que, dados los vectores
  `v1 = Vector([2, 1, 2])` y `v2 = Vector([0.5, 1, 0.5])`, la componente de `v1` paralela
  a `v2` es `Vector([1.0, 2.0, 1.0])`, y la componente perpendicular es `Vector([1.0, -1.0, 1.0])`.

### Entrega

#### Fichero `algebra/vectores.py`

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno
  y los tests unitarios de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido
  de la función, los argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el
  uso de los estándares marcados por PEP-ocho.

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el
fichero `algebra/vectores.py` con la opción *verbosa*, de manera que se muestre el
resultado de la ejecución de los tests unitarios.

![Imatge tests unitaris](Tests%20Unitaris%20vectors.png)


#### Código desarrollado

Inserte a continuación el código de los métodos desarrollados en esta tarea, usando los
comandos necesarios para que se realice el realce sintáctico en Python del mismo (no
vale insertar una imagen o una captura de pantalla, debe hacerse en formato *markdown*).

```python 
'''
Txell Vilamajó i Puixeu
TASCA 3: APA CURS 2025 - 2026

Classe per la grestió de vectors:

Tests uniteris:
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])

>>> v1 * v2
Vector([4, 10, 18])

>>> v1 @ v2
32

>>> v3 = Vector([2, 1, 2])
>>> v4 = Vector([0.5, 1, 0.5])
>>> v3 // v4
Vector([1.0, 2.0, 1.0])

>>> v3 % v4
Vector([1.0, -1.0, 1.0])
'''
# Com que és una classe el nom comença en MAJUSCULA
'''
Txell Vilamajó i Puixeu
TASCA 3: APA CURS 2025 - 2026

Classe per la grestió de vectors:

Tests uniteris:
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])

>>> v1 * v2
Vector([4, 10, 18])

>>> v1 @ v2
32

>>> v3 = Vector([2, 1, 2])
>>> v4 = Vector([0.5, 1, 0.5])
>>> v3 // v4
Vector([1.0, 2.0, 1.0])

>>> v3 % v4
Vector([1.0, -1.0, 1.0])
'''
# Com que és una classe el nom comença en MAJUSCULA
class Vector:
    vector = []  # Una llista buida també es pot crear amb: vector = list() 
    # VECTOR:
        # Compost
        # Mutable 
        # Hi ha un ordre 
            # --> Tot això encaixa amb la LLISTA!

    # Quan cridem a la classe s'executen dos mètodes magics:
        # __new__() --> És el veritable constructor de la classe, però habitualment mai utilitzem un metode ne diferent al que hi ha per defecte. Només el modifiquem si volguessim canviar l'espai de memòria on està situat. 
        # __init__ --> A tots els efectes és el constructor que utilitzarem SEMPRE i ha de ser un mètode que no retorni res (que retorni NONE)

    # Quan vulguem fer un constructor de la classe Vector haurem de fer:
    def __init__(self, iterable):  # Primer hem de posar l'objecte (self) i l'argument iterable (podem anar recorrent per agafar els valors)
        self.vector = [element for element in iterable]
        # [expresió for element in iterable if condicio]
            # Podem no posar algunes de les pars, per exemple a vegades no fa falta posar condicions

# ------------------------------------------------------------------------------------
    
    def __repr__(self):
        '''
        Representació oficial del vector
            Passem com a argument el propi vector.
        '''
        return "Vector(" + repr(self.vector) + ")"

# ------------------------------------------------------------------------------------

    def __str__(self):
        '''
        Representació bonica (string) del vector
            Passem com a argument el propi vector i obtenim la representació d'aquest
        '''
        return str(self.vector)

# ------------------------------------------------------------------------------------

    def __len__(self):  
        '''
        Funció que retorna la longitud del vector
            Passem com a argument el propi vector i obtenim la longitud d'aquest. 
        '''
        return len(self.vector)  

# ------------------------------------------------------------------------------------
    def __getitem__(self, key):
        """
        Retrona l'element kèssim del vector
        """
        return self.vector[key]


    def __setitem__(self, key, value):
        """
        Permet l'assignació de valors al vector
        """
        self.vector[key] = value
# ------------------------------------------------------------------------------------
    
    def __mul__ (self, other):
        '''
        Multiplicacio vector*vector o vector*numero
            Passem com a argument dos vectors o un vector i un escalar.
            Retorna un vector que eés el resultat de la multiplicació vector*vector o vector*numero
        '''
        if isinstance(other, (int, float, complex)):
            return Vector([element*other for element in self])

        else:
            return Vector([un*altre for un, altre in zip(self, other)])
 

# ------------------------------------------------------------------------------------

    __rmul__=__mul__

# ------------------------------------------------------------------------------------

    def __matmul__(self, other):
        '''
        Producte escalar (operador @)
            v1[0]*v2[0] + v1[1]*v2[1]...
            Passem com a arguments dos vectors per tal de fer el producte escalar.
        '''
        if not isinstance(other, Vector):
            raise TypeError("El producte escalar només es pot fer entre dos vectors.")
    
        if len(self) != len(other):
            raise ValueError("Els vectors han de tenir la mateixa longitud.")

        # Multipliquem parelles i sumem el resultat
        return sum(un * altre for un, altre in zip(self, other))
        
# ------------------------------------------------------------------------------------

    def __floordiv__(self, other):
        '''
        Retorna la component paralela (operador //)
            ((v1 @ v2) / (v2 @ v2)) * v2
            Passem com a arguments dos vectors.
        '''
        return ((self @ other) / (other @ other)) * other

# ------------------------------------------------------------------------------------

    def __sub__(self, other):  # El necessitem per després poder fer la resta en el __mod__
        '''
        Resta de vectors (self - other)
        '''
        # Fem la resta element a element
        return Vector([un - altre for un, altre in zip(self, other)])
        

    def __mod__(self, other):
        '''
        Retorna la component normal
            v1 - v1_paralela
            Passem com a arguments dos vectors.
        '''
        return self - (self // other)

        
# ------------------------------------------------------------------------------------
    
# PER TAL QUE ELS TEST UNITARIS FUNCIONIN:
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

#### Subida del resultado al repositorio GitHub y *pull-request*

La entrega se formalizará mediante *pull request* al repositorio de la tarea.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y
visualizarse correctamente en el repositorio, incluyendo la imagen con la ejecución de
los tests unitarios y el realce sintáctico del código fuente insertado.
