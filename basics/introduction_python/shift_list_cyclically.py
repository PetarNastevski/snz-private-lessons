'''
Напишете функција која ќе прави поместување на листа за K места во лево и во десно. На почетокот се вчитува листата од стандарден влез, а потоа се вчитува бројот K. Доколку бројот K е негативен поместувањето се извршува во десно, a ако е позитивен поместувањето се извршува во лево.
'''


def shiftList(l, k):            # we define the function --> arguments are the list and the number of positions we need to shift
    k = k % len(l)              # this step solves the problem when k is bigger than the length of the list
    return l[k:] + l[:k]        # slice the list twice and then concatenate them in one list  (here we can see the power of negative indexing in python that we discussed)


if __name__ == '__main__':
    l = list(map(int, input().split(' ')))
    k = int(input())
    # vashiot kod pishuvajte go tuka
    print(shiftList(l, k))
