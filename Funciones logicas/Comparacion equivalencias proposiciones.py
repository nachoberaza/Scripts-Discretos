# Script, en paradigma estructurado,pensado para comparar 
# y verificar los ejercicios de simplificacion
# de proposiciones logicas de la unidad 1
# mediante el uso de la tabla de verdad.

#Limpia la consola al iniciar
import os
os.system('cls')

# ------ Proposiciones de 2 variables ------ #

#La proposicion original presteada 
def calculate(p,q):
    result=bool(False)
    
    #Proposiciones original
    #result=
        
    return result

#La proposicion a la que se quiere comparar preseteada
def calculateToComparate(p,q):
    result=bool(False)
    
    #Proposicion original
    #result = 
        
    return result

# ------ ************************ ------#

# ------ Proposiciones de 3 variables ------ #

#La funcion tiene que estar preseteada 
def calculate(p,q,r):
    result=bool(False)
    
    #Proposicion original
    #result=    
    return result

def calculateToComparate(p,q,r):
    result=bool(False)
    
    #Proposicion simplificada propuesta
    #result =         
    return result

# ------ ************************ ------#

def print_table(option) :

    if ( option == 2 ):
        print( "  P || Q || f(p,q) || Funcion propuesta " )
        print(" ======================================== ")
        print ("  F |  F  |   " +"     "+ str( calculate(False,False) ) +"     "+ str( calculateToComparate(False,False) ) )
        print ("  F |  V  |   " +"     "+ str( calculate(False,True) )  +"     "+ str( calculateToComparate(False,True) ) )
        print ("  V |  F  |   " +"     "+ str( calculate(True,False) )  +"     "+ str( calculateToComparate(True,False) ) )
        print ("  V |  V  |   " +"     "+ str( calculate(True,True) )   +"     "+ str( calculateToComparate(True,True) ) )

    elif( option == 3 ):

        print( "  P || Q || R || f(p,q) || Funcion propuesta " )
        print(" ============================================= ")
        print ("  F |  F  | F " +"     "+ str( calculate(False,False,False) )+"     "+ str( calculateToComparate(False,False,False) ) )
        print ("  F |  F  | V " +"     "+ str( calculate(False,False,True) ) +"     "+ str( calculateToComparate(False,False,True) ) )
        print ("  F |  V  | F " +"     "+ str( calculate(False,True,False) ) +"     "+ str( calculateToComparate(False,True,False) ) )
        print ("  F |  V  | V " +"     "+ str( calculate(False,True,True) )  +"     "+ str( calculateToComparate(False,True,True) ) )
        print ("  V |  F  | F " +"     "+ str( calculate(True,False,False) ) +"     "+ str( calculateToComparate(True,False,False) ) )
        print ("  V |  F  | V " +"     "+ str( calculate(True,False,True) )  +"     "+ str( calculateToComparate(True,False,True) ) )
        print ("  V |  V  | F " +"     "+ str( calculate(True,True,False) )  +"     "+ str( calculateToComparate(True,True,False) ) )
        print ("  V |  V  | V " +"     "+ str( calculate(True,True,True) )   +"     "+ str( calculateToComparate(True,True,True) ) )
        
    else:
        print("Aun no se programaron proposiciones con esa cantidad de variables")

    print ("\n")

#--------------------------------------------------------------------------------------------------------#

#Comienzo de la ejecucion
option=int(input("Ingrese la cantidad de variables que tiene la proposicion a evaluar: "))
print_table(option)

print("Finalizando script...")
