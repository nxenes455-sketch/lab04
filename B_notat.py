diametri = int(input("Jep diametrin e picës (cm): "))
cmimi = int(input("Jep çmimin bazë (Lek): "))

if diametri >= 30:
    cmimi = cmimi + cmimi * 0.10

print("Çmimi final:", int(cmimi), "Lek")
