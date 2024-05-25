print("******* BIENVENIDO AL BURGUER KING *******")

print("Ingrese los datos para la factura electrónica")

nombreCliente = input("Ingrese su nombre: ")
numeroCedula = int(input("Ingrese su número de cédula: "))
correoElectronico = input("Ingrese su correo: ")
numeroHamburguesas = int(input("Ingrese el número de hamburguesas: "))
print("Ingrese el tipo de hamburguesa: ")
tipoHamburguesa = int(input(" 1) simple 2) doble 3) triple "))
if tipoHamburguesa == 1 or tipoHamburguesa == 2 or tipoHamburguesa == 3:
    if tipoHamburguesa == 1 :
        precio = numeroHamburguesas*1.50
    elif tipoHamburguesa == 2:
        precio = numeroHamburguesas*2.50
    elif tipoHamburguesa == 3:
        precio = numeroHamburguesas*3.25
    print("Ingrese la forma de pago")
    tipoPago = int ( input( " 1) Tarjeta 2) Efectivo " ))
    if  tipoPago == 1:
        recargo = precio *0.05
        preciofinal = precio + recargo
        print(f"Genial, {nombreCliente}, el precio final es de ${preciofinal:.2f}")
        print(f"La factura se enviará a su correo: {correoElectronico}")
    elif tipoPago == 2:
        print(f"Genial, {nombreCliente}, el precio final es de ${precio:.2f}")
        print(f"La factura se enviará a su correo: {correoElectronico}")
    else:
        print("No existe ese tipo de pago")
        print("Muchas gracias")
else :
    print("Ese tipo de hamburguesa no existe")
    print("Muchas gracias")
        
