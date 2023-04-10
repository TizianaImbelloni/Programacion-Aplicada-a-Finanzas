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
                 
    def get_coords(self, p) : 
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
        elems = []
        for i in range(len(self.elems)):
            if self.get_coords(i)[0] != j:
                elems.append(self.elems[i])
            else:
                pass

        return myarray(elems, self.r, self.c-1, self.by_row)
             
    
    def del_col (self, k) : 
        """"Funcion que toma como parametro un numero de columna para poder borrar dicha fila y te devuelve los elementos de la matriz que no fueron eliminados """
        elems = []
        for i in range(len(self.elems)):
            if self.get_coords(i)[1] != k:
                elems.append(self.elems[i])
            else:
                pass

        return myarray(elems, self.r, self.c-1, self.by_row)
             
    
    def swap_rows(self, j , k) : 
        """"Funcion que toma como parametro dos filas de la matriz y las intercambia de poscion """
        elems_2 = self.elems.copy()
        for i in range (self.c) : 
            row1 = self.get_pos(j, i)
            row2 = self.get_pos(k, i)
            x = elems_2[row1]
            elems_2[row1] = elems_2[row2]
            elems_2[row2] = x
        return myarray(elems_2, self.r, self.c, self.by_row) 
            
    
    def swap_cols (self, l, m) :
        """"Funcion que toma como parametro dos columnas de la matriz y las intercambia de poscion """
        elems_2 = self.elems.copy()
        for i in range (self.r) : 
            col1 = self.get_pos(i, l)
            col2 = self.get_pos(i, m)
            x = elems_2[col1]
            elems_2[col1] = elems_2[col2]
            elems_2[col2] = x
        return myarray(elems_2, self.r, self.c, self.by_row) 
                    
        
    def scale_row (self, j, x) : 
        """"Funcion que toma como parametro, una fila de la matriz y un numero por el cual va a multiplicar la fila ingresada de la matriz"""
        elems_2 = self.elems.copy()
        row = self.get_row(j)
        for i, e in enumerate(row) : 
            p_row = self.get_pos(j, i)
            elems_2[p_row] = e * x
        return myarray(elems_2, self.r, self.c, self.by_row) 
    
    def scale_col (self, k, y) :
        """"Funcion que toma como parametro, una columna de la matriz y un numero por el cual va a multiplicar la columna ingresada de la matriz"""
        elems_2 = self.elems.copy()
        col = self.get_col(k)
        for i, e in enumerate(col) : 
            p_col = self.get_pos(i , k)
            elems_2[p_col] = e * y
        return myarray(elems_2, self.r, self.c, self.by_row) 
    
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
        return myarray(lista, self.r, self.c, self.by_row) 
    
    def flip_cols(self) : 
        """"Funcion que devuelvenuna copia del los elemementos de la clase, pero reflejado especularmente en sus columnas."""
        lista = []
        for i in range (self.c-1, -1, -1) : 
            row = self.get_col(i)
            for e in row : 
                lista.append(e)
        return myarray(lista, self.r, self.c, self.by_row) 
    
    def det (self) : 
        if self.c != self.r :
            print("No se puede utilizar esta funcion ya que la matriz no es cuadrada")
            salida = None
        elif self.c == 2 and self. r == 2 : 
            if self.by_row == True : 
                mult1 = self.elems[0] * self.elems[3] - self.elems[1] * self.elems[2]
               
                if mult1 >= 0 : 
                    print("La matriz es inversible ")
                    
                else : 
                    print("La matriz es inversible")
                
                salida = mult1 
            
        elif self.r != 2 and self.c != 2  and self.c == self.r : 
            lista = []
            for i in range (self.c) : 
                matriz = self.del_col(i)
                matriz = matriz.del_row(0)
                mult = myarray(matriz.elems, 2,2, self.by_row)
                mat = self.elems[i] * mult.det()
                lista.append(mat)   
                
            det = lista[0] - lista[1] + lista[2]
            if det >= 0 : 
                print("La matriz es inversible ")
                
            else : 
                print("La matriz es inversible")
            salida = det 
                
        return salida 
                
    #def inversa (self) : 
        
    def __add__(self, b):
        """Funcion que toma como parametro una matriz y un numero entero, y devuelve una matriz con sus elementos sumados al numero entero"""
        new_elems = []
        if (isinstance(b, int)) :
            for i in self.elems : 
                new_elems.append(i+b)
                salida = myarray(new_elems, self.r, self.c, self.by_row)
                
        elif (isinstance(b, type (self))) : 
              for i in range(len(self.elems)) : 
                  new_elems.append(self.elems[i]+ b.elems[i])
                  salida = myarray(new_elems, self.r, self.c, self.by_row) 
                  
        else :
            print("El parametro de entrada es de tipo ", str(type(b)))
            salida = None
        return salida 
                      
    
    def __radd__(self, b):
        """Funcion que toma como parametro un numero entero y una matriz, y devuelve una matriz con sus elementos sumados al numero entero"""
        return self.__add__(b)
    
    def __sub__(self, b):
        """Funcion que toma como parametro una matriz y un numero entero, y devuelve una matriz con sus elementos restados al numero entero"""
        new_elems = []
        if (isinstance(b, int)) : 
            for i in self.elems : 
                new_elems.append(i-b)
                salida = myarray(new_elems, self.r, self.c, self.by_row) 
                
        elif (isinstance(b, type (self))) : 
              for i in range(len(self.elems)) : 
                  new_elems.append(self.elems[i]-b.elems[i])
                  salida = myarray(new_elems, self.r, self.c, self.by_row) 
                  
        else :
            print("El parametro de entrada es de tipo ", str(type(b)))
            salida = None
        return salida 
    
    def __rsub__(self, b):
        """Funcion que toma como parametro un numero entero y una matriz, y devuelve una matriz con sus elementos restados al numero entero"""
        return self.__sub__(b)
    
    def __pow__(self,b) :
        """Funcion que toma como parametro una matriz y un numero entero, y devuelve una matriz con sus elementos elevados al numero entero"""
        matriz = myarray(self.elems, self.r, self.c, self.by_row)
        matriz_2 = myarray(self.elems, self.r, self.c, self.by_row)
        if b == 0 :
            salida = 1
        
        elif b == 1 : 
            salida = matriz
        
        
        elif(isinstance(b, int)) :
            for i in range (b-1) : 
                mult = matriz@matriz_2 
                matriz_2 = myarray(mult, self.r, self.c, self.by_row)
            salida = mult
             
        else :
                print("El parametro de entrada es de tipo ", str(type(b)))
                salida = None
        return salida
    
    def __rpow__(self,b) :
         """Funcion que toma como parametro un numero entero y una matriz , y devuelve una matriz con sus elementos elevados al numero entero"""
         return self.__pow__(b)
    
    def __mul__(self, b) :
        """Funcion que toma como parametro una matriz y un numero entero, y devuelve una matriz con sus elementos multiplicados al numero entero"""
        new_elems = []
        if(isinstance(b, int)) :
            for i in self.elems : 
                new_elems.append(i*b)
                salida = myarray(new_elems, self.r, self.c, self.by_row) 
            
        else :
             print("El parametro de entrada es de tipo ", str(type(b)))
             salida = None
        return  salida 
    
    
    def __rmul__(self, b) :
        """Funcion que toma como parametro un numero entero y una matriz, y devuelve una matriz con sus elementos multiplicados al numero entero"""
        return self.__mul__(b)
      
            
    def __matmul__ (self, b): 
        """"Funcion que toma como parametro dos matrices, en las cuales deben coincidr el numero de filas de una con el de las columnas de la otra. 
        La funcion devuelve una matriz nueva a partir de la multiplicacion de dichas matrices"""
        new_elems = []
        if self.r == b.c or self.c == b.r : 
            for i in range(self.r):
                row = self.get_row(i)
                for e in range(b.c) : 
                    col = b.get_col(e)
                    elems = 0
                    for k in range(self.c) : 
                        elems += row[k] * col[k]
                    new_elems.append(elems)
            salida = myarray(new_elems, self.r, b.c, self.by_row)
                    
        elif self.r != b.c : 
              print ("No se puede multiplicar dichas matrices")  
              salida = None
        
        return salida
    
    def swap_row_identity(self,j ,k ) : 
        """"Funcion que toma como parametro una matriz y dos numeros de fila de la misma, y devuelve dichas filas intercambiadas de lugar"""
        identidad = I(self.r, self.r, self.by_row)
        n_identidad = identidad.swap_rows(j, k).elems
        matriz_i = myarray(n_identidad, self.r, self.r, self.by_row)
        matriz = myarray(self.elems, self.r, self.c, self.by_row) 
        new = matriz_i @ matriz
                
        return new
    
    def swap_col_identity(self,l ,m ) : 
        """"Funcion que toma como parametro una matriz y dos numeros de columnas de la misma, y devuelve dichas columnas intercambiadas de lugar"""
        identidad = I(self.c, self.c, self.by_row)
        n_identidad = identidad.swap_cols(l, m).elems
        matriz_i = myarray(n_identidad, self.c, self.c,self.by_row )
        matriz = myarray(self.elems, self.r, self.c, self.by_row) 
        new = matriz @ matriz_i
                
        return new
    
    def del_row_identity (self, j) : 
        """"Funcion que toma como parametro una matriz y un numero de fila, y devuelve la matriz sin dicha fila"""
        identidad = I(self.r, self.r, self.by_row).del_col(j)
        matriz_i = myarray(identidad.elems, self.r-1 , self.r, self.by_row)
        matriz = myarray(self.elems, self.r, self.c, self.by_row) 
        new = matriz_i @ matriz
        new = [i for i in new.elems if i != 0]
        return new
    
    def del_col_identity (self, l) : 
        """"Funcion que toma como parametro una matriz y un numero de columna, y devuelve la matriz sin dicha columna"""
        identidad = I(self.c, self.c, self.by_row).del_col(l)
        matriz_i = myarray(identidad.elems, self.c, self.c-1, self.by_row)
        matriz = myarray(self.elems, self.r, self.c, self.by_row) 
        new = matriz @ matriz_i
        new = [i for i in new.elems if i != 0]
        return new
       
        

        
                        
