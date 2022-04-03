from typing_extensions import Self
import numpy as np
import numpy

class ModeloSimplex():
    funcion_objetivo = np.array(float)
    n_variables = int
    n_restriccion = int
    restriccion = np.zeros(shape = (n_variables,n_restriccion))
    max = True
    """
    Esto es solo un maquetado del la case ModeloSimplex 

    Los métodos con return 0 modifican al objeto por lo 
    que la función final ya no debe retornar nada """

    def simplex_max():
        resultado = [[],[]]
        return resultado
    def simplex_min():
        resultado = [[],[]]
        return resultado
    def tableau_max(self):
        funcion_objetivo = numpy.multiply(funcion_objetivo,─1)
        restriccion
        return 0
    def tableau_min(self):
        funcion_objetivo
        restriccion
        return 0
    def columna_pivote_max(self):
        resultado = int
        return resultado
    def columna_pivote_min(self):
        resultado = int
        return resultado
    def fila_pivote(self):
        resultado = float
        return resultado


    def gauss(self,pivote_fila, pivote_columna):
        # Se ubica el elemento pivote
        valor_pivote = self.restriccion[pivote_fila][pivote_columna]

        # Se divide la fila pivote entre el elemento pivote
        for i in range(self.n_variables):
            self.restriccion[pivote_fila][i] = self.restriccion[pivote_fila][i]/valor_pivote

        # Se obtiene el elemento pivote de la fila
        aux = self.funcion_objetivo[pivote_columna]

        # Fila original - pivote de la fila * fila pivote
        for i in range(self.n_variables):
            self.funcion_objetivo[i] = self.funcion_objetivo[i] - (aux * self.restriccion[pivote_fila][i])
        for i in range(self.n_variables):
            # Se obtiene el elemento pivote de la fila
            aux = self.restriccion[i][pivote_columna]

            """
            Fila original - pivote de la fila * fila pivote 
            Exceptuando la fila pivote
            """
            for j in range(self.n_restriccion):
                if i != pivote_fila:
                    self.restriccion[i][j] = self.restriccion[i][j] - (aux * self.restriccion[pivote_fila][i])


    def parada_max(self):
        resultado = bool
        return resultado
    def parada_min(self):
        resultado = bool
        return resultado
