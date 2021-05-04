'''
Да се направи таблица на степени, кубови и квадратни корени на броевите од m до n, така што резултатот ќе се чува во речник на кој клучот е самиот број, а вредноста е торка од облик (квадрат, куб, корен). Пр:

{1:(1,1,1), 2:(4,8,1.1412), …}

Потоа да се искористи речникот така што за прочитан број од стандардниот влез ќе ја испечати торката која е соодветна на бројот или да испечати “nema podatoci” доколку прочитаниот број е надвор од интервалот. Исто така треба да се испечати целиот речник (во зависност од прочитаните m и n).
'''

import math

if __name__ == "__main__":
    m = int(input())             # we have three given integers on std input
    n = int(input())
    x = int(input())
    # vasiot kod pisuvajte go tuka
    dict = {}
    for i in range(m, n + 1):                       # the interval starts from m and goes to n (n number is included in the interval)
        dict[i] = (i ** 2, i ** 3, math.sqrt(i))    # the key is each number of the interval and the value is tuple that has three values inside ---> square, cube and root of the key number
    if x >= m and x <= n:                           # we check if the given number is in the given interval then we print the tuple for that key on stdout
        print(dict[x])
    else:
        print("nema podatoci")
    print(dict)                                     # at the end we print the whole dictionary
