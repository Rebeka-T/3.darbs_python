"""
Ir uzrakstīta programma Python, izmantojot funkciju.
Summējot divus norādītos veselos skaitļus. 
Tomēr, ja summa ir no 15 līdz 20, tā atgriezīs 20.

"""
def spec_summa(a,b): # a un b ir parametri
    kopa=a+b 
    if 15<= kopa<=20:
        return 20
    else:
        return kopa
# piemērs 
sk1=int(input("ievadi 1. skaitli"))
sk2=int(input("ievadi 2. skaitli"))

rezultats=spec_summa(sk1, sk2) # jānorāda 2 argumenti

print(f"rezultāts ir: {rezultats}")