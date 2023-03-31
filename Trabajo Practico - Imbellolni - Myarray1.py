#TP - Matrices
class myarray () : 
    def __init__ (self,elems, r, c, by_row) :
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row
        
    def get_pos(self, j, k):
        """"Funcion en la que se ponen como parametros las coordenadas de un elemento de la matriz y se devuelve la posicion del elemento en la lista, elems"""
        p = 0
        if self.by_row == True : 
             for i in range(0, self.r) : 
                 if i == j :
                     p = i *self.c + k 
        else : 
             for i in range(self.c) :
                 if i == k : 
                     p = i*self.r + j
        return p
                 
    def get_cords(self, p) : 
        """"Funcion que toma como parametro la posicion de un elemento en la lista, elems y devuelve las coordenadas del elemento en la matriz"""
        if self.by_row == True : 
            j = p // self.c
            k = p % self.c
            
        else : 
            j = p // self.r
            k = p % self.r
        return (j,k)
    
    def switch(self) : 
        """"Funcion que altera el orden de los elementos de la lista, elems y cambia el valor de la variable by_row por su valor opuesto"""
        new_elems = self.elems[::-1] 
        new_by_row = not self.by_row  
        return myarray(new_elems, self.r, self.c,new_by_row )
     
    def get_row(self, j) :
        """"Funcion que toma como parametro un numero de fila y te devuelve los elementos de la fila """
        if self.by_row ==True : 
            start = j * self.c
            end = start + self.c
            salida = self.elems[start:end:]
            
        else : 
            start = j 
            end = (self.r * self.c) + start 
            salida = self.elems[start:end:self.r]
        return salida
    
    def get_col(self, k) : 
        """"Funcion que toma como parametro un numero de columna y te devuelve los elementos de la fila """
        if self.by_row == True : 
            start = k
            end = (self.r * self.c) + start 
            salida = self.elems[start:end:self.c]
            
        else : 
            start = k * self.r
            end = start + self.r
            salida = self.elems[start:end:]
        return salida
    
    def get_elem(self, i) :
        """"Funcion que toma como parametro la posicion de un elemento de la matriz y te devuelve el valor del elemento """
        j,k = i
        if self.by_row == True : 
            row = self.get_row(j)
            salida = row[k]
            
        else : 
            col = self.get_col(k)
            salida = col[j]
        return salida
        
  
    def del_row (self, j) :
        """"Funcion que toma como parametro un numero de fila para poder borrar dicha fila y te devuelve los elementos de la matriz que no fueron eliminados """
        row = self.get_row(j)
        for i in row: 
            self.elems.remove(i)
        return self.elems
    
    def del_col (self, k) : 
        """"Funcion que toma como parametro un numero de columna para poder borrar dicha fila y te devuelve los elementos de la matriz que no fueron eliminados """
        col = self.get_col(k)
        for i in col: 
            self.elems.remove(i)
        return self.elems
    
    def swap_rows(self, j , k) : 
        """"Funcion que toma como parametro dos filas de la matriz y las intercambia de poscion """
        row_1 = list(self.get_row(j))
        row_2 = list(self.get_row(k))
        for i in range (len(self.elems)) :
            if self.elems[i] == row_1[i-self.c] : 
                self.elems[i] = row_2[i]
        
            elif self.elems[(i)] == row_2[i-self.c] : 
                    self.elems[i] = row_1[i-self.c]
                
        return self.elems
            
    
    def swap_cols (self, l, m) :
        """"Funcion que toma como parametro dos columnas de la matriz y las intercambia de poscion """
        for i in range (self.r) : 
            col1 = self.get_pos(i, l)
            col2 = self.get_pos(i, m)
            x = self.elems[col1]
            self.elems[col1] = self.elems[col2]
            self.elems[col2] = x
        return self.elems
                    
        
    def scale_row (self, j, x) : 
        """"Funcion que toma como parametro, una fila de la matriz y un numero por el cual va a multiplicar la fila ingresada de la matriz"""
        row = self.get_row(j)
        for i, e in enumerate(row) : 
            p_row = self.get_pos(j, i)
            self.elems[p_row] = e * x
        return self.elems
    
    def scale_col (self, k, y) :
        """"Funcion que toma como parametro, una columna de la matriz y un numero por el cual va a multiplicar la columna ingresada de la matriz"""
        col = self.get_col(k)
        for i, e in enumerate(col) : 
            p_col = self.get_pos(i , k)
            self.elems[p_col] = e * y
        return self.elems            
       
    def transpose(self) : 
        """"Funcion que cambia las columnas por las filas y las filas por las columnas, es decri que calcula la transversa de la matriz"""
        if self.by_row ==  True : 
            c = self.r
            r = self.c 
            salida = myarray(self.elems,r,c, False)
        else : 
            c = self.r
            r = self.c 
            salida = myarray(self.elems,r,c, True)
        return salida 
    
    def flip_row(self):
        """"Funcion que devuelvenuna copia del los elemementos de la clase, pero reflejado especularmente en sus filas."""
        lista = []
        for i in range (self.r-1, -1, -1) : 
            row = self.get_row(i)
            for e in row : 
                lista.append(e)
        return lista
    
    def flip_cols(self) : 
        """"Funcion que devuelvenuna copia del los elemementos de la clase, pero reflejado especularmente en sus columnas."""
        lista = []
        for i in range (self.c-1, -1, -1) : 
            row = self.get_col(i)
            for e in row : 
                lista.append(e)
        return lista
        
   
matriz = myarray([1, 2, 3, 4, 5, 6], 2, 3, True)






