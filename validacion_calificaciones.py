# Lista de calificaciones:
qualifications_list = []
start = True

while start:
    try:
        question = input("¿Qué desea hacer? \na. determinar estado aprobación\nb. calcular promedio \nc. contar calificaciones mayores \nd. verificar calificaciones específicas\n"
        ).lower()
        match question:
            # Determinar el estado de aprobación:
            case "a" | "determinar estado aprobacion":
                while True:
                    try:
                        qualification = int(input("Ingresar calificación (entre 0-100): "))
                        if 0 <= qualification <= 100:
                            # Si la calificación es menor a 70 entonces reprobó
                            if qualification < 70:
                                print("Reprobó")
                            else:
                                # Si es mayor a 70 aprobó
                                print("Aprobó")
                            break
                        else:
                            # Si ingresa un valor menor a 0 o mayor a 100
                            print("Ingresa un valor entre 0 y 100")
                    except (ValueError, KeyboardInterrupt):
                        print("Ingresa un valor válido")
            # Calcular el promedio de las calificaciones: 
            case "b" | "calcular promedio":
                while True:
                    try:
                        qualifications = input("Ingresa las calificaciones (entre 0-100) separadas por comas: ")
                        # Lista de calificaciones que separa con comas cada elemento dentro de la lista
                        qualifications_list = [int(quali) for quali in qualifications.split(',')]
                        if all(0 <= q <= 100 for q in qualifications_list):
                            # Operación para calcular el promedio de 
                            average = sum(qualifications_list) / len(qualifications_list)
                            print(f"El promedio es: {average:.2f}")
                            break
                        else:
                            print("Ingresa un valor válido entre 0 y 100")
                    except (ValueError, KeyboardInterrupt):
                        print("Ingresa valores válidos y separados por comas.")
            # Contar calificaciones mayores:
            case "c" | "contar calificaciones mayores":
                while True:
                    try:  
                        if all(0 <= q <= 100 for q in qualifications_list):
                            qualification = float(input("Ingresa la calificacion que quieres comprobar: "))
                            mayores = [q for q in qualifications_list if q > qualification]
                            # leng: tamaño de la lista de números mayores de qualification
                            leng = len(mayores)
                            if leng > 1:
                                #Si hay calificaciones mayores:
                                print(f"Hay {len(mayores)} valores mayores que {qualification} y son: {mayores}")
                                break
                            else:
                                # Si no hay calificaciones mayores
                                print(f"No hay calificaciones mayores a {qualification}")
                                break
                        else:
                            print("Ingresa un valor válido entre 0 y 100")
                    except (ValueError, KeyboardInterrupt):
                        print("Ingresa valores válidos.")
            # Verificar y contar calificaciones específicas
            case "d" | "verificar calificaciones especificas":
                while True:
                    try: 
                        qualification = float(input("Ingresa la calificacion que quieres comprobar: "))
                        # search: busca en la lista de calificaciones y cuenta la calificación específica que se está buscando
                        search = qualifications_list.count(qualification)
                        if all(0 <= q <= 100 for q in qualifications_list):
                            if search < 1:
                                print("Esta nota no existe")
                                break                                            
                            elif search == 1:
                                print(f"La nota {qualification} no se repite")
                                break
                            elif search > 1:
                                print(f'Hay {search} valores de: {qualification}')
                                break
                        else:
                            print("Todas las calificaciones deben estar entre 0 y 100.")
                    except (ValueError, KeyboardInterrupt):
                        print("Ingresa valores válidos.")
            # Caso para cuando no reconoce una opción válida (a, b, c, o d)
            case _:
                print("Opción no reconocida. Intenta de nuevo.")
    # Excepción para el error Keyboard interrupt
    except KeyboardInterrupt:
        print("Ocurrió un error inesperado:" )
        
    # el usuario ingresa si quiere intentar una nueva opción (s) o no (n)
    choose = input("¿Deseas intentar una nueva opción? (si/no): ").lower()
    if choose == "n" or choose == "no":
        print("Fue un placer ayudarte, espero que hayas aprobado <3")
        break
