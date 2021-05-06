'''
Потребно е да изградите систем за препорака на филмови за корисниците. Најпрво поделете го иницијалното множество на
множество за тренирање и множество за тестирање, така што множеството за тестирање ќе биде составено од корисниците
проследени на стандарден влез, додека множеството за тренирање ги вклучува сите останати корисници.

При давањето на препорака за даден корисник од тестирачкото множество, потребно е множеството за тренирање да не ги
содржи корисниците од тестирачкото множество, освен моменталниот корисник за кој се изведува препораката
(кој треба да е вклучен во множеството при одредување на препораките). Пример: доколку корисниците 1, 2, 3 се дел
од тестирачкото множество потребно е при предвидување на препорака на корисникот 1 од целокупното множество со сите
корисници да не се земаат во предвид корисниците 2 и 3, при препорака за корисникот 2 не треба да се земаат во предвид
корисниците 1 и 3, а при препорака на корисникот 3 не треба да се земаат во предвид корисниците 1 и 2 соодветно.

На стандарден излез испринтајте ги првите три препораки за музичките изведувачи за секој од корисниците во множеството
за тестирање. Користете систем за препорака базиран на корисниците и Пирсонова корелација.
'''

from recommender_systems import *


ratings = {
    'Lisa Rose': {'Catch Me If You Can': 3.0 , 'Snakes on a Plane': 3.5, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0, 'Snitch': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5,  'The Night Listener': 3.0,'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Catch Me If You Can': 2.5, 'Lady in the Water': 2.5,'Superman Returns': 3.5, 'The Night Listener': 4.0, 'Snitch': 2.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,'The Night Listener': 4.5, 'Superman Returns': 4.0,'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'Just My Luck': 2.0, 'Superman Returns': 3.0, 'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Catch Me If You Can': 4.5, 'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'Snitch': 4.5},
    'Toby': {'Snakes on a Plane':4.5, 'Snitch': 5.0},
    'Michelle Nichols': {'Just My Luck' : 1.0, 'The Night Listener': 4.5, 'You, Me and Dupree': 3.5, 'Catch Me If You Can': 2.5, 'Snakes on a Plane': 3.0},
    'Gary Coleman': {'Lady in the Water': 1.0, 'Catch Me If You Can': 1.5, 'Superman Returns': 1.5, 'You, Me and Dupree': 2.0},
    'Larry': {'Lady in the Water': 3.0, 'Just My Luck': 3.5, 'Snitch': 1.5, 'The Night Listener': 3.5}
    }


if __name__ == '__main__':
    test_users = list(input().split(", "))       # we have list of users for testing on input
    data_test= {}                                # two sets in one we will put the users that will help us test our recommendation system and in another the users that will help us train it
    data_train = {}
    for user in ratings.keys():                  # we iterate the users(keys) in the given set
        if user in test_users:                   # if the user is in the list on input we will use that user for testing if not for training
            data_test[user] = ratings[user]
        else:
            data_train[user] = ratings[user]
    output = ''                                  # there are more sophisticated ways to do it but to be sure that everyone understands i will concatenate one string to get the desired output
    for user in test_users:                      # now we iterate the testing users
        output = user + ': '
        data_train[user] = data_test[user]       # in order to get recommendations for the user we need to put him in to the training set ---> if not we will get key error
        rec = get_recommendations(data_train, user, sim_pearson)   # we recommend for that user
        data_train.pop(user)      # and take him out immediately as we do not want to affect the recommendations for other users from the test set
        counter = 0
        for el in rec:                          # rec is sorted list of tuples where the most recommended item is tuple at the first place(index 0 in the tuple is the value index1 is predicted movie)
            output = output + el[1] + '; '      # concatenate each movie to the output
            counter += 1
            if counter == 3:                    # because we get sorted list of recommendations we break after getting the first 3 ---> another way is to make the cycle stop at 3 like this [:3]
                break
        if output == user + ': ':               # if the recommendation list is empty
            output = output + 'no recommendations ...'   # we concatenate this to the user name
            print(output)
        else:
            print(output[:-2])