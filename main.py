def sestej(a, b): return a + b
def odstej(a, b): return a - b
def pomnozi(a, b): return a * b
def deli(a, b):
    if b == 0: return "Napaka: Deljenje z 0 ni dovoljeno!"
    return a / b

while True:
    print("\n--- MINI KALKULATOR ---")
    print("1: Sestevanje | 2: Odstevanje | 3: Mnozenje | 4: Deljenje | 0: Izhod")
    izbira = input("Vnesi izbiro (0-4): ")

    if izbira == "0":
        print("Zapiranje programa... Nasvidenje!")
        break

    if izbira in ["1", "2", "3", "4"]:
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))

        if izbira == "1":
            print(f"==> IZRACUN: {x} + {y} = {sestej(x, y)}")
        elif izbira == "2":
            print(f"==> IZRACUN: {x} - {y} = {odstej(x, y)}")
        elif izbira == "3":
            print(f"==> IZRACUN: {x} * {y} = {pomnozi(x, y)}")
        elif izbira == "4":
            print(f"==> IZRACUN: {x} / {y} = {deli(x, y)}")
    else:
        print("Neveljavna izbira, poskusi ponovno.")