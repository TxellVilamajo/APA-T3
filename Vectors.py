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