import os
import time

autos = []
tipos_auto = ['sedan','deportivo','pickup','city car','SUV']

while True:
    os.system('cls')
    print("REGISTRO DE AUTOS")
    print("1. Agregar auto")
    print("2. Ver autos")
    print("3. Actualizar auto")
    print("4. Eliminar auto")
    print("5. Salir")
    while True:
        try:    
            opc = int(input("Ingrese opción: "))
            if opc in (1, 2, 3, 4, 5):
                break
            else:
                print("ERROR, opción debe ser (1, 2, 3, 4, 5)!")
        except:
            print("ERROR, debe ingresar opción en números enteros")

    if opc == 1:
        print("AGREGAR AUTO")
        while True:
            patente = input("Ingrese patente: ")
            if len(patente)  ==6:
                print("Patente guardada con éxito!")
                time.sleep(2)
                break
            else:
                print("ERROR, la patente ingresada debe tener 6 caracteres")
                time.sleep(2)
        os.system("cls")
        while True:
            marca = input("Ingrese marca: ")
            if len(marca)>=2 and len(marca)<=10:
                print("Marca del auto guardado!")
                time.sleep(2)
                break
            else:
                print("Error, marca de auto no disponible!") 
                time.sleep(2)   


        while True:
            modelo = input("Ingrese modelo: ")
            if len(modelo)>=2 and len(modelo)<=14:
                print("Modelo del auto guarado con exitó")
                time.sleep(2)
                break
            else:
                print("Error, modelo de auto no encontrado")
        while True:    
            try:
                tipo_del_auto = int(input("Ingrese tipo de auto (1: sedan  2: deportivo  3: pickup  4: city car  5: SUV): "))
                if tipo_del_auto in range(1, len(tipos_auto)+1):
                    print("Tipo de auto ingresado con éxito!")
                    time.sleep(2)
                    break
                else:
                    print("ERROR, debe ingresar un tipo de auto de la lista")
                    time.sleep(2)
            except:
                print("ERROR, debe ingresar el valor que quiere en números enteros")
                time.sleep(2)
       

        auto = {
            "patente": patente,
            "marca": marca,
            "modelo": modelo,
            "tipo_auto": tipos_auto[tipo_del_auto-1]
        }
        autos.append(auto)
        print("AUTO AGREGADO!")

    elif opc == 2:
        for auto in autos:
            print(auto) 
    
        time.sleep(3)

    elif opc == 3:
        print("ACTUALIZAR AUTO")
        print("Patentes de autos actuales: ", [auto["patente"] for auto in autos])
        while True:
            try:
                patente_buscar = input("Ingrese patente del auto que desea cambiar la patente actual: ")
                for auto in autos:
                    if patente_buscar == auto["patente"]:
                        while True:
                            modelo_nuevo = input("Ingrese nueva patente: ")
                            if len(modelo_nuevo)==6:
                                auto["modelo"] = modelo_nuevo
                                print("AUTO ACTUALIZADO!")
                                time.sleep(2)
                                break
                            else:
                                print("ERROR, la patente debe contener 6 digitos")
                                time.sleep(1)
                        
                else:
                    print("No se ha encontrado ningún auto con la patente ingresada.")
                break
            except:
                print("ERROR, debe ingresar la patente del auto que desea actualizar correctamente")
    elif opc == 4:
        os.system('cls')
        print("ELIMINAR AUTO")
        if autos:
            print("Patentes de autos actuales: ", [auto["patente"] for auto in autos])
            patente_eliminar = input("Ingrese patente del auto a eliminar: ")
            for auto in autos:
                if patente_eliminar == auto["patente"]:
                    autos.remove(auto)
                    print("AUTO ELIMINADO!")
                    break
            else:
                print("No se ha encontrado ningún auto con la patente ingresada")
        else:
            print("No hay autos registrados.")
            break
        time.sleep(2)
    else:
        print("ADIOS!")
        break
    time.sleep(2)
