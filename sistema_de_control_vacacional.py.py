print ("sistema de años de vacaciones rasppi")

nombre = input ("¿cual es su nombre?: ")

llave = int (input( nombre + " ¿a que llave perteneces?:\n "))

if llave == 1:
    print(nombre + " bienvenido al departamento de manofactura. \n ")

    año = int (input(nombre + "¿cuanto años solicitas?: "))

    if año == 1:
        print (nombre + " su vacaciones sera de 10 a 15 dias como minimo.")
    elif año == 2:
        print (nombre + " su vacaciones seran de 20 a 30 dias como minimo.")
    elif año == 3:
        print (nombre + " su vacaciones seran de 1 mes a 1 mes y medio. ")
    else:
        print (nombre + " lo sentimos aun no esta en cupo de vacacionar. ")

elif llave == 2:
    print( nombre+ " bienvenido al departamento de longistica.\n ")

    año_dos = int (input("¿cuanto años de vacaciones necesitas?: "))

    if año_dos == 1:
        print (nombre + " su vacaiones sera de 15 a 20 dias minimo. ")
    elif año_dos == 2:
        print (nombre + " su vacaciones seran de 20 a 30 dias minimo. ")
    elif año_dos == 3:
        print (nombre + " su vacaciones seran de 30 a 35 dias minimo.")
    else:
        print (nombre + "\n lo sentimo no esta ortorgado a las vacaciones.\n ")
else:
    print (nombre + " su departamento no se encuentra.")

print ("fin.")

    
