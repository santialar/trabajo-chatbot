def Taller_mecanico():
    print("---------Bienvenido al Taller Mecánico----------")

    arrancado = input("¿El auto arranca? (si/no): ").strip().lower()
    print("------------------------------------------------------")
    luces = input("¿Las luces del tablero funcionan? (si/no): ").strip().lower()
    print("------------------------------------------------------")
    apagado = input("¿El auto se apaga al acelerar? (si/no): ").strip().lower()
    print("------------------------------------------------------")
    humow = input("¿Sale humo blanco del escape? (si/no): ").strip().lower()
    print("------------------------------------------------------")
    humob = input("¿Sale humo negro del escape? (si/no): ").strip().lower()

    if arrancado == 'no' and luces == 'no':
        print("Posible causa: batería descargada.")
    elif arrancado == 'no' and luces == 'si':
        print("Posible causa: motor de arranque dañado.")
    elif arrancado == 'si' and apagado == 'si':
        print("Posible causa: problema en el suministro de combustible.")
    elif humob == 'si':
        print("Posible causa: mezcla rica de combustible.")
    elif humow == 'si':
        print("Posible causa: falla en la junta de culata.")
    else:
        print("No hay una posible causa, contáctese con un asesor")

if __name__ == "__main__":
    Taller_mecanico()
