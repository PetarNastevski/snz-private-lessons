'''
Изградете 2 дрва на одлука. Едното дрво на одлука ќе ја користи првата половина од податочното множество,
а другото дрво, втората половина. Доколку двете дрва на одлука на тест примерот го дадат истиот резултат,
да се испечати тој резултат. Доколку дадат различен резултат, да се испечати KONTRADIKCIJA.
Доколку некое од дрвата има само една класа тогаш се предвидува истата, но ако има повеќе од една треба да се избере
таа со најголем број на инстанци. Ако во листот има неколку класи со ист број на инстанци да се предвиде првата класа
по азбучен ред.
'''

from decision_trees import *

trainingData = [
    [6.3, 2.9, 5.6, 1.8, 'I. virginica'],
    [6.5, 3.0, 5.8, 2.2, 'I. virginica'],
    [7.6, 3.0, 6.6, 2.1, 'I. virginica'],
    [4.9, 2.5, 4.5, 1.7, 'I. virginica'],
    [7.3, 2.9, 6.3, 1.8, 'I. virginica'],
    [6.7, 2.5, 5.8, 1.8, 'I. virginica'],
    [7.2, 3.6, 6.1, 2.5, 'I. virginica'],
    [6.5, 3.2, 5.1, 2.0, 'I. virginica'],
    [6.4, 2.7, 5.3, 1.9, 'I. virginica'],
    [6.8, 3.0, 5.5, 2.1, 'I. virginica'],
    [5.7, 2.5, 5.0, 2.0, 'I. virginica'],
    [5.8, 2.8, 5.1, 2.4, 'I. virginica'],
    [6.4, 3.2, 5.3, 2.3, 'I. virginica'],
    [6.5, 3.0, 5.5, 1.8, 'I. virginica'],
    [7.7, 3.8, 6.7, 2.2, 'I. virginica'],
    [7.7, 2.6, 6.9, 2.3, 'I. virginica'],
    [6.0, 2.2, 5.0, 1.5, 'I. virginica'],
    [6.9, 3.2, 5.7, 2.3, 'I. virginica'],
    [5.6, 2.8, 4.9, 2.0, 'I. virginica'],
    [7.7, 2.8, 6.7, 2.0, 'I. virginica'],
    [6.3, 2.7, 4.9, 1.8, 'I. virginica'],
    [6.7, 3.3, 5.7, 2.1, 'I. virginica'],
    [7.2, 3.2, 6.0, 1.8, 'I. virginica'],
    [6.2, 2.8, 4.8, 1.8, 'I. virginica'],
    [6.1, 3.0, 4.9, 1.8, 'I. virginica'],
    [6.4, 2.8, 5.6, 2.1, 'I. virginica'],
    [7.2, 3.0, 5.8, 1.6, 'I. virginica'],
    [7.4, 2.8, 6.1, 1.9, 'I. virginica'],
    [7.9, 3.8, 6.4, 2.0, 'I. virginica'],
    [6.4, 2.8, 5.6, 2.2, 'I. virginica'],
    [6.3, 2.8, 5.1, 1.5, 'I. virginica'],
    [6.1, 2.6, 5.6, 1.4, 'I. virginica'],
    [7.7, 3.0, 6.1, 2.3, 'I. virginica'],
    [6.3, 3.4, 5.6, 2.4, 'I. virginica'],
    [5.1, 3.5, 1.4, 0.2, 'I. setosa'],
    [4.9, 3.0, 1.4, 0.2, 'I. setosa'],
    [4.7, 3.2, 1.3, 0.2, 'I. setosa'],
    [4.6, 3.1, 1.5, 0.2, 'I. setosa'],
    [5.0, 3.6, 1.4, 0.2, 'I. setosa'],
    [5.4, 3.9, 1.7, 0.4, 'I. setosa'],
    [4.6, 3.4, 1.4, 0.3, 'I. setosa'],
    [5.0, 3.4, 1.5, 0.2, 'I. setosa'],
    [4.4, 2.9, 1.4, 0.2, 'I. setosa'],
    [4.9, 3.1, 1.5, 0.1, 'I. setosa'],
    [5.4, 3.7, 1.5, 0.2, 'I. setosa'],
    [4.8, 3.4, 1.6, 0.2, 'I. setosa'],
    [4.8, 3.0, 1.4, 0.1, 'I. setosa'],
    [4.3, 3.0, 1.1, 0.1, 'I. setosa'],
    [5.8, 4.0, 1.2, 0.2, 'I. setosa'],
    [5.7, 4.4, 1.5, 0.4, 'I. setosa'],
    [5.4, 3.9, 1.3, 0.4, 'I. setosa'],
    [5.1, 3.5, 1.4, 0.3, 'I. setosa'],
    [5.7, 3.8, 1.7, 0.3, 'I. setosa'],
    [5.1, 3.8, 1.5, 0.3, 'I. setosa'],
    [5.4, 3.4, 1.7, 0.2, 'I. setosa'],
    [5.1, 3.7, 1.5, 0.4, 'I. setosa'],
    [4.6, 3.6, 1.0, 0.2, 'I. setosa'],
    [5.1, 3.3, 1.7, 0.5, 'I. setosa'],
    [4.8, 3.4, 1.9, 0.2, 'I. setosa'],
    [5.0, 3.0, 1.6, 0.2, 'I. setosa'],
    [5.0, 3.4, 1.6, 0.4, 'I. setosa'],
    [5.2, 3.5, 1.5, 0.2, 'I. setosa'],
    [5.2, 3.4, 1.4, 0.2, 'I. setosa'],
    [5.5, 2.3, 4.0, 1.3, 'I. versicolor'],
    [6.5, 2.8, 4.6, 1.5, 'I. versicolor'],
    [5.7, 2.8, 4.5, 1.3, 'I. versicolor'],
    [6.3, 3.3, 4.7, 1.6, 'I. versicolor'],
    [4.9, 2.4, 3.3, 1.0, 'I. versicolor'],
    [6.6, 2.9, 4.6, 1.3, 'I. versicolor'],
    [5.2, 2.7, 3.9, 1.4, 'I. versicolor'],
    [5.0, 2.0, 3.5, 1.0, 'I. versicolor'],
    [5.9, 3.0, 4.2, 1.5, 'I. versicolor'],
    [6.0, 2.2, 4.0, 1.0, 'I. versicolor'],
    [6.1, 2.9, 4.7, 1.4, 'I. versicolor'],
    [5.6, 2.9, 3.6, 1.3, 'I. versicolor'],
    [6.7, 3.1, 4.4, 1.4, 'I. versicolor'],
    [5.6, 3.0, 4.5, 1.5, 'I. versicolor'],
    [5.8, 2.7, 4.1, 1.0, 'I. versicolor'],
    [6.2, 2.2, 4.5, 1.5, 'I. versicolor'],
    [5.6, 2.5, 3.9, 1.1, 'I. versicolor'],
    [5.9, 3.2, 4.8, 1.8, 'I. versicolor'],
    [6.1, 2.8, 4.0, 1.3, 'I. versicolor'],
    [6.3, 2.5, 4.9, 1.5, 'I. versicolor'],
    [6.1, 2.8, 4.7, 1.2, 'I. versicolor'],
    [6.4, 2.9, 4.3, 1.3, 'I. versicolor'],
    [6.6, 3.0, 4.4, 1.4, 'I. versicolor'],
    [6.8, 2.8, 4.8, 1.4, 'I. versicolor'],
    [6.7, 3.0, 5.0, 1.7, 'I. versicolor'],
    [6.0, 2.9, 4.5, 1.5, 'I. versicolor'],
    [5.7, 2.6, 3.5, 1.0, 'I. versicolor'],
    [5.5, 2.4, 3.8, 1.1, 'I. versicolor'],
    [5.5, 2.4, 3.7, 1.0, 'I. versicolor'],
    [5.8, 2.7, 3.9, 1.2, 'I. versicolor'],
    [6.0, 2.7, 5.1, 1.6, 'I. versicolor'],
    [5.4, 3.0, 4.5, 1.5, 'I. versicolor'],
    [6.0, 3.4, 4.5, 1.6, 'I. versicolor'],
    [6.7, 3.1, 4.7, 1.5, 'I. versicolor'],
    [6.3, 2.3, 4.4, 1.3, 'I. versicolor'],
    [5.6, 3.0, 4.1, 1.3, 'I. versicolor'],
    [5.5, 2.5, 4.0, 1.3, 'I. versicolor'],
    [5.5, 2.6, 4.4, 1.2, 'I. versicolor'],
    [6.1, 3.0, 4.6, 1.4, 'I. versicolor'],
    [5.8, 2.6, 4.0, 1.2, 'I. versicolor'],
    [5.0, 2.3, 3.3, 1.0, 'I. versicolor'],
    [5.6, 2.7, 4.2, 1.3, 'I. versicolor'],
    [5.7, 3.0, 4.2, 1.2, 'I. versicolor'],
    [5.7, 2.9, 4.2, 1.3, 'I. versicolor'],
    [6.2, 2.9, 4.3, 1.3, 'I. versicolor'],
    [5.1, 2.5, 3.0, 1.1, 'I. versicolor'],
    [5.7, 2.8, 4.1, 1.3, 'I. versicolor'],
    [6.4, 3.1, 5.5, 1.8, 'I. virginica'],
    [6.0, 3.0, 4.8, 1.8, 'I. virginica'],
    [6.9, 3.1, 5.4, 2.1, 'I. virginica'],
    [6.7, 3.1, 5.6, 2.4, 'I. virginica'],
    [6.9, 3.1, 5.1, 2.3, 'I. virginica'],
    [5.8, 2.7, 5.1, 1.9, 'I. virginica'],
    [6.8, 3.2, 5.9, 2.3, 'I. virginica'],
    [6.7, 3.3, 5.7, 2.5, 'I. virginica'],
    [6.7, 3.0, 5.2, 2.3, 'I. virginica'],
    [6.3, 2.5, 5.0, 1.9, 'I. virginica'],
    [6.5, 3.0, 5.2, 2.0, 'I. virginica'],
    [6.2, 3.4, 5.4, 2.3, 'I. virginica'],
    [4.7, 3.2, 1.6, 0.2, 'I. setosa'],
    [4.8, 3.1, 1.6, 0.2, 'I. setosa'],
    [5.4, 3.4, 1.5, 0.4, 'I. setosa'],
    [5.2, 4.1, 1.5, 0.1, 'I. setosa'],
    [5.5, 4.2, 1.4, 0.2, 'I. setosa'],
    [4.9, 3.1, 1.5, 0.2, 'I. setosa'],
    [5.0, 3.2, 1.2, 0.2, 'I. setosa'],
    [5.5, 3.5, 1.3, 0.2, 'I. setosa'],
    [4.9, 3.6, 1.4, 0.1, 'I. setosa'],
    [4.4, 3.0, 1.3, 0.2, 'I. setosa'],
    [5.1, 3.4, 1.5, 0.2, 'I. setosa'],
    [5.0, 3.5, 1.3, 0.3, 'I. setosa'],
    [4.5, 2.3, 1.3, 0.3, 'I. setosa'],
    [4.4, 3.2, 1.3, 0.2, 'I. setosa'],
    [5.0, 3.5, 1.6, 0.6, 'I. setosa'],
    [5.1, 3.8, 1.9, 0.4, 'I. setosa'],
    [4.8, 3.0, 1.4, 0.3, 'I. setosa'],
    [5.1, 3.8, 1.6, 0.2, 'I. setosa'],
    [5.9, 3.0, 5.1, 1.8, 'I. virginica']
]

