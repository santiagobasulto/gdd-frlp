'''
Created on 01/09/2011

@author: santiago
'''
import unittest

from hashtable import HashTable

class HashTableTest(unittest.TestCase):
    clave = "JKAJ"
    valor = "Hu2Aw"
    
    valores_test = [('a','b'),('c','d'),('e','f'),('g','h'),('i','j')]
    
    def testCreaTabla(self):
        h = HashTable(capacidad=100)
        self.assertEquals(100,len(h))
        
    def testInsertaElemento(self):
        h = HashTable()
        h.put(self.clave,self.valor)
        self.assertEquals(self.valor,h.get(self.clave))
    
    def testInsertarElementosMismaClave(self):
        h = HashTable()
        h.put(self.clave,self.valor)
        h.put(self.clave,self.valor*2)
        self.assertEquals(self.valor*2,h.get(self.clave))
        
    def testColisiones(self):
        fn_colisionadora = lambda clave : 15
        h = HashTable(funcion_hash=fn_colisionadora)
        #Pongo los valores
        for i in range(2):
            k,v = self.valores_test[i]
            h.put(k,v)
        #Los recupero
        for i in range(2):
            k,v = self.valores_test[i]
            self.assertEquals(v,h.get(k))
    
if __name__ == "__main__":
    unittest.main()