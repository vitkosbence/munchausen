# munchausen
Megoldás a Münchausen számok megkeresésének optimalizálására pythonban.
10-es számrendszer, 0^0 = 0 értelmezés, 440 millió felső határ a keresésnek.

A megoldás részletei:

-Hatványozás -> 0^0 ... 9^9 hatványok tárolása egy tömbben, későbbiekben innen való elérése.

-Int cast -> 0 ... 9 egyjegyű sztringek és int értékükből álló párok tárolása egy dictionaryban, későbbiekben innen való elérése.

-Minden határ alatti természetes szám vizsgálata -> Csak "Münchausen összeg"-ként előállítható számok vizsgálata. (bővebben pdf)
