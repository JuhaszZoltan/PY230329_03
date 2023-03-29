from module import *
versenyzok:list[Versenyzo] = []
file = open(file='Eredmenyek.txt', mode='r', encoding='ANSI')
for s in file: versenyzok.append(Versenyzo(s))

print(f'versenyt befejezők száma: {len(versenyzok)}')

ejsz:int = 0
for v in versenyzok:
    if v.kategoria == 'elit junior':
        ejsz += 1
print(f'elit junior indulók száma: {ejsz}')

eko:int = 0
for v in versenyzok:
    eko += (2014 - v.szul_ev)
aek:float = round(eko / len(versenyzok), 1)
print(f'átlagéletkor: {aek}')

kk:str = input('írj be egy kategóriát: ')
rajtszamok:list[int] = []
for v in versenyzok:
    if v.kategoria == kk:
        rajtszamok.append(v.rajtszam)
if len(rajtszamok) == 0:
    print('\tnincs ilyen kategória!')
else:
    print('\trajtszámok:', end=' ')
    for r in rajtszamok:
        print(r, end=' ')
    print(end='\n')

nok:list[Versenyzo] = []
for v in versenyzok:
    if not v.nem:
        nok.append(v)
mini:int = 0
for i in range(1, len(nok)):
    if nok[i].ossz_mp < nok[mini].ossz_mp:
        mini = i
print(f'győztes a nők között: {nok[mini].nev}')
