#desarrollo actividad para evaluacion n°2 30%

#1 voy a importar os y time 
import time, os

#2 crear el menu (cabecera y cuerpo)

#espacio para crear banderas (Boolean)
banderaMenu = True
banderaRut = True
banderaEdad = True
while banderaMenu:
    os.system("cls")
    print("\tCentro Medico DUOC")
    print("1) Registrar Paciente")
    print("2) Atencion Paciente")
    print("3) Consultar Datos Paciente")
    print("4) Salir")
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion == 1:
            os.system("cls")
            print("Registrar Paciente")
            while banderaRut:
                try:
                    rut = int(input("ingrese rut\n"))
                    while rut < 5000000 or rut > 99999999:
                        rut = int(input("ingrese rut, debe estar en el rango 5000000 y 99999999\n"))
                    banderaRut = False    
                except:
                    print("para el campo rut, ese dato es invalido")
            nombre = input("ingrese su nombre\n")
            while nombre == "":
                nombre = input("ingrese su nombre, no debe venir vacio\n")
            direccion = input("ingrese su direccion\n")
            while direccion == "":
                direccion = input("ingrese su direccion, no debe venir vacio\n")
            while banderaEdad:
                try:
                    edad = int(input("ingrese edad\n"))
                    while edad < 0 or edad > 110:
                        edad = int(input("ingrese edad, debe estar en rango 0 y 110\n"))
                    banderaEdad = False
                except:
                    print("para el campo edad, el dato ingresado no es valido")
            sexo = input("ingrese sexo\n")
            while sexo != "m" and sexo != "M" and sexo != "f" and sexo != "F":
                sexo = input("ingrese sexo, recuerde que solo acepta f o m\n")
            ps = input("ingrese prevision de salud\n")
            while ps != "fonasa" and ps != "isapre":
                ps = input("ingrese prevision de salud, recuerde que las opciones son isapre o fonasa\n")
            correo = input("ingrese correo\n")
            while '@' not in correo:
                correo = input("ingrese correo, recuerde que debe ingresar un @\n")
        elif opcion == 2:
            os.system("cls")
            print("Atencion Paciente")
            rutPaciente = int(input("ingrese paciente"))
            if rutPaciente == rut:
                fecha = input("ingres fecha dd/mm/aaaa\n")
                registro = input("indique el motivo de la consulta\n")
        elif opcion == 3:
            os.system("cls")
            print("Consultar Datos Paciente")
            rutPaciente = int(input("ingrese paciente"))
            if rutPaciente == rut:
                print(f"RUT: {rut}")
                print(f"NOMBRE: {nombre}")
                print(f"DIRECCION: {direccion}")
                print(f"CORREO: {correo}")
                print(f"PREV SALUD: {ps}")
                print(f"EDAD: {edad}")
                print(f"FECHA: {fecha}")
                print(f"REGISTRO: {registro}")
                enter = input("pulse enter para continuar...")
        elif opcion == 4:
            os.system("cls")
            print("Ha salido del sistema…")
            banderaMenu = False
    except:
        print("opcion ingresada no existe")
        time.sleep(2)