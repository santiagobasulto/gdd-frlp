'''
Created on 01/09/2011

@author: santiago
'''
import unittest

from hashtable import HashTable

class HashTableTest(unittest.TestCase):
    clave = "JKAJ"
    valor = "Hu2Aw"
    
    def creaTablaTest(self):
        h = HashTable(elementos=100)
        self.assertEquals(0,len(h))
        
    def insertaElementoTest(self):
        h = HashTable()
        h.put(self.clave,self.valor)
        self.assertEquals(self.valor,h.get(self.clave))
        