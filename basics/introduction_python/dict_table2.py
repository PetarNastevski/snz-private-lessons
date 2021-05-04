'''
Да се креира таблица на трети корени така што решението ќе биде речник во кој клуч е целиот број а вредност ќе биде неговиот трет корен. Клучевите на речникот треба да бидат само природни броеви чиј трети корен е природен број помеѓу m и n. Може да се искористи дел од решението на претходната задача. Потоа за прочитан влез од стандардниот влез да се испечати неговиот трет корен доколку припаѓа на таблицата со корени (речникот) или да се испечати дека нема податоци. Потоа треба да се испечати и добиениот речник во зависност од m и n.
'''

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())
    # vasiot kod pisuvajte go tuka

    # {512: 8, 729: 9, 1000: 10}       # one example for output
    dict = {}                          # we define one empty dictionary
    for i in range(m, n+1):            # we iterate all numbers in the given interval
        key = i*i*i                    # the key this time is the third root of the number
        dict[key] = i                  # the value for each key is that number itself
    if x >=m and x<=n:                 # from here it is the same as in the previous task
        print(dict[x])
    else:
        print("nema podatoci")
    print(dict)