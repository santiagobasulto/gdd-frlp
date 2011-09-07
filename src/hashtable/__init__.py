def funcionModularSimple(clave):
    return hash(clave)

class HashTable:
    def __init__(self,capacidad=100,funcion_hash=funcionModularSimple,factor_carga = 0.75):
        self.elementos = [None for i in range(capacidad)]
        self.cantidad_elementos = capacidad
        self.funcion_hash = funcion_hash
        self.factor_carga = factor_carga
        self.carga_maxima = int(self.factor_carga*capacidad) 
        pass
    
    #TODO
    def rehash(self,nueva_capacidad):
        pass
    def acotar_clave(self,valor):
        """Acota la clave para que entre en la tabla"""
        return valor % self.cantidad_elementos
    
    def put(self,clave,valor):
        index = self.acotar_clave(self.funcion_hash(clave))
        if self.elementos[index] is None:
            self.elementos[index] = [(clave,valor)]
        else:
            elementos_anteriores = self.elementos[index]
            replace = False
            for i,e in enumerate(elementos_anteriores):
                if e[0]==clave:
                    elementos_anteriores[i] = (clave,valor)
                    replace = True
                    break
            if not replace:
                elementos_anteriores.append((clave,valor))
                self.cantidad_elementos += 1
                if self.cantidad_elementos >= self.carga_maxima:
                    self.rehash(self.calcular_nueva_capacidad())
            # El codigo de arriba puede ser reemplazado por
            #f = lambda t,c,v: t[0] == c and (c,v) or t 
            #elementos_anteriores = [f(t,clave,valor) for t in elementos_anteriores]
            self.elementos[index] = elementos_anteriores

    def get(self,clave):
        index = self.acotar_clave(self.funcion_hash(clave))
        elementos =self.elementos[index]
        if elementos is None or len(elementos)==0:
            return None
        for e in elementos:
            if e[0]==clave:
                return e[1]
        return None
    
    def __len__(self):
        return len(self.elementos)