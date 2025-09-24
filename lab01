
import sys
import platform

print("OK - Python u instalua!")
print("Version:", sys.version)
print("Interpreter:", sys.executable)
print("OS:", platform.system(), platform.release())
print("-" * 40)

emri = input("Shkruaj emrin: ")
print(f"Pershendetje, {emri}! Python gati per pune.")
print("-" * 40)

a_txt = input("Jep numrin A: ")
b_txt = input("Jep numrin B: ")

if not (a_txt.lstrip("-").isdigit() and b_txt.lstrip("-").isdigit()):
    print("Gabim: te dhenat duhet te jene numra te plote (p.sh. 7, -3).")
    raise SystemExit(1)

a = int(a_txt)
b = int(b_txt)

print("Shuma:", a + b)
print("Produkti:", a * b)
print("-" * 40)

