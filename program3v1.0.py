# !/usr/bin/python 
# -*- coding: UTF-8 -*-
#################################################################################
# Nombre del programa:  program3_v1.0                                           #  
# Correo Electronico:   afarable-1997@hotmail.com                               #
# Fecha:                23/03/2018                                              #
# Descripción:          Programa encargado de realizar calcular los parametros  #
#                       de regresion lineal y el coheficiente de coorelacion de #
#                       un conjunto par de numeros                              #
#################################################################################

__author__ = 'Danny Rojas Reyes'
__version__ = 'program3_v1.0.py'

import os
from math import pow, sqrt

""" Descripción de la clase
#Nombre: Operation                                                                                       
#Descripción: se ejecutaran las distintas operaciones para llevar a 
#             cabo  los los parámetros de regresión lineal y el 
#             coeficiente de correlación    
#Constructor: Operation()
#Parámetros del constructor:  null

#Metodos: 3(sumNumber, sumForXandYsquare, productOfXwithY)
"""

class Operation:

    number_square = 0.00
    number_productXandY = 0.00

    def sumNumber(self, array):
        return sum(array);
        
    def sumForXandYsquare(self, array):
        self.number_square = 0.00
        for item in array:
            self.number_square = self.number_square + pow(item, 2)
        return self.number_square
    
    def productOfXwithY(self, arrayX, arrayY):
        for item in range(len(arrayX)):
            self.number_productXandY = self.number_productXandY + (arrayX[item] * arrayY[item])
        return self.number_productXandY


""" Descripción de la clase                                                              
#Nombre: InputData                                                                                       
#Descripción: se ejecutaran en primera instancia para instanciar la clase Operation      
#Constructor: InputData()
#Parámetros del constructor:  null

#Metodos: 1(main)
"""

class InputData():
    def main():
        operations = Operation()
        const_repeat = 0;
        
        #srcX = [130, 650,99, 150, 128, 302, 95, 945, 368, 961,]
        #srcY = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
        srcX = list()
        srcY = list()

        const_repeat = int(raw_input('¿Cuantos valores quieres ingresar? : '))

        for i in range(const_repeat):
            number = float(raw_input('(X)Escribe el dato: '))
            srcX.append(number)

        os.system('cls')

        for i in range(const_repeat):
            number = float(raw_input('(Y)Escribe el dato: '))
            srcY.append(number)

        os.system('cls')

        const_Yk = 386;

        try:
            const_x = operations.sumNumber(srcX);
            const_y = operations.sumNumber(srcY);
    
            const_Xavg = const_x / float(len(srcX))
            const_Yavg = const_y / float(len(srcY))

            const_x_square  = operations.sumForXandYsquare(srcX);
            const_y_square  = operations.sumForXandYsquare(srcY);

            const_XprodutY  = operations.productOfXwithY(srcX, srcY)

            print "******  linear regression parameters Beta0 and Beta1 | correlation coefficients R(x,y) r^2 ****"

            beta1 = ((const_XprodutY) - (len(srcX) * const_Xavg * const_Yavg)) / float(const_x_square - (len(srcX) * pow(const_Xavg,2)))
            print "Beta 1: " + str(beta1)

            numRxy = len(srcX) * const_XprodutY - (const_x * const_y)
            denomRxy = sqrt((len(srcX) * const_x_square - pow(const_x,2)) * (len(srcX) * const_y_square - pow(const_y,2)))
            Rxy = numRxy / float(denomRxy)
            print "R(x,y): " + str(Rxy)

            beta0 = const_Yavg - beta1 * const_Xavg
            print "Beta 0 :" + str(beta0)

            R_square = Rxy * Rxy
            print "R^2 :" + str(R_square)

            Yk = beta0 + beta1 * const_Yk
            print "Yk :" + str(Yk)
        except ZeroDivisionError:
            print "has occurred a error, Try again... "

    if __name__ == '__main__':
        os.system('cls')
        main()