if __name__ == "__main__":
    att1 = float(input())
    att2 = float(input())
    att3 = float(input())
    att4 = float(input())
    planttype = input()
    testCase = [att1, att2, att3, att4, planttype]

    length = len(trainingData) // 2     # we get the size of the training set and we divide it with // --> integer divison
                                        # because we want to slice based on this number and we dont want it to be decimal
    train1 = trainingData[:length]      # we slice the set in to two different sets first and second 50% of the samples
    train2 = trainingData[length:]

    tree1 = build_tree(train1)          # we train two trees the first one with the first 50% of the samples and the
    tree2 = build_tree(train2)          # second one with the second 50%

    # from now one we will use this way to extract the class from the dictionary that we get after the prediction with trees
    p_class1 = max(classify(testCase, tree1).items(), key=lambda x: x[1])[0]   # we turn the dictionary to list of tuples with .items(), after that with the inline anonymous func lambda we are looking for
    p_class2 = max(classify(testCase, tree2).items(), key=lambda x: x[1])[0]   # the tuple that has the max biggest val of all other tuples in the list on pos 1 which is the val from the dictionary
                                                                               # the last part [0] is because max will return the whole tuple and we need only the key (predicted_class) so we store what is on pos 0 in the tuple
    if p_class1 == p_class2:     # if we get the same class with both trees we print that class
        print(p_class1)
    else:
        print("KONTRADIKCIJA")    # if not we print contradiction