class I(myarray):
    def __init__(self, r, c, by_row):
        self.r = r
        self.c = c
        self.by_row = by_row
        self.elems = [0] * (self.r * self.c)
        x = 0
        for i in range(self.r) :  
            for e in range(self.c) : 
                if i == e :
                    self.elems[x] = 1
                x+= 1        
        
                    
matriz = myarray([1, 2, 3, 4, 5, 6, 7, 8, 9], 3 , 3, True)

# # Get Position 
# position = matriz.get_pos(0,1)
# print ("La posicion del elemento en la lista es,  " , position)

# # Get Coordenadas
# coordenadas = matriz.get_coords(0)
# print ('Las coordenadas en la matriz de la posicion dada en la lista son, ', coordenadas)

# # Get Row
# row = matriz.get_row(0)
# print ('Los elementos de la fila dada son, ', row)

# # Get Column 
# col = matriz.get_col(0)
# print ('Los elementos de la columna dada son, ', col)

# # Get Element
# element = matriz.get_elem((0,1))
# print ('El elemento es, ', element )

# # Delete Row 
# del_row = matriz.del_row(0).elems
# print (f'La nueva matriz es, ' , del_row)

# # Delete Column 
# del_col = matriz.del_col(0).elems
# print ('La nueva matriz es, ', del_col)

