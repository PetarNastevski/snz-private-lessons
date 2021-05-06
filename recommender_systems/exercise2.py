'''
Во речникот ratings се чуваат информации за оцени на филмови. Клуч е името на корисникот и вредност е речник чиј клуч е
филмот, а вредност е оцената која корисникот ја дал за филмот. За името на корисникот прочитано од стандарден влез да се
препорача филм на следниот начин. Прво се прави препорака според најслични корисници користејќи евклидово растојание и
пирсонов коефициент на корелација како метрика за сличност. Доколку со двете метрики за сличност се добие истиот филм,
тогаш се печати тој филм. Во спротивно, се прави препорака според најслични филмови. Доколку препорачаниот филм според
најслични филмови е еднаков со некој од препорачаните филмови според најслични корисници (препорачаниот филм со евклидово
растојание и препорачаниот филм со пирсонов коефициент на корелација), тогаш се печати тој филм. Во спротивно се печати
филмот кој има највисока вредност за препорака.
'''


from recommender_systems import *


ratings = {
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

if __name__ == '__main__':
    user_name = input()

    rec_user_pear = get_recommendations(ratings, user_name, sim_pearson)     # get both user recommendations (using sim_pearson and sim_distance)
    rec_user_ekvi = get_recommendations(ratings, user_name, sim_distance)

    if rec_user_pear[0][1] == rec_user_ekvi[0][1]:     # if they are both the same just print one of them
        print(rec_user_ekvi[0][1])
    else:
        inverted = transform_prefs(ratings)            # if not make item based recommendation
        rec_item = get_recommendations_item_based(inverted, user_name)
        if rec_item[0][1] == rec_user_ekvi[0][1] or rec_item[0][1] == rec_user_pear[0][1]:   # if that recommendation is the same with either of the other two
            print(rec_item[0][1])      # print that
        else:
            maks = -99999              # if not find the movie that has the highest grade given from some user based on the given dataset
            movie = None
            for item in inverted.keys():               # iterate each movie
                for grade in inverted[item].values():  # iterate the grades for that movie
                    if grade >= maks:                  # if the grade is the biggest found grade save it and save the corresponding movie
                        maks = grade
                        movie = item
                # suma = sum(svrteno[item].values())    # if we needed to find the movie with the biggest sum of all grades for that movie
                # if suma > maks:
                #     maks = suma
                #     film = item
            print(movie)                                 # print previously saved movie
