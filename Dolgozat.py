szoveg = "Ha itt a nyár, ugye komám, a szív a víznek szalutálés vígan lépked, akár a tornászígy megy a nagy ho-ho-ho horgász. Bátran rikkant, puhányok ho-ho-ho-ho-ho,megint csak ho-ho-ho-ho. Van itt csali és egy két horog, az eszem pedig jól forog, cselt a cselre kiválón sorjáz, ravasz a nagy ho-ho-ho horgász. Városbéli puhányok, nyavalyások ha gyötör a láz,fületek nyissátok gyorsan, hallgassátok,amit most néktek, hallgassátok, amit most néktek eldalol a ho-ho-ho nagy horgász.Ha itt a nyár, ugye komám, a szív a víznek szalutál,és vígan lépked, akár a tornász így megy a nagy ho-ho-ho horgász.Bátran rikkant, puhányok ho-ho-ho-ho-ho,megint csak ho-ho-ho-ho.Van itt csali és egy két horog,az eszem pedig jól forog,cselt a cselre kiválón sorjáz,ravasz a nagy ho-ho-ho horgász. Városbéli puhányok, nyavalyások ha gyötör a láz,fületek nyissátok gyorsan, hallgassátok, űamit most néktek, hallgassátok,amit most néktek eldalol a ho-ho-ho nagy horgász."

#1.feladat
print(len(szoveg))

#2.feladat
print("Ennyiszer található meg a szövegben a horgász szó: ", szoveg.count('horgász'))

#3.feladat
ujszoveg=szoveg.replace("ho-ho-ho", "HO-HO-HO")
print(ujszoveg)

#4.feladat
Lszam = []
Lbetu = []

for b in szoveg:
    if (b.isalpha()):
        Lbetu.append(b)
    elif (b.isalnum()):
        Lszam.append(int(b))

print("Jelenleg nincs szám a szöveg, ha szeretne látni számokat akkor írjon ",Lszam)
        
#5.feladat
Hmely = []
Hmagas = []


for h in szoveg:
    if (h in "e" and "é" and "i" and "í" and "ö" and "ő" and "ü" and "ű"):
        Hmely.append(h)
    elif (h in  "a" and "á" and "o" and "ó" and "u" and "ú"):
        Hmagas.append(h)
        
print("Ennyi db mély magánhangzó található:  ",len(Hmely))
print("Ennyi db magas magánhangzó található:  ",len(Hmagas))
