'''
Да се изгради дрво на одлука со даденото множество за тренирање и да се испечати класата која се класифицира за дадениот
тест примерок, така што таа ќе ја печати само класата која ја предвидува (а не речник). Притоа да се провери дали во
листот има повеќе од една класа. Ако има само една класа тогаш се предвидува истата, но ако има повеќе од една треба
да се испечати таа со најголем број на инстанци. Ако во листот има неколку класи со ист број на инстанци да се предвиди
првата класа по азбучен ред.
'''

from decision_trees import *

training_data = [['slashdot', 'USA', 'yes', 18, 'None'],
                 ['google', 'France', 'yes', 23, 'Premium'],
                 ['google', 'France', 'yes', 23, 'Basic'],
                 ['google', 'France', 'yes', 23, 'Basic'],
                 ['digg', 'USA', 'yes', 24, 'Basic'],
                 ['kiwitobes', 'France', 'yes', 23, 'Basic'],
                 ['google', 'UK', 'no', 21, 'Premium'],
                 ['(direct)', 'New Zealand', 'no', 12, 'None'],
                 ['(direct)', 'UK', 'no', 21, 'Basic'],
                 ['google', 'USA', 'no', 24, 'Premium'],
                 ['slashdot', 'France', 'yes', 19, 'None'],
                 ['digg', 'USA', 'no', 18, 'None'],
                 ['google', 'UK', 'no', 18, 'None'],
                 ['kiwitobes', 'UK', 'no', 19, 'None'],
                 ['digg', 'New Zealand', 'yes', 12, 'Basic'],
                 ['slashdot', 'UK', 'no', 21, 'None'],
                 ['google', 'UK', 'yes', 18, 'Basic'],
                 ['kiwitobes', 'France', 'yes', 19, 'Basic']]

if __name__ == "__main__":
    referrer = input()
    location = input()
    read_FAQ = input()
    pages_visited = int(input())
    service_chosen = input()

    test_case = [referrer, location, read_FAQ, pages_visited, service_chosen]

    tree = build_tree(training_data)                                              # train the tree with the given set
    p_class1 = max(classify(test_case, tree).items(), key=lambda x: x[1])[0]      # classify with the trained tree for the given sample on input

    print(p_class1)    #print the classification
