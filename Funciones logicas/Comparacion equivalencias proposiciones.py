# Script, en paradigma estructurado con elementos de POO, pensado para comparar 
# y verificar los ejercicios de simplificacion
# de proposiciones logicas de la unidad 1
# mediante el uso de la tabla de verdad.

#Limpia la consola al iniciar
import os
os.system('clear')

class Operation:

    #La funcion tiene que estar preseteada 
    def calculate(self,p,q,r):
        result=bool(False)
        
        #Proposicion original
        #result=    
        return result

    def calculateToComparate(self,p,q,r):
        result=bool(False)
        
        #Proposicion simplificada propuesta
        #result =         

        return result

def print_table(option) :
    operation=Operation()

    if ( option == 2 ):
        print( "  P || Q || f(p,q) || Funcion propuesta " )
        print(" ======================================== ")
        print ("  F |  F  |   " +"     "+ str( operation.calculate(False,False,None) ) +"     "+ str( operation.calculateToComparate(False,False,None) ) )
        print ("  F |  V  |   " +"     "+ str( operation.calculate(False,True,None) )  +"     "+ str( operation.calculateToComparate(False,True,None) ) )
        print ("  V |  F  |   " +"     "+ str( operation.calculate(True,False,None) )  +"     "+ str( operation.calculateToComparate(True,False,None) ) )
        print ("  V |  F  |   " +"     "+ str( operation.calculate(True,False,None) )  +"     "+ str( operation.calculateToComparate(True,False,None) ) )
        print ("  V |  V  |   " +"     "+ str( operation.calculate(True,True,None) )   +"     "+ str( operation.calculateToComparate(True,True,None) ) )

    elif( option == 3 ):

        print( "  P || Q || R || f(p,q) || Funcion propuesta " )
        print(" ============================================= ")
        print ("  F |  F  | F " +"     "+ str( operation.calculate(False,False,False) )+"     "+ str( operation.calculateToComparate(False,False,False) ) )
        print ("  F |  F  | V " +"     "+ str( operation.calculate(False,False,True) ) +"     "+ str( operation.calculateToComparate(False,False,True) ) )
        print ("  F |  V  | F " +"     "+ str( operation.calculate(False,True,False) ) +"     "+ str( operation.calculateToComparate(False,True,False) ) )
        print ("  F |  V  | V " +"     "+ str( operation.calculate(False,True,True) )  +"     "+ str( operation.calculateToComparate(False,True,True) ) )
        print ("  V |  F  | F " +"     "+ str( operation.calculate(True,False,False) ) +"     "+ str( operation.calculateToComparate(True,False,False) ) )
        print ("  V |  F  | V " +"     "+ str( operation.calculate(True,False,True) )  +"     "+ str( operation.calculateToComparate(True,False,True) ) )
        print ("  V |  V  | F " +"     "+ str( operation.calculate(True,True,False) )  +"     "+ str( operation.calculateToComparate(True,True,False) ) )
        print ("  V |  V  | V " +"     "+ str( operation.calculate(True,True,True) )   +"     "+ str( operation.calculateToComparate(True,True,True) ) )
        
    else:
        print("Aun no se programaron proposiciones con esa cantidad de variables")

    print ("\n")

#--------------------------------------------------------------------------------------------------------#

#Comienzo de la ejecucion
option=int(input("Ingrese la cantidad de variables que tiene la proposicion a evaluar: "))
print_table(option)

print("Finalizando script...")
