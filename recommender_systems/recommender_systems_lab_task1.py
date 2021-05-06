'''
Дадено е множество кое е претставено како речник чиј клуч е името на корисникот и вредност како речник чиј клуч е филмот,
а вредност е оцената која корисникот ја дал за филмот. Да се напише функција која ќе генерира табела на слични корисници
претставена како речник од речници (клучеви се имињата на корисниците), така што за секој пар корисници ќе чува торка од
сличност базирана на Пеарсонова корелација, сличност базирана на Евклидово растојание, и број на заеднички оцени
(оцени дадени за исти филмови). Вредностите да бидат заокружени на 3 децимали. За прочитани имиња на двајца корисници
да се испечати торката која се чува во генерираната табела.
'''


from recommender_systems import *

movie_reviews = {
    'Lisa Rose': {'Catch Me If You Can': 3.0, 'Snakes on a Plane': 3.5, 'Superman Returns': 3.5,
                  'You, Me and Dupree': 2.5, 'The Night Listener': 3.0, 'Snitch': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'The Night Listener': 3.0,
                     'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Catch Me If You Can': 2.5, 'Lady in the Water': 2.5, 'Superman Returns': 3.5,
                         'The Night Listener': 4.0, 'Snitch': 2.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0,
                     'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0,
                     'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Catch Me If You Can': 4.5, 'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                      'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'Snitch': 4.5},
    'Toby': {'Snakes on a Plane': 4.5, 'Snitch': 5.0},
    'Michelle Nichols': {'Just My Luck': 1.0, 'The Night Listener': 4.5, 'You, Me and Dupree': 3.5,
                         'Catch Me If You Can': 2.5, 'Snakes on a Plane': 3.0},
    'Gary Coleman': {'Lady in the Water': 1.0, 'Catch Me If You Can': 1.5, 'Superman Returns': 1.5,
                     'You, Me and Dupree': 2.0},
    'Larry': {'Lady in the Water': 3.0, 'Just My Luck': 3.5, 'Snitch': 1.5, 'The Night Listener': 3.5}
}

# in these exercises we will work with dictionaries as training sets


def number_same_movies(user1, user2, data_set):     # function that will count the number of the same movies rated by two users
    counter = 0
    for movie1 in data_set[user1].keys():          # iterate the keys(movies) from the inner dictionary which is value for the key user --> this means that the movies rated by the user are store in another dictionary where keys are the movies and values are the grades
        for movie2 in data_set[user2].keys():      # double cycle to check everyone with everyone
            if movie1 == movie2:                   # if two different users rated the same movie we count
                counter += 1
    return counter


def similar_users_table(reviews):                 # the function that will create the requested table
    similar = {}                                  # this is the main dictionary that will look like this  {user1: {user2: (sim_pearson, sim_distance, num_rated_movies), user3: (sim_pearson, sim_distance, num_rated_movies)..}, user2: {}}..

    for user1 in movie_reviews.keys():            # we iterate all users for each user we calculate the three values with everyone else
        dict_2 = {}                               # inner dictionary restarted for every user
        for user2 in movie_reviews.keys():        # we iterate everyone else
            if user1 == user2:                    # make sure that we are not doing the calculations for the same user
                continue
            pear = sim_pearson(reviews, user1, user2)    # calculate
            ekvi = sim_distance(reviews, user1, user2)
            dict_2[user2] = (round(ekvi, 3), round(pear, 3), number_same_movies(user1, user2, reviews))   # the keys in the inner dictionary are the users the values are the calculations stored in a tuple
        similar[user1] = dict_2    # now we put the inner dict as value for each user
    return similar    # return the created table


if __name__ == "__main__":
    user1 = input()             # two users on input
    user2 = input()

    table = similar_users_table(movie_reviews)       # create the table
    print(table[user1][user2])                       # find the tuple value for the two users on input
