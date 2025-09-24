
BYREK_CMIMI = 120
LENG_CMIMI = 80
ZBRITJE = 0.10

def merr_input_numrik(prompt):
    while True:
        try:
            vlera = int(input(prompt))
            if vlera < 0:
                print("Ju lutem futni nje numer pozitiv.")
                continue
            return vlera
        except ValueError:
            print("Ju lutem futni nje numer të vlefshem.")

def merr_input_karte():
    while True:
        pergjigje = input("Ke karte studenti? po/jo: ").lower().strip()
        if pergjigje in ["po", "jo"]:
            return pergjigje
        print("Ju lutem përgjigjuni me 'po' ose 'jo'.")

def llogarit_nenshum(byrek, leng):
    return byrek * BYREK_CMIMI + leng * LENG_CMIMI

def apliko_zbritje(nenshum, ka_karte):
    if ka_karte == "po":
        return round(nenshum * (1 - ZBRITJE), 2), "10%"
    return nenshum, "0%"

def printo_fature(nenshum, zbritje_txt, total):

    print(f"Nën-totali: {nenshum} Lek")
    print(f"Zbritja: {zbritje_txt}")
    print(f"Totali për pagese: {total:.2f} Lek")


byrek = merr_input_numrik("Sasia e byrekve: ")
leng = merr_input_numrik("Sasia e lengjeve: ")
ka_karte = merr_input_karte()

nenshum = llogarit_nenshum(byrek, leng)
total, zbritje_txt = apliko_zbritje(nenshum, ka_karte)

printo_fature(nenshum, zbritje_txt, total)

