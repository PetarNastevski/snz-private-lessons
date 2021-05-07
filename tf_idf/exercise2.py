'''
Изградете два модели за класификација на документи, со кои ќе се одредува дали даден документ е формален или неформален. Првиот модел е модел на Наивен баесов класификатор. Вториот класификатор е дрво на одлука каде што документите се претставени со tf-idf вектори. Тренирајте ги двата класификатори со соодветното множество за тренирање.

За документот прочитан од стандарден влез испечатете ја класата во која тој припаѓа. Доколку со двата поединечни класификатори се добие истата класа, тогаш се печати таа. Во спротивно се печати непозната (unknown) класа.
'''

from tf_idf import *
from naive_bayes.naive_bayes import *
from decision_trees.decision_trees import *

train_data = [
    ("""I like Rhythm and Blue music.""", 'formal'),
    ("""Back in my day Emo was a comedian :/""", 'informal'),
    ("""Why sit and listen to Locke, Jack, or Syead?""", 'informal'),
    ("""There's nothing he needs to change.""", 'formal'),
    ("""It does not exist.""", 'formal'),
    ("""I like when the Prime Minister goes door to door to find the girl!""", 'informal'),
    ("""Mine is book by Steve Martin called 'The Pleasure of my Company'.""", 'formal'),
    ("""What differentiates a mosquitoo from a blonde?""", 'formal'),
    ("""They're pretty good. Also, that's a good song.""", 'formal'),
    ("""And every time I hear that song I get butterflies in my stomach!""", 'informal'),
    ("""It's the biggest load of crap I've seen for ages.""", 'informal'),
    ("""I do not think Beyonce can sing, dance, or act. You mentioned Rihanna, who is that?""", 'formal'),
    ("""as i lay dying is far far away from christ definitaly!""", 'informal'),
    ("""I was unaware that you were in law enforcement, as well.""", 'formal'),
    ("""I might be seeing them in a few months!""", 'informal'),
    ("""I called to say 'I Love You""", 'formal'),
    ("""that´s why they needed to open that hatch so much!""", 'informal'),
    (
    """I would most likely not vote for him, although I believe Melania would be the most attractive First Lady in our country's history.""",
    'formal'),
    ("""I do not hate him.""", 'formal'),
    ("""He's supposed to be in jail!""", 'informal'),
    ("""i thought that she did an outstanding job in the movie""", 'informal'),
    ("""Nicole Kidman, I love her eyes""", 'informal'),
    ("""Youtube.com also features many of the current funny ads.""", 'formal'),
    ("""I enjoy watching my companion attempt to role-play with them.""", 'formal'),
    ("""omg i love that song im listening to it right now""", 'informal'),
    ("""Some of my favorite television series are Monk, The Dukes of Hazzard, Miami Vice, and The Simpsons.""",
     'formal'),
    ("""I have a desire to produce videos on Full Metal Alchemist.""", 'formal'),
    ("""tell him you want a 3 way with another hot girl""", 'informal'),
    (
    """I would travel to that location and physically assault you at this very moment, however, I am unable to swim.""",
    'formal'),
    ("""No, no, no that was WITNESS...""", 'informal'),
    ("""aneways shonenjump.com is cool and yeah narutos awsum""", 'informal'),
    (
    """Your mother is so unintelligent that she was hit by a cup and told the police that she was mugged.""", 'formal'),
    ("""You must be creative and find something to challange us.""", 'formal'),
    ("""i think they would have, quite a shame isn't it""", 'informal'),
    ("""I am watching it right now.""", 'formal'),
    ("""I do not know; the person who invented the names had attention deficit disorder.""", 'formal'),
    ("""im a huge green day fan!!!!!""", 'informal'),
    ("""I believe, rather, that they are not very smart on this topic.""", 'formal'),
    ("""Of course it is Oprah, because she has been providing better advice for a longer time.""", 'formal'),
    ("""Chicken Little my son loves that movie I have to watch at least 4 times a day!""", 'informal'),
    ("""That is the key point, that you fell asleep.""", 'formal'),
    ("""A brunette female, a blonde, and person with red hair walked down a street.""", 'formal'),
    ("""who is your best bet for american idol season five""", 'informal'),
    ("""That is funny.  Girls need to be a part of everything.""", 'formal'),
    ("""In point of fact, Chris's performance looked like the encoure performed at a Genesis concert.""", 'formal'),
    ("""In my time, Emo was a comedian.""", 'formal'),
    ("""my age gas prices and my blood pressure  LOL""", 'informal'),
    ("""Moriarty and so forth, but what character did the Peruvian actor portray?""", 'formal'),
    ("""What did the beaver say to the log?""", 'formal'),
    ("""Where in the world do you come up with these questions????""", 'informal'),
    ("""even though i also agree that the girls on Love Hina are pretty scrumptious""", 'informal'),
    ("""I miss Aaliyah, she was a great singer.""", 'formal'),
    ("""and the blond says Great they already put me on my first murder mystery case""", 'informal'),
]

if __name__ == '__main__':
    recenica = input()

    classifier = NaiveBayes(get_words)  # make one Naive Baes classifier

    for row in train_data:  # train it with the given dataset
        classifier.train(row[0], row[1])

    pred_baes = classifier.classify_document(
        recenica)  # predict for the given input (returns just class so we need to do nothing more)

    docs = []  # we need separately sentences and labels so we can make set list of lists(vectors) compatible for decision_trees
    labels = []

    for row in train_data:
        docs.append(row[0])         # two separate lists for sentences and labels
        labels.append(row[1])

    dataset, df, n, vocab = create_dataset(docs,
                                           labels)  # the result from create dataset is set list of vectors that is compatible with decision trees ---> we will use everything else to turn test sentences to vectors so we can predict for them with the trained tree
    # df = calculate_document_frequencies(docs)
    # n = len(docs)
    # vocab = get_vocabulary(docs)    # these 3 are all called in create dataset
    tree = build_tree(dataset)  # train the tree with the vectors
    vec_in = process_document(recenica, df, n,
                              vocab)  # the sentence on input has to be casted to vector also ---> because if not the tree cannot recognize it
    pred_tree = max(classify(vec_in, tree).items(), key=lambda x: x[1])[0]   # predict with the tree and take the prediction out of the dictionary

    if pred_tree == pred_baes:     # if both predictions are the same then print it if not unknown
        print(pred_tree)
    else:
        print("unknown")