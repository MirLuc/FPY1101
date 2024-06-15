#instalar githun desktop en pc personal
import os

# Definición de la colección de cargos
cargos_disponibles = ["CEO", "Desarrollador", "Analista de datos"]

# Función para registrar un trabajador
def registrar_trabajador():
    print("\nRegistro de Trabajador")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = input(f"Cargo ({', '.join(cargos_disponibles)}): ")
    while cargo not in cargos_disponibles:
        print(f"Cargo no válido. Los cargos disponibles son: {', '.join(cargos_disponibles)}")
        cargo = input("Cargo: ")
    sueldo_bruto = float(input("Sueldo Bruto: "))
    desc_salud = sueldo_bruto * 0.07  # Descuento salud (7%)
    desc_afp = sueldo_bruto * 0.12    # Descuento AFP (12%)
    liquido_pagar = sueldo_bruto - desc_salud - desc_afp
    
    # Mostrar los resultados
    print("\nResumen del Trabajador Registrado:")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Cargo:", cargo)
    print("Sueldo Bruto:", sueldo_bruto)
    print("Descuento Salud (7%):", desc_salud)
    print("Descuento AFP (12%):", desc_afp)
    print("Líquido a Pagar:", liquido_pagar)
    
    # Retornar los datos como una tupla
    return (nombre, apellido, cargo, sueldo_bruto, desc_salud, desc_afp, liquido_pagar)

# Función para listar todos los trabajadores
def listar_trabajadores(trabajadores):
    print("\nLista de Trabajadores:")
    if not trabajadores:
        print("No hay trabajadores registrados.")
    else:
        for idx, trabajador in enumerate(trabajadores, start=1):
            print(f"Trabajador {idx}:")
            print("Nombre:", trabajador[0])
            print("Apellido:", trabajador[1])
            print("Cargo:", trabajador[2])
            print("Sueldo Bruto:", trabajador[3])
            print("Descuento Salud (7%):", trabajador[4])
            print("Descuento AFP (12%):", trabajador[5])
            print("Líquido a Pagar:", trabajador[6])
            print()

# Función para imprimir planilla de sueldos en un archivo de texto
def imprimir_planilla(trabajadores):
    print("\nImprimir Planilla de Sueldos")
    if not trabajadores:
        print("No hay trabajadores registrados para imprimir la planilla.")
        return
    
    cargo_seleccionado = input(f"Seleccione un cargo ({', '.join(cargos_disponibles)}) o escriba 'todos' para imprimir todos: ")
    if cargo_seleccionado.lower() == 'todos':
        archivo_nombre = "planilla_todos.txt"
    elif cargo_seleccionado in cargos_disponibles:
        archivo_nombre = f"planilla_{cargo_seleccionado}.txt"
    else:
        print("Cargo no válido.")
        return
    
    with open(archivo_nombre, 'w') as archivo:
        archivo.write("Planilla de Sueldos\n\n")
        for trabajador in trabajadores:
            if cargo_seleccionado.lower() == 'todos' or trabajador[2] == cargo_seleccionado:
                archivo.write(f"Nombre: {trabajador[0]}\n")
                archivo.write(f"Apellido: {trabajador[1]}\n")
                archivo.write(f"Cargo: {trabajador[2]}\n")
                archivo.write(f"Sueldo Bruto: {trabajador[3]}\n")
                archivo.write(f"Descuento Salud (7%): {trabajador[4]}\n")
                archivo.write(f"Descuento AFP (12%): {trabajador[5]}\n")
                archivo.write(f"Líquido a Pagar: {trabajador[6]}\n")
                archivo.write("\n")
    
    print(f"Se ha generado el archivo '{archivo_nombre}' con la planilla de sueldos.")

# Función principal del programa
def main():
    trabajadores = []
    
    while True:
        print("\nBienvenido al Sistema de Gestión de Sueldos")
        print("1. Registrar Trabajador")
        print("2. Listar Todos los Trabajadores")
        print("3. Imprimir Planilla de Sueldos")
        print("4. Salir del Programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            trabajador = registrar_trabajador()
            trabajadores.append(trabajador)
        elif opcion == '2':
            listar_trabajadores(trabajadores)
        elif opcion == '3':
            imprimir_planilla(trabajadores)
        elif opcion == '4':
            print("Gracias por utilizar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