# # Swap Rows
# swap_rows = matriz.swap_rows(0,1).elems
# print ('La nueva matriz es, ', swap_rows)

# # Swap Columns
# swap_cols = matriz.swap_cols(0,1).elems
# print ('La nueva matriz es, ', swap_cols)

# # Scale Row
# scale_row = matriz.scale_row(1,2).elems
# print ('La nueva matriz es, ', scale_row)

# # Scale Column
# scale_col = matriz.scale_col(1,2).elems
# print ('La nueva matriz es, ', scale_col)

# # Transpose 
# transpose = matriz.transpose().get_row(1)
# print ('La nueva matriz es, ', transpose)

# # Flip Rows 
# flip_rows = matriz.flip_row().elems
# print ('La nueva matriz es, ', flip_rows)

# # Flip Columns
# flip_cols = matriz.flip_cols()
# print ('La nueva matriz es, ', flip_cols)

# Determinante 
det = matriz.det()






matriz_2 = myarray([6, 5, 4, 3, 2, 1], 3 , 2, True)
#matriz = myarray([1, 2, 3, 4, 5, 6, 7, 8, 9], 3 , 3 , True)
# print(matriz + 4)
# print(4 + matriz)
# print(matriz + matriz_2)
# print(matriz + "H")
# print(matriz - 4)
# print(4 - matriz)
# print(matriz - matriz_2)
# print(matriz - "H")
# print(matriz * 4)
# print(4 * matriz)
# print(matriz * "H")
# print(matriz**2)
# print(2**matriz)
# print(matriz@matriz)
# print(matriz.swap_row_identity(0,1))
# print(matriz.swap_col_identity(0,1))
# print(matriz.del_row_identity(1)) 
# print(matriz.del_col_identity(1))



