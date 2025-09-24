emri = "noel"  
print(f"Përshëndetje, {emri}!")

vitlindja = 2025 - 12 
mosha = 2025 - vitlindja

if mosha < 0:
    print("Vit i pavlefshëm")
else:
    print(f"Je {mosha} vjeç.")

diametri = 30 
cmimi_baze = 80  

if diametri >= 30:
    cmimi_final = cmimi_baze * 1.10
else:
    cmimi_final = cmimi_baze

print(f"Çmimi final: {round(cmimi_final)} Lek")

piket = 80  # Default value

if piket > 100 or piket < 0:
    print("Vlerë e pavlefshme")
elif piket >= 90:    
    print("Shkëlqyeshëm")
elif piket >= 75:
    print("Shumë mirë")
elif piket >= 60:
    print("Mirë")
elif piket >= 40:
    print("Mjaftueshëm")
else:
    print("Dobët")

numri = 12  

if numri % 2 == 0:
    print("Çift")
else:
    print("Tek")

cmimi = 80.0 
sasia = 12

if sasia < 0:
    print("Sasia e pavlefshme")
else:
    karta = "po" 
    nentotal = cmimi * sasia

    if karta == "po":
        zbritja = nentotal * 0.10
    else:
        zbritja = 0

    tvsh = (nentotal - zbritja) * 0.15
    total = nentotal - zbritja + tvsh

    print("------------------------------")
    print(f"Nën-total: {format(nentotal, '.2f')} Lek")
    print(f"Zbritja: 10% (Vlera: {format(zbritja, '.2f')} Lek)")
    print(f"TVSH (15%): {format(tvsh, '.2f')} Lek")
    print(f"Totali për pagesë: {format(total, '.2f')} Lek")

    if total >= 1000:
        print("Kupon fiskal: PO")
    else:
        print("Kupon fiskal: JO")
