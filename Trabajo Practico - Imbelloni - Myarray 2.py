#Matriz con Lista de listas
class myarray () : 
    def __init__ (self,elems, r, c, by_row) :
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row
        
    def matriz(self) : 
        if self.by_row == True : 
            x = self.c
            y = 0
            new_elems = []
            for i in range(self.r): 
                new_elems.append(list(self.elems[y:x:]))
                x = x + self.c
                y = y + self.c
            salida = new_elems
            
        else : 
            x = self.r
            y = 0
            new_elems = []
            for i in range(self.c): 
                new_elems.append(list(self.elems[y:x:]))
                x = x + self.r
                y = y + self.r
            salida = new_elems
        return salida
            
    def get_pos(self, j, k):
        """"Funcion en la que se ponen como parametros las coordenadas de un elemento de la matriz y se devuelve la posicion del elemento en la lista, elems"""
        lista = myarray.matriz(self)
        elem = lista[j][k] 
        return self.elems.index(elem)
            
    
    def get_cords(self, p) : 
        """"Funcion que toma como parametro la posicion de un elemento en la lista, elems y devuelve las coordenadas del elemento en la matriz"""
        lista = myarray.matriz(self)
        for i in range(len(lista)): 
                if lista[i][p] == self.elems[p]:
                    return i,p
                
    def switch(self) : 
         """"Funcion que altera el orden de los elementos de la lista, elems y cambia el valor de la variable by_row por su valor opuesto"""
         new_elems = self.elems[::-1] 
         new_by_row = not self.by_row  
         return myarray(new_elems, self.r, self.c,new_by_row )
     
    def get_row(self, j) :
         """"Funcion que toma como parametro un numero de fila y te devuelve los elementos de la fila """
         lista = myarray.matriz(self)
         if self.by_row == True : 
             salida = lista[j]
            
         else : 
             lista2 = []
             for i in range(self.c) :
                 x = lista[i][j]
                 lista2.append(x)
             salida = lista2
            
         return salida
     
    def get_col(self, k) : 
        """"Funcion que toma como parametro un numero de columna y te devuelve los elementos de la fila """
        lista = myarray.matriz(self)
        if self.by_row == True : 
           new_lista = []
           for i in range(len(lista)): 
               new_lista.append(lista[i][k])   
               salida = new_lista
        else : 
         salida =  lista[k]  
        return salida
    
    def get_elem(self, i) :
        """"Funcion que toma como parametro la posicion de un elemento de la matriz y te devuelve el valor del elemento """
        j,k = i
        lista = myarray.matriz(self)
        return lista[j][k]
    
    def del_row (self, j) :
        """"Funcion que toma como parametro un numero de fila para poder borrar dicha fila y te devuelve los elementos de la matriz que no fueron eliminados """
        lista = myarray.matriz(self)
        if self.by_row ==  True : 
            lista.pop(j)
            
        else : 
            for i in range(self.c) :
                x = lista[i][j]
                lista[i].remove(x)         
        return lista
         
    def del_col (self, k) : 
        """"Funcion que toma como parametro un numero de columna para poder borrar dicha fila y te devuelve los elementos de la matriz que no fueron eliminados """
        lista = myarray.matriz(self)
        if self.by_row == True : 
            for i in range(self.r) :
                x = lista[i][k]
                lista[i].remove(x) 
                salida = lista
            
        else : 
            salida = lista.pop(k)
        return salida
      
    def swap_rows(self, j , k) :
        """"Funcion que toma como parametro dos filas de la matriz y las intercambia de poscion """
        lista = myarray.matriz(self)
        if self.by_row == True :
            x = lista[j]
            lista[j] = lista[k]
            lista[k] = x    
            
        else : 
            for i in range(j,k+1) :
                x = lista[i][k]
                lista[i][k] = lista[i][j]
                lista[i][j] = x
        return lista
    
    def swap_cols (self, l, m) :
        """"Funcion que toma como parametro dos columnas de la matriz y las intercambia de poscion """
        lista = myarray.matriz(self)
        if self.by_row == True :
           for i in range(l,m+1) :
               x = lista[i][l]
               lista[i][l] = lista[i][m]
               lista[i][m] = x 
            
        else : 
            x = lista[l]
            lista[l] = lista[m]
            lista[m] = x    
        return lista
    
    def scale_row (self, j, x) : 
        """"Funcion que toma como parametro, una fila de la matriz y un numero por el cual va a multiplicar la fila ingresada de la matriz"""
        lista = myarray.matriz(self)
        row = self.get_row(j)
        if self.by_row == True : 
            for i in range(self.c) : 
                e = row[i]
                y = e * x 
                lista[j][i] = y
                
        else : 
            for i in range(self.c) : 
                e = row[i]
                y = e * x 
                lista[i][j] = y
        
        return lista
    
    def scale_col (self, k, y) :
        """"Funcion que toma como parametro, una columna de la matriz y un numero por el cual va a multiplicar la columna ingresada de la matriz"""
        lista = myarray.matriz(self)
        col = self.get_col(k)   
        if self.by_row == True : 
            for i in range(self.r) : 
                e = col[i]
                x = e * y
                lista[i][k] = x
                
        else : 
            for i in range(self.r) : 
                e = col[i]
                x = e * y
                lista[k][i] = x
        return lista
    
    def transpose(self) : 
        """"Funcion que cambia las columnas por las filas y las filas por las columnas, es decri que calcula la transversa de la matriz"""
        if self.by_row ==  True : 
            x = self.c
            y = 0
            new_elems = []
            for i in range(self.r): 
                new_elems.append(list(self.elems[y:x:]))
                x = x + self.c
                y = y + self.c
            salida = new_elems
            
        else : 
            x = self.r
            y = 0
            new_elems = []
            for i in range(self.c): 
                new_elems.append(list(self.elems[y:x:]))
                x = x + self.r
                y = y + self.r
            salida = new_elems
        return salida
            
    def flip_row(self):
        """"Funcion que devuelvenuna copia del los elemementos de la clase, pero reflejado especularmente en sus filas."""
        lista_final = []
        for i in range (self.r-1, -1, -1) : 
            row = self.get_row(i)
            lista_final.append(row)
        return lista_final
            
    def flip_col(self):
        """"Funcion que devuelvenuna copia del los elemementos de la clase, pero reflejado especularmente en sus columnas."""
        lista_final = []
        for i in range (self.c-1, -1, -1) : 
            col = self.get_col(i)
            lista_final.append(col)
        return lista_final
            
        
  
matriz = myarray([1, 2, 3, 4, 5, 6], 2, 3, True)


                
                
                
                
                
                
                
                