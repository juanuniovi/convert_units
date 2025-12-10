def metros_a_km(m):
    return m / 1000

def km_a_metros(km):
    return km * 1000

if __name__ == "__main__":
    print("Conversor de unidades")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Metros")
    opcion = input("Elige opción (1/2): ")

    if opcion == "1":
        m = float(input("Introduce metros: "))
        print(f"{m} metros son {metros_a_km(m)} km")
    elif opcion == "2":
        km = float(input("Introduce km: "))
        print(f"{km} km son {km_a_metros(km)} metros")
    else:
        print("Opción no válida")

# quiero que saque por pantalla el valor en ambas unidades:
    if opcion == "1":
        m = float(input("Introduce metros: "))
        km = metros_a_km(m)
        print(f"{m} metros son {km} km")
        print(f"{km} km son {km_a_metros(km)} metros")
    elif opcion == "2":
        km = float(input("Introduce km: "))
        m = km_a_metros(km)
        print(f"{km} km son {m} metros")
        print(f"{m} metros son {metros_a_km(m)} km")    




