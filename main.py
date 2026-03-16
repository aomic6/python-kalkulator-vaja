def sestej(a, b): return a + b
def odstej(a, b): return a - b
def pomnozi(a, b): return a * b
def deli(a, b):
    if b == 0: return "Napaka: Deljenje z 0 ni dovoljeno!"
    return a / b

zgodovina = []

while True:
    print("\n--- MINI KALKULATOR (Končna verzija) ---")
    print("1: + | 2: - | 3: * | 4: / | 0: Izhod")
    izbira = input("Izbira: ")

    if izbira == "0":
        print("Nasvidenje!")
        break

    if izbira in ["1", "2", "3", "4"]:
        x = float(input("Prvo stevilo: "))
        y = float(input("Drugo stevilo: "))

        if izbira == "1":
            res = sestej(x, y)
            izpis = f"{x} + {y} = {res}"
        elif izbira == "2":
            res = odstej(x, y)
            izpis = f"{x} - {y} = {res}"
        elif izbira == "3":
            res = pomnozi(x, y)
            izpis = f"{x} * {y} = {res}"
        elif izbira == "4":
            res = deli(x, y)
            izpis = f"{x} / {y} = {res}"

        print(f"==> REZULTAT: {izpis}")
        zgodovina.append(izpis)
        
        # Prikaz zgodovine (zadnji 3 elementi)
        print(f"Zgodovina (zadnji 3): {zgodovina[-3:]}")
    else:
        print("Neveljavna izbira.")