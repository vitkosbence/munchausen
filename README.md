# munchausen
Megoldás a Münchausen számok megkeresésének optimalizálására pythonban.
10-es számrendszer, 0^0 = 0 értelmezés, 440 millió felső határ a keresésnek.

A megoldás részletei:

-Hatványozás -> 0^0 ... 9^9 hatványok tárolása egy tömbben, későbbiekben innen való elérése.
-Int cast -> 0 ... 9 egyjegyű sztringek és int értékükből álló párok tárolása egy dictionaryban, későbbiekben innen való elérése.

-Minden határ alatti természetes szám vizsgálata -> Csak "Münchausen összeg"-ként előállítható számok vizsgálata.
A Münchausen összeg egy szám számjegyeinek, saját magukkal azonos kitevőjű hatványainak összege. Ha egy szám Münchausen szám akkor egyenlő
saját Münchausen össszegével, tehát előállítható 0^0, 1^1, ... 9^9 számok összegeként. A megoldás csak az ezen számokból előállítható
összegeken megy végig.

Ezen összegek előállítását az 1 számjegyű számok Münchausen összegeivel kezdi, majd mindig a korábbi összegekre építve megy tovább.
Belátható, hogy ha már kiszámoltuk a 2 jegyű számok Münchausen összegeit, a 3 jegyű számok összegei elérhetőek csupán ezen számok
0^0 ... 9^9 számokkal való megnövelésével.

Fontos viszont figyelni a duplikátumok elkerülésére ezért ha egy adott számmal való növelések már megtörténtek, akkor azt követő számoknál
kihagyjuk azokat amiket előző körben növeltünk ezzel a számmal.

Például: 3 jegyű számok összegeit generáljuk, a 0-val való növelések már megtörténtek rendelkezünk a 0^0+0^0+0^0 ... 0^0+9^9+9^9 összegekkel.
Az előző körben 0-val növelt számokat mostmár ignorálni kell, mert minden 3 jegyű szám összege ami ezen 2 jegyű szám összegekből készíthető már
meg van, 1^1+0^0+1^1 = 0^0+1^1+1^1, 4^4+0^0+3^3 = 0^0+4^4+3^3 stb.

-Továbbá nem szükséges olyan Münchausen összeget vizsgálni, ami vagy a felső határ felett van, vagy kevesebb számjegyű, mint az őt előállító
számjegyek száma.
