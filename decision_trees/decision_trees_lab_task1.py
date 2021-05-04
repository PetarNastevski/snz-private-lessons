'''
Да се промени класата за дрво на одлука за да чува и информација на кое ниво во дрвото се наоѓа јазолот.
Потоа да се променат и функциите за градење и печатење на дрвото така што за секој јазол се додава информација за
нивото и се печати и нивото. Коренот е на нулто ниво. Со функцијата print_tree треба да се испечати креираното дрво на
одлука. Прочитана инстанца од стандарден влез да се додаде на тренинг множеството и потоа да се истренира и испечати
дрвото на одлука со ова податочно множество.
'''


from decision_trees_changed import *

trainingData=[['slashdot','USA','yes',18,'None'],          # the sets with which we will train the trees will be list of lists, usually the class will be the last column
        ['google','France','yes',23,'Premium'],
        ['google','France','yes',23,'Basic'],
        ['google','France','yes',23,'Basic'],
        ['digg','USA','yes',24,'Basic'],
        ['kiwitobes','France','yes',23,'Basic'],
        ['google','UK','no',21,'Premium'],
        ['(direct)','New Zealand','no',12,'None'],
        ['(direct)','UK','no',21,'Basic'],
        ['google','USA','no',24,'Premium'],
        ['slashdot','France','yes',19,'None'],
        ['digg','USA','no',18,'None'],
        ['google','UK','no',18,'None'],
        ['kiwitobes','UK','no',19,'None'],
        ['digg','New Zealand','yes',12,'Basic'],
        ['slashdot','UK','no',21,'None'],
        ['google','UK','yes',18,'Basic'],
        ['kiwitobes','France','yes',19,'Basic']]


if __name__ == "__main__":
    referrer = input()
    location = input()
    readFAQ = input()
    pagesVisited = int(input())
    serviceChosen = input()

    testCase = [referrer, location, readFAQ, pagesVisited, serviceChosen]   # from the given inputs we create one test case
    trainingData.append(testCase)          # the requirement says the first we need to add the created instance to the training set
    t = build_tree(trainingData, 0)        # here as we can see we call the build_tree function and we are passing one more argument than normally
    print_tree(t)                          # this argument is the level which starts from 0 and recursively increase
                                           # at the end we just call the changed print_tree function that now prints the level of each node
