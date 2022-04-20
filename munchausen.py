#!/usr/bin/env python3

def main():
    #Futásidő mérés
    import time
    startTime = time.time()
    #A hatványok listájának létrehozása
    powers_list = [0] + [i**i for i in range(1,10)]
    #Dcitionary létrehozása a castolás helyettesítéséhez
    cast_dict = {"0": 0}
    for i in range(1,10):
        cast_dict[str(i)] = i
    #kezdő értékek inicializálása, itt tároljuk az korábban kiszámolt összegeket, minden új értéket egy korábbi összeg megnövelésével képzünk
    prev_sums = powers_list.copy()
    #a duplikátumok eleklürésére szolgáló pontok kezdőértékeinek megadása, (pl az 1+1, 1+2 stb. vizsgyálatok után már a 2+1, 3+1 fölösleges)
    duplicate_avoidance = [0,1,2,3,4,5,6,7,8,9]
    #legkisebb i-számjegyű szám -1 érték kezdőértéke
    min_sum = 9
    #kezdőértékek Münchausen vizsgálata
    for munchausen_sum in prev_sums:
        testsum = 0
        for char in str(munchausen_sum):
            testsum+=powers_list[cast_dict[char]]
        if(munchausen_sum == testsum):
            print(munchausen_sum)
    #fő loop   
    for n in range(2,10):
        #ebben a ciklusban figyelt "előző összegek"-et tároló tömbrész hosszának fixálása
        sums_to_increase = len(prev_sums)
        #a 2. optimális vizsgálási pont megadása 0-val megnövelt számok mennyiségével (a következő ciklusra)
        next_dup_avoid = len(prev_sums)
        #1^1-9^9 számokkal való növelések, illetve az így generált összegek vizsgálása        
        for i in range(1,10):
            for j in range(duplicate_avoidance[i],sums_to_increase):
                munchausen_sum = prev_sums[j]+powers_list[i]
                if(min_sum<munchausen_sum and 440_000_000>munchausen_sum):
                    testsum = 0
                    for char in str(munchausen_sum):
                        testsum+=powers_list[cast_dict[char]]
                    if(munchausen_sum == testsum):
                        print(munchausen_sum)
                prev_sums.append(munchausen_sum)
            #az optimális keresési pontok frissítése a következő ciklusra
            duplicate_avoidance[i],next_dup_avoid = next_dup_avoid,next_dup_avoid+sums_to_increase-duplicate_avoidance[i]
        #i+1 számjegyszámú számok alsó határának frissítése
        min_sum = (min_sum+1)*10-1
    #Futásidő mérés
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))           
#############################################################################

if __name__ == '__main__':
    